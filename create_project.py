import os
import sys
import logging
import git_manager

# Configure logging
logging.basicConfig(level=logging.INFO)

DIRECTORIES = [
    'src',
    'tests',
    'docs',
    'data',
    'config'
]

FILES = [
    'README.md',
    'requirements.txt',
    '.gitignore',
    'src/__init__.py',
    'src/main.py',
    'tests/__init__.py',
    'tests/test_main.py',
    'config/settings.py'
]

def create_project_structure(project_name):
    """Create a project structure with specified directories and files.

    Args:
        project_name (str): The name of the project directory to create.
    """
    try:
        # Main project directory
        os.makedirs(project_name, exist_ok=True)
        logging.info(f"Created main project directory: {project_name}")

        # Subdirectories
        for directory in DIRECTORIES:
            os.makedirs(os.path.join(project_name, directory), exist_ok=True)
            logging.info(f"Created directory: {directory}")

        # Create empty files
        for file in FILES:
            with open(os.path.join(project_name, file), 'w') as f:
                f.write('')  # Create an empty file
            logging.info(f"Created file: {file}")

        # Add Git management
        os.chdir(project_name)
        git_manager.manage_git_operations()

        logging.info(f"Project '{project_name}' structure created and Git initialized!")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_project.py <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    create_project_structure(project_name)