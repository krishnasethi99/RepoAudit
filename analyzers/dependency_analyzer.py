import tomllib
import sys

def dependency_analyzer(repo_info, ast_info):
    dependencies = {
        "missing_dependencies": [],
        "unused_dependencies": [],
        "declared_dependencies": [],
        "imported_dependencies": [],
    }
    IGNORED_IMPORTS = {
        imp.lower().replace("-", "_")
        for imp in {
            "_typeshed",
            "typing_extensions",
            "pytest",
        }
    }
    PACKAGE_ALIASES = {
        "pil": "pillow",
        "yaml": "pyyaml",
        "dateutil": "python-dateutil",
        "dotenv": "python-dotenv",
        "sklearn": "scikit-learn",
        "bs4": "beautifulsoup4",
        "cv2": "opencv-python",
    }

    STANDARD_LIBS = set(sys.stdlib_module_names)
    local_modules = {
        file.stem.lower()
        for file in repo_info["python_files"]
    }
    package_dirs = {
        file.parent.name.lower()
        for file in repo_info["python_files"]
        if file.name == "__init__.py"
    }
    local_modules = {
        module.lower().replace("-", "_")
        for module in (local_modules | package_dirs)
    }

    imports = set()

    for imp in ast_info.get("imports", []):
        module_name = imp.split(".")[0].lower()

        module_name = PACKAGE_ALIASES.get(module_name, module_name)
        imports.add(module_name)

    requirements_file = repo_info.get("requirements_file", [])
    pyproject_file = repo_info.get("pyproject_file", [])

    for req_file in requirements_file:
        try:
            with open(req_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        dependencies["declared_dependencies"].append(line.split("==")[0].split(">=")[0].split("<=")[0].split(">")[0].split("<")[0].strip().split("~=")[0])
        except Exception as e:
            print(f"Error reading requirements file {req_file}: {e}")

    for pyproject in pyproject_file:
        try:
            with open(pyproject, "rb") as f:
                pyproject_data = tomllib.load(f)

                # Poetry style
                poetry_deps = (pyproject_data.get("tool", {}).get("poetry", {}).get("dependencies", {}))

                for dep in poetry_deps:
                    if dep != "python":
                        dependencies["declared_dependencies"].append(dep)

                # Modern PEP 621 style
                project_deps = (
                    pyproject_data.get("project", {}).get("dependencies", []))

                for dep in project_deps:
                    dep_name = (
                        dep.split("==")[0]
                        .split(">=")[0]
                        .split("<=")[0]
                        .split(">")[0]
                        .split("<")[0]
                        .split("~=")[0]
                        .strip()
                    )
                    dependencies["declared_dependencies"].append(
                        dep_name
                    )
        except Exception as e:
            print(f"Error reading pyproject file {pyproject}: {e}")

    declared = set(dependencies["declared_dependencies"])
    declared = {dep.lower().replace("-", "_") for dep in declared}

    dependencies["imported_dependencies"] = list(imports)
    imported = set(dependencies["imported_dependencies"])
    imported = {dep.lower().replace("-", "_") for dep in imported}
    imported = imported - STANDARD_LIBS -  IGNORED_IMPORTS - local_modules

    missing = imported - declared
    unused = declared - imported
    dependencies["missing_dependencies"] = list(missing)
    dependencies["unused_dependencies"] = list(unused)

    dependencies["declared_dependencies"] = sorted(declared)
    dependencies["imported_dependencies"] = sorted(imported)
    dependencies["missing_dependencies"] = sorted(missing)
    dependencies["unused_dependencies"] = sorted(unused)

    return dependencies