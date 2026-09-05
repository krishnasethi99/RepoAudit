def scan_repository(repo_path):
    repo_info = {
        "has_readme": False,
        "has_dockerfile": False,
        "has_requirements": False,
        "has_pyproject": False,
        "has_env_example": False,
        "total_files": 0,
        "total_python_files": 0,
        "total_markdown_files": 0,
        "total_env_files": 0,
        "python_files": [],
        "requirements_file": [],
        "pyproject_file": [],
        "env_example_files": [],
        "readme_files": [],
        "primary_readme": None,
        "repo_path": repo_path,
        "repository_name": repo_path.name,
    }

    IGNORE_DIRS = {
        "tests",
        "test",
        "docs",
        "examples",
        "example",
        "benchmarks",
        ".venv",
        "venv",
        "__pycache__",
        ".git",
        "build",
        "dist",
    }

    if not repo_path:
        print("No repository path provided. Aborting scan.")
        return

    for file in repo_path.rglob("*"):
        if any(part.lower() in IGNORE_DIRS for part in file.parts):
            continue

        if file.name.lower() in {"readme.md", "readme"}:
            repo_info["has_readme"] = True
            repo_info["readme_files"].append(file)

            if repo_info["primary_readme"] is None:
                repo_info["primary_readme"] = file

        if file.name.lower() == "dockerfile":
            repo_info["has_dockerfile"] = True
        if file.suffix.lower() == ".txt" and "requirements" in file.stem.lower():
            repo_info["has_requirements"] = True
            repo_info["requirements_file"].append(file)
        if file.name.lower() == "pyproject.toml":
            repo_info["has_pyproject"] = True
            repo_info["pyproject_file"].append(file)

        if (file.name.lower() == ".env.example" or file.name.lower() == "example.env" or file.name.lower().endswith(".env.example")):
            repo_info["has_env_example"] = True
            repo_info["env_example_files"].append(file)

        if file.is_file():
            repo_info["total_files"] += 1
        if file.is_file() and file.suffix == ".py":
            repo_info["total_python_files"] += 1
            repo_info["python_files"].append(file)
        if file.is_file() and file.suffix == ".md":
            repo_info["total_markdown_files"] += 1
        if file.is_file() and "env" in file.name.lower():
            repo_info["total_env_files"] += 1
       
    return repo_info