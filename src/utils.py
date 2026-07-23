import sys 
import os 
from src.exception import CustomException 
from src.logger import logging
import pickle 

def save_obj(obj,file_path):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        logging.info('Excepion Occured at save object')
        raise CustomException(e,sys)
    
  