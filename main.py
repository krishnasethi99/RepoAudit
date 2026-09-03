from fetchers.github_fetcher import clone_repository

url = input("Enter GitHub Repository URL: ")

repo_path = clone_repository(url)

if repo_path:
    print(f"Repository Path: {repo_path}")
if repo_path is None:
    print("Repository analysis aborted.")
    exit()