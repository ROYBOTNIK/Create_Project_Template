# Project Creation and Git Management Scripts

This repository contains two Python scripts that work together to create a new project structure and manage Git operations:

1. `create_project.py`: Creates a new project structure with predefined directories and files.
2. `git_manager.py`: Manages Git operations for the project.

## Prerequisites

- Python 3.6 or higher
- Git installed and configured on your system

## Installation

1. Clone this repository or download the scripts:
   - `create_project.py`
   - `git_manager.py`

2. Place both scripts in the same directory where you want to create your new projects.

## Usage

### Creating a New Project

To create a new project with the predefined structure and initialize Git:

This will:
- Create a new directory with the given project name
- Set up the project structure (directories and files)
- Initialize a Git repository
- Create a .gitignore file
- Make an initial commit
- Create a save point (Git tag)

### Managing Git Operations

The `git_manager.py` script can be used independently for Git operations:

1. To initialize Git and push to a remote repository:
   ```
   python git_manager.py <remote_repo_url>
   ```

2. To make a commit with a custom message:
   ```
   python git_manager.py "Your commit message here"
   ```

3. To perform local Git operations without pushing:
   ```
   python git_manager.py
   ```

## Script Details

### create_project.py

This script:
- Creates a project directory with the given name
- Sets up predefined subdirectories (src, tests, docs, data, config)
- Creates initial empty files (README.md, requirements.txt, .gitignore, etc.)
- Calls `git_manager.py` to initialize Git for the new project

### git_manager.py

This script provides functions for:
- Initializing a Git repository
- Creating a .gitignore file
- Adding files to staging
- Committing changes
- Creating save points (tags)
- Setting up a remote repository
- Pushing changes to a remote repository
- Creating and switching branches

## Customization

- Modify the `DIRECTORIES` and `FILES` lists in `create_project.py` to change the project structure.
- Edit the `gitignore_content` in `git_manager.py` to customize the .gitignore file.

## Notes

- The scripts use logging to provide information about the operations being performed.
- Error handling is implemented to catch and report issues during execution.
- Make sure you have the necessary permissions to create directories and files in the location where you run these scripts.

## Contributing

Feel free to fork this repository and submit pull requests to enhance the functionality of these scripts.

## License

[Specify your license here]