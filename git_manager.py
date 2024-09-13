import os
import subprocess
import sys
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command):
    """Run a shell command and return its output."""
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True, shell=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
        sys.exit(1)

def init_repo():
    """Initialize a new Git repository."""
    run_command("git init")
    logging.info("Git repository initialized.")

def create_gitignore():
    """Create a .gitignore file with common Python ignores."""
    gitignore_content = """
# Python
__pycache__/
*.py[cod]
*.so

# Environments
.env
.venv
env/
venv/
ENV/

# IDEs
.vscode/
.idea/

# Logs
*.log

# OS generated files
.DS_Store
Thumbs.db
"""
    with open(".gitignore", "w") as f:
        f.write(gitignore_content.strip())
    logging.info(".gitignore file created.")

def add_files():
    """Add all files to the Git staging area and log added files."""
    result = run_command("git add .")
    logging.info("All files added to staging area.")
    
    # Log the status after adding files
    status_output = run_command("git status --short")
    if status_output:
        logging.info(f"Files staged for commit:\n{status_output}")
    else:
        logging.info("No files staged for commit.")

def commit_changes(message):
    """Commit changes with the given message."""
    run_command(f'git commit -m "{message}"')
    logging.info(f"Changes committed: {message}")

def create_save_point(name):
    """Create a save point (tag) with the given name."""
    run_command(f"git tag {name}")
    logging.info(f"Save point created: {name}")

def push_to_remote(remote="origin", branch="main"):
    """Push changes and tags to the remote repository."""
    run_command(f"git push {remote} {branch}")
    run_command("git push --tags")
    logging.info(f"Changes and tags pushed to {remote}/{branch}")

def setup_remote(url):
    """Set up a remote repository."""
    run_command(f"git remote add origin {url}")
    logging.info(f"Remote repository set: {url}")

def manage_git_operations(repo_url=None):
    """Manage Git operations for the project."""
    if not os.path.exists(".git"):
        init_repo()
        create_gitignore()
    
    add_files()
    commit_changes("Update project files")
    create_save_point(f"save_point_{int(time.time())}")
    
    if repo_url:
        setup_remote(repo_url)
    
    push_to_remote()

def create_branch(branch_name):
    """Create a new branch and switch to it."""
    run_command(f"git checkout -b {branch_name}")
    logging.info(f"Switched to new branch: {branch_name}")

def switch_branch(branch_name):
    """Switch to an existing branch."""
    run_command(f"git checkout {branch_name}")
    logging.info(f"Switched to branch: {branch_name}")

def view_commit_history():
    """Display the commit history."""
    try:
        history = run_command("git log --oneline")
        logging.info(f"Commit history:\n{history}")
    except Exception as e:
        logging.error(f"Failed to retrieve commit history: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "history":
            view_commit_history()
        else:
            repo_url = sys.argv[1]
            manage_git_operations(repo_url)
    else:
        manage_git_operations()