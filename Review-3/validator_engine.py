import re
def compile_rules(rules):
    compiled = []
    for r in rules:
        checks = []
        for chk in r.get("checks", []):
            if chk["type"] in ("allow", "block"):
                checks.append({
                    "type": chk["type"],
                    "rx": re.compile(chk["pattern"], re.IGNORECASE)
                })
            else:
                checks.append({"type": chk["type"]})

        compiled.append({
            "field": r["field"],
            "path": r["path"],
            "checks": checks
        })
    return compiled

def validate(payload, compiled_rules):
    errors = []

    for rule in compiled_rules:
        field = rule["field"]
        path = rule["path"]

        cur = payload
        for key in path.split("."):
            if not isinstance(cur, dict) or key not in cur:
                cur = None
                break
            cur = cur[key]

        value = cur

        for chk in rule["checks"]:
            t = chk["type"]

            if t == "required":
                if value is None or (isinstance(value, str) and value.strip() == ""):
                    errors.append({
                        "field": field,
                        "path": path,
                        "code": "REQUIRED",
                        "message": "Field is required."
                    })

            elif t == "string":
                if value is not None and not isinstance(value, str):
                    errors.append({
                        "field": field,
                        "path": path,
                        "code": "TYPE_ERROR",
                        "message": "Expected a string."
                    })

            elif t == "allow":
                if isinstance(value, str) and not chk["rx"].fullmatch(value):
                    errors.append({
                        "field": field,
                        "path": path,
                        "code": "INVALID_FORMAT",
                        "message": "Invalid format."
                    })

            elif t == "block":
                if isinstance(value, str) and chk["rx"].search(value):
                    errors.append({
                        "field": field,
                        "path": path,
                        "code": "MALFORMED_TEXT",
                        "message": "Forbidden pattern found."
                    })

    return {"valid": len(errors) == 0, "errors": errors}
