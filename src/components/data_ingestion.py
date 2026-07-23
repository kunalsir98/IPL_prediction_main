import sys,os 
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split

class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df=pd.read_csv(os.path.join('notebook/final_data.csv'))
            logging.info('Data Frame Readen as Pandas DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            train_set,test_set=train_test_split(df,test_size=0.32,random_state=42)
            logging.info('Train Test Split Done Correctly')

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info('Exception Occured at Data Ingestion Stage')
            raise CustomException(e,sys)

if __name__ == '__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()