from pathlib import Path
import subprocess

def clone_repository(url):

    # Extract the repository name from the URL
    repo_name = url.split('/')[-1].replace('.git', '')

    temp_dir = Path('temp')
    temp_dir.mkdir(exist_ok=True)

    repo_path = temp_dir / repo_name

    # Check if the directory already exists
    if repo_path.exists():
        print(f"Repository already cloned.")
        return repo_path

    # Clone the repository using git
    try:
        subprocess.run(['git', 'clone', url, str(repo_path)], check=True, capture_output=True, text=True)
        print(f"Successfully cloned the repository '{repo_path}'.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone the repository.\nError: {e.stderr}")
        return None

    return repo_path