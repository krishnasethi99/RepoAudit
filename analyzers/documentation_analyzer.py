
def doc_analyzer(repo_info):
    EXPECTED_SECTIONS = {
        "installation": [
            "installation",
            "install",
            "setup",
            "getting started"
        ],

        "usage": [
            "usage",
            "run",
            "quick start",
            "example"
        ],

        "configuration": [
            "configuration",
            "config",
            "environment",
            ".env",
            "settings"
        ],

        "contributing": [
            "contributing",
            "contribution"
        ]
    }
    result = {
        "has_readme": False,
        "sections_found": [],
        "missing_sections": []
    }
    readme_file = repo_info.get("primary_readme")
    if not readme_file:
        return result

    try:
        with open(readme_file, "r", encoding="utf-8") as f:
            content = f.read().lower()
    except Exception:
        return result
    result["has_readme"] = True

    for section, keywords in EXPECTED_SECTIONS.items():
        found = False

        for keyword in keywords:

            if keyword in content:
                found = True
                break

        if found:
            result["sections_found"].append(section)
        else:
            result["missing_sections"].append(section)
    return result