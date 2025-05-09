import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging

import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()
# ye genric fanction ke liye

host=os.getenv("host")
user=os.getenv("user")
passw=os.getenv("password")
db=os.getenv("db")


def red_sql_data():
    logging.info("reading sql database started")
    try:
        mydb=pymysql.connect(
            
            host=host,
            user=user,
            password=passw,
            db=db
            
            
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from student',mydb)
        print(df.head())
        
        return df
        
        
    except Exception as ex:
        raise CustomException(ex)
    