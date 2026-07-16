from src.logger import logging 
from src.exception import CustomException
from dataclasses import dataclass
import pandas as pd 
import sys
import os
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_paths:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            df=pd.read_clipboard(os.path.join('notebook/final_data.csv'))
            logging.info('reading data as panda as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_paths),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_paths,index=False)

            train_set,test_set=train_test_split(df,test_size=0.32)

            logging.info('initiated train test split')


            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Data igestion is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info('Exception occured at data ingestion stage')
            raise CustomException(e,sys)

if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
