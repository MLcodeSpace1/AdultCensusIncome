import os
import sys

from adult.exception import adultException
from adult.util.util import load_object

import pandas as pd


class adultData:

    def __init__(self,
                 age: int,
                 workclass: float,
                 fnlwgt: float,
                 education: float,
                 education-num: int,
                 marital-status: str,
                 occupation: str,
                 relationship: str,
                 race: str,
                 sex: str,
                 capital-gain: int,
                 capital-loss: int,
                 hours-per-week: int,
                 country:str
                 ):
        try:
            self.longitude = longitude
            self.latitude = latitude
            self.adult_median_age = adult_median_age
            self.total_rooms = total_rooms
            self.total_bedrooms = total_bedrooms
            self.population = population
            self.households = households
            self.median_income = median_income
            self.ocean_proximity = ocean_proximity
            self.median_house_value = median_house_value
        except Exception as e:
            raise adultException(e, sys) from e

    def get_adult_input_data_frame(self):

        try:
            adult_input_dict = self.get_adult_data_as_dict()
            return pd.DataFrame(adult_input_dict)
        except Exception as e:
            raise adultException(e, sys) from e

    def get_adult_data_as_dict(self):
        try:
            input_data = {
                "longitude": [self.longitude],
                "latitude": [self.latitude],
                "adult_median_age": [self.adult_median_age],
                "total_rooms": [self.total_rooms],
                "total_bedrooms": [self.total_bedrooms],
                "population": [self.population],
                "households": [self.households],
                "median_income": [self.median_income],
                "ocean_proximity": [self.ocean_proximity]}
            return input_data
        except Exception as e:
            raise adultException(e, sys)


class adultPredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise adultException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise adultException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            median_house_value = model.predict(X)
            return median_house_value
        except Exception as e:
            raise adultException(e, sys) from e