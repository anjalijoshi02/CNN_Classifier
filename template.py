import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')

package_name="deepClassifier"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",  # let's say you have created any class and you want to specifically test that class , then we use unit tests  
    "tests/integration/__init__.py",  # when you are testing working of the pipeline
    "configs/config.yaml",
    "dvc.yaml",  # dvc=data versioning control file
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini", # used for testing of the project locally
    "research/trials.ipynb",
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for file  {filename} ")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0) :
        with open(filepath,"w") as f:
            pass # create an empty file
            logging.info(f"Creating empty file : {filepath}")
    else:
        logging.info(f"{filename} already exits")
