from validator_engine import compile_rules, validate

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

compiled = compile_rules(rules)

payload = {
    "user": {
        "name": "Vinod123",
        "bio": "<script>alert(1)</script>"
    }
}

result = validate(payload, compiled)
print(result)
