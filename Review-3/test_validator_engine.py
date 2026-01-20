import unittest
from validator_engine import compile_rules, validate

class TestValidatorEngine(unittest.TestCase):
    def setUp(self):
        rules = [
            {
                "field": "name",
                "path": "user.name",
                "checks": [
                    {"type": "required"},
                    {"type": "string"},
                    {"type": "allow", "pattern": r"[A-Za-z ]+"}
                ]
            },
            {
                "field": "bio",
                "path": "user.bio",
                "checks": [
                    {"type": "string"},
                    {"type": "block", "pattern": r"<\s*script.*?>"},
                    {"type": "block", "pattern": r"\b(drop|select|delete|insert)\b"}
                ]
            }
        ]
        self.compiled = compile_rules(rules)

    def test_valid_payload(self):
        payload = {"user": {"name": "Vinod Kumar", "bio": "Backend dev"}}
        result = validate(payload, self.compiled)
        self.assertTrue(result["valid"])
        self.assertEqual(result["errors"], [])

    def test_required_fail(self):
        payload = {"user": {"bio": "Hello"}}
        result = validate(payload, self.compiled)
        self.assertFalse(result["valid"])
        self.assertTrue(any(e["code"] == "REQUIRED" for e in result["errors"]))

    def test_type_fail(self):
        payload = {"user": {"name": 99, "bio": "Hello"}}
        result = validate(payload, self.compiled)
        self.assertFalse(result["valid"])
        self.assertTrue(any(e["code"] == "TYPE_ERROR" for e in result["errors"]))

    def test_allow_regex_fail(self):
        payload = {"user": {"name": "Vinod123", "bio": "Hello"}}
        result = validate(payload, self.compiled)
        self.assertFalse(result["valid"])
        self.assertTrue(any(e["code"] == "INVALID_FORMAT" for e in result["errors"]))

    def test_block_script(self):
        payload = {"user": {"name": "Vinod", "bio": "<script>alert(1)</script>"}}
        result = validate(payload, self.compiled)
        self.assertFalse(result["valid"])
        self.assertTrue(any(e["code"] == "MALFORMED_TEXT" for e in result["errors"]))

    def test_block_sql_keywords(self):
        payload = {"user": {"name": "Vinod", "bio": "DROP table users"}}
        result = validate(payload, self.compiled)
        self.assertFalse(result["valid"])
        self.assertTrue(any(e["code"] == "MALFORMED_TEXT" for e in result["errors"]))

if __name__ == "__main__":
    unittest.main()
