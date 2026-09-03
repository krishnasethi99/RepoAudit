from fetchers.github_fetcher import clone_repository
from scanners.repository_scanner import scan_repository

url = input("Enter GitHub Repository URL: ")

repo_path = clone_repository(url)

if repo_path:
    print(f"Repository Path: {repo_path}")
if repo_path is None:
    print("Repository analysis aborted.")
#     exit()

repo_info = scan_repository(repo_path)
print("\nRepository Scan Results:")
print(f"README Found: {repo_info['has_readme']}")
print(f"Dockerfile Found: {repo_info['has_dockerfile']}")
print(f"Requirements Found: {repo_info['has_requirements']}")
print(f"PyProject Found: {repo_info['has_pyproject']}")
print(f"Env Example Found: {repo_info['has_env_example']}")
print("\nRepository Scan Summary:")
print(f"Total Python Files: {repo_info['total_python_files']}")
print(f"Total Files: {repo_info['total_files']}")
print(f"Markdown Files: {repo_info['total_markdown_files']}")
print(f"Environment Files: {repo_info['total_env_files']}")