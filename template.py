import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

Project_name="mlproject"
list_of_files=[
".github/workflows/.gitkeep",
f"src/{Project_name}/__init__.py",
f"src/{Project_name}/components/__init__.py",
f"src/{Project_name}/utils/__init__.py",
f"src/{Project_name}/utils/common.py",
f"src/{Project_name}/config/__init__.py",
f"src/{Project_name}/config/configuration.py",
f"src/{Project_name}/pipeline/__init__.py",
f"src/{Project_name}/entity/__init__.py",
f"src/{Project_name}/entity/config_entity.py",
f"src/{Project_name}/constant/__init__.py",
"config/config.yaml",
"dvc.yaml",
"params.yaml",
"schema.yaml",
"main.py",
"app.py",
"Dockerfile",
"requirements.txt",
"setup.py",
"research/trails.ipynb",
"templates/index.html"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir , filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory;{filedir}for the file:{filename}")
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file:{filepath}")
    else:
        logging.info(f"{filename} id already exists")
