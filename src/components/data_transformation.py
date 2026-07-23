import sys 
import os 
from src.exception import CustomException
from src.logger import logging
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from dataclasses import dataclass

@dataclass
class DataTransFormationConfig:
    prepeocessor_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransFormation:
    def __init__(self):
        self.data_transformation_config=DataTransFormationConfig()

    def get_data_transformation_obj(self):
        