import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
import pandas as pd

class TrainPipeline:
    def __init__(self):
        pass

    def initiate_training(self):
        try:
            logging.info("Starting the training pipeline")
            
            # Data Ingestion
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
            
            # Data Transformation
            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
            
            # Model Training
            model_trainer = ModelTrainer()
            r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
            
            logging.info(f"Training completed with R2 score: {r2_score}")
            return r2_score
            
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    train_pipeline = TrainPipeline()
    train_pipeline.initiate_training()