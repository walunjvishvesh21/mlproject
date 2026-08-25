import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformationConfig, DataTransformataion
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer


'''
data_ingestion.py file ka main kaam poori ML pipeline ko start karna hai — sabse pehle DataIngestionConfig mein raw, train aur test files ke paths define hote hain, phir DataIngestion class stud.csv dataset ko read karke artifacts folder mein raw data save karti hai aur dataset ko 80% training aur 20% testing mein divide karke train.csv aur test.csv save karti hai; uske baad wahi train/test data DataTransformataion ko diya jata hai jahan data ko ML model ke layak transform kiya jata hai, aur finally transformed data ModelTrainer ko diya jata hai jahan ML models train hote hain, unke performance compare hote hain aur best model/result generate hota hai. 
Simple words mein: data_ingestion.py = data read karo → train/test mein divide karo → data transform karo → model train karo → result do.


'''



@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('ENTERED THE DATA INGESTION')

        try:
            df = pd.read_csv('notebook\\data\\stud.csv')
            logging.info('READ THE DATASET AS DATAFRAME')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("TRAIN TEST SPLIT INITIALIZED")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("INGESTION OF THE DATA IS COMPLETED")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformataion()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))