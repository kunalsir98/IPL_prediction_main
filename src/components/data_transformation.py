import sys 
import  os 
from src.exception import CustomException 
from src.logger import logging 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder
from sklearn.pipeline import Pipeline 
from sklearn.compose import ColumnTransformer 
from dataclasses import dataclass 
import pandas as pd 
from src.utils import save_obj


@dataclass 
class DataTransformationConfig:
    preprocessor_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransFormation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_transformation_obj(self):
        logging.info('starting get data transformation')

        try:

            categorical_cols=['city', 'date', 'team1', 'team2', 'toss_winner', 'toss_decision',
        'result', 'player_of_match', 'venue', 'umpire1', 'umpire2']
            numerical_cols=['season', 'dl_applied', 'win_by_runs', 'win_by_wickets']

            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scalar',StandardScaler())

                ]
            )
            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('onehotencoder',OneHotEncoder(handle_unknown='ignore',sparse_output=False)),
                    ('StandardScaler',StandardScaler(with_mean=False))
                
                ]
            )
            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols),
                ('cat_pipeline',cat_pipeline,categorical_cols)
            ])


            logging.info('Get Data Transformation Completed')

            return preprocessor
        
        except Exception as e:
            logging.info('Exception Occured in get data transformation')
            raise CustomException(e,sys)


    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info('Reading As pandas DaataFrame')
            logging.info(f'Readig Top 5 columns of Train Data:{train_df.head().to_string()}')
            logging.info(f'Reading Top 5 Columns of Test Data:{test_df.head().to_string()}')

            logging.info('obtaing get data transformation object')

            preprocessor_obj=self.get_transformation_obj()

            target_column='winner'
            drop_column=[target_column]

            input_feature_train_df=train_df.drop(drop_column,axis=1)
            target_feature_train_df=[target_column]

            input_feature_test_df=test_df.drop(drop_column,axis=1)
            target_feature_test_df=[target_column]

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)

            le=LabelEncoder()

            target_train_arr=le.fit_transform(target_feature_train_df)
            target_test_arr=le.transform(target_feature_test_df)

            save_obj(
                file_path=self.data_transformation_config.preprocessor_file_path,
                obj=preprocessor_obj

            )


            return(
                input_feature_train_arr,
                target_train_arr,
                input_feature_test_arr,
                target_test_arr,
                self.data_transformation_config.preprocessor_file_path

            )
        
        
        except Exception as e:
            logging.info('Error OCccured at datatransformation stage')
            raise CustomException(e,sys)

    

    
        
    

