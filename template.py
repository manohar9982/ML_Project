import os # ye ganric folder ka path nikal ke data hai
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO) # iska matlab hume ganric information logging ka dtails aayega

project_name="mlproject"

list_of_files=[
    #".github/workflows/.gitkeep",# ye isliye banayege ki deployement ke case me github action likhenge usko humko basicly workflows me likhna pdata hai
     f"src/{project_name}/__init__.py", ## folder ko package banana hai to uske under likenge __init__.py
     f"src/{project_name}/components/__init__.py",
     f"src/{project_name}/components/data_ingestion.py",
     f"src/{project_name}/components/data_tranformation.py",
     f"src/{project_name}/components/model_tranier.py",
     f"src/{project_name}/components/model_monitering.py",
     f"src/{project_name}/pipelines/__init__.py",
     f"src/{project_name}/pipelines/training_pipeline.py",
     f"src/{project_name}/pipelines/prediction_pipeline.py",
     f"src/{project_name}/exception.py",
     f"src/{project_name}/logger.py",
     f"src/{project_name}/utils.py",
     "main.py",
     "app.py",
     "Dockerfile",
     "requirements.txt",
     "setup.py"
     
     
     
]

for filepath in list_of_files:
    filepath = Path(filepath)  # ye jo path variable h apne project ke specific path nikalega
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":  # agr file directory kuch bhi empty nahi mil raha hai
        os.makedirs(filedir,exist_ok=True) #filedir bna dega
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # agr ye file exist nahi kr raha h or uska size bhi 0 h to
        with open(filepath,'w') as f: # file ko open krenge 
            pass # mtlb kuch nahi kr rahe hai
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")
