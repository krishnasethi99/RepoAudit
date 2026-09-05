from pathlib import Path

def entrypoint_analyzer(ast_info):
    result = {
        "likely_entrypoint": None,
        "all_entrypoints": []
    }
    priority = [
        "main.py",
        "app.py",
        "run.py",
        "manage.py"
    ]

    result["all_entrypoints"] = sorted(
        ast_info.get("entrypoints", [])
    )

    for priority_file in priority:
        for entrypoint in result["all_entrypoints"]:
            if Path(entrypoint).name.lower() == priority_file:
                result["likely_entrypoint"] = entrypoint
                return result

    if result["all_entrypoints"]:
        result["likely_entrypoint"] = result["all_entrypoints"][0]

    return result