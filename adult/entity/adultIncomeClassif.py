import os
import sys

from adult.exception import AdultException
from adult.util.util import load_object

import pandas as pd


class adultData:

    def __init__(self,
                 age: int,
                 workclass: float,
                 fnlwgt: float,
                 education: str,
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
            self.age = age
            self.workclass = workclass
            self.fnlwgt = fnlwgt
            self.education = education
            self.education-num = education-num
            self.marital-status = marital-status
            self.occupation = occupation
            self.relationship = relationship
            self.race = race
            self.sex = sex
            self.capital-gain = capital-gain
            self.capital-loss = capital-loss
            self.hours-per-week = hours-per-week
            self.country = country
        except Exception as e:
            raise AdultException(e, sys) from e

    def get_adult_input_data_frame(self):

        try:
            adult_input_dict = self.get_adult_data_as_dict()
            return pd.DataFrame(adult_input_dict)
        except Exception as e:
            raise AdultException(e, sys) from e

    def get_adult_data_as_dict(self):
        try:
            input_data = {
                "age": [self.age],
                "workclass": [self.workclass],
                "fnlwgt": [self.fnlwgt],
                "education": [self.education],
                "education-num": [self.education-num],
                "marital-status": [self.marital-status],
                "occupation": [self.occupation],
                "relationship": [self.relationship],
                "race": [self.race],
                "sex": [self.sex],
                "capital-gain": [self.capital-gain],
                "capital-loss": [self.capital-loss],
                "hours-per-week": [self.hours-per-week],
                "country": [self.country]}
            return input_data
        except Exception as e:
            raise AdultException(e, sys)


class adultClassifier:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise AdultException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise AdultException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            Incomevalue = model.predict(X)
            return Incomevalue
        except Exception as e:
            raise AdultException(e, sys) from e