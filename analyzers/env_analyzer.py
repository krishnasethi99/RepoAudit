def env_analyzer(repo_info, ast_info):
    result = {
        "used_env_vars": set(),
        "declared_env_vars": set(),
        "missing_env_vars": set()
    }

    result["used_env_vars"] = set(ast_info.get("env_vars", []))
    env_example_files = repo_info.get("env_example_files",[])

    for file in env_example_files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith("#"):
                        continue
                    if "=" not in line:
                        continue

                    key = line.split("=", 1)[0].strip()
                    if key:
                        result["declared_env_vars"].add(key)

        except Exception as e:
            print(f"Error reading env file {file}: {e}")

    result["missing_env_vars"] = (result["used_env_vars"]- result["declared_env_vars"])

    result["used_env_vars"] = sorted(result["used_env_vars"])
    result["declared_env_vars"] = sorted(result["declared_env_vars"])
    result["missing_env_vars"] = sorted(result["missing_env_vars"])

    return result