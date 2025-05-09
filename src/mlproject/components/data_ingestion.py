#database ---> data read ---->train test split

# mysql  --> traintest split-->dataset
import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from src.mlproject.utils import red_sql_data
from dataclasses import dataclass #iska use jo jo hume input parameter dena h vo sare ya initialize kr denge
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifact','train.csv')
    test_data_path:str=os.path.join('artifact','test.csv')
    raw_data_path:str=os.path.join('artifact','raw.csv')
    # ye sb save artifact folder  vaha save hoga
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # means isme tino path aa jayenge
        
    def initiate_data_ingestion(self):
        try:
            ##reading the data from mysql
            df=red_sql_data()
            logging.info("reading completed mysql database")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) # folder banega 
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) # 
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            df.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info('Data ingestion is completed')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)
        
            