import ast

def python_ast_scanner(python_files):

    ast_info = {
    "imports": set(),
    "env_vars": set(),
    "entrypoints": set(),
    "scan_errors": [],
    }

    if not python_files:
        print("No Python files found.")
        return ast_info

    for file in python_files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                source = f.read()
                tree = ast.parse(source, filename=str(file))
                # Perform AST analysis on the parsed tree
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            ast_info["imports"].add(alias.name.split('.')[0])  # Get the top-level module name
                    elif isinstance(node, ast.ImportFrom):
                        module = node.module
                        if module:
                            ast_info["imports"].add(module.split(".")[0])
                    elif isinstance(node, ast.Assign):
                        if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Attribute):
                            if (
                                node.value.args
                                and isinstance(node.value.args[0], ast.Constant)
                                and isinstance(node.value.func.value, ast.Name)
                                and node.value.func.value.id == "os"
                                and node.value.func.attr == "getenv"
                            ):
                                ast_info["env_vars"].add(node.value.args[0].value)
                        elif isinstance(node.value, ast.Subscript):
                            if (
                                isinstance(node.value.value, ast.Attribute)
                                and isinstance(node.value.value.value, ast.Name)
                                and node.value.value.value.id == "os"
                                and node.value.value.attr == "environ"
                                and isinstance(node.value.slice, ast.Constant)
                            ):
                                ast_info["env_vars"].add(node.value.slice.value)

                    elif isinstance(node, ast.If):
                        if (
                            isinstance(node.test, ast.Compare)
                            and isinstance(node.test.left, ast.Name)
                            and node.test.left.id == "__name__"
                            and len(node.test.comparators) == 1
                            and isinstance(node.test.comparators[0], ast.Constant)
                            and node.test.comparators[0].value == "__main__"
                        ):
                            ast_info["entrypoints"].add(str(file))

        except SyntaxError as e:
            ast_info["scan_errors"].append(
                f"{file}: {e}"
            )
            continue
        except UnicodeDecodeError as e:
            ast_info["scan_errors"].append(
                f"{file}: {e}"
            )
            continue
        except Exception as e:
            ast_info["scan_errors"].append(
                f"{file}: {e}"
            )
            continue


    ast_info["imports"] = sorted(ast_info["imports"])
    ast_info["env_vars"] = sorted(ast_info["env_vars"])
    ast_info["entrypoints"] = sorted(ast_info["entrypoints"])

    return ast_info