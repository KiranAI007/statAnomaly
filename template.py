'''
    we need this template file to create the project structure.
'''

# import the libraries
import os
from pathlib import Path
import logging

# create the logging structure
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# give my project name
project_name = 'anomalyDetection'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
]

