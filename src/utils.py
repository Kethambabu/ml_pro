import os
import sys
import dill  # dill is used for serializing Python objects
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from src.exception import CustomException
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    from sklearn.metrics import r2_score

def evaluate_models(x_train, y_train, x_test, y_test, models,params):
    from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import sys
from src.exception import CustomException
import logging

def evaluate_models(x_train, y_train, x_test, y_test, models, param):
    try:
        report = {}
        best_model = None
        best_score = -1
        best_model_name = None

        for model_name in models:
            model = models[model_name]
            params = param.get(model_name, {})

            logging.info(f"Evaluating model: {model_name}")

            gs = GridSearchCV(model, params, cv=3, n_jobs=-1, verbose=0)
            gs.fit(x_train, y_train)

            best_model_candidate = gs.best_estimator_
            y_test_pred = best_model_candidate.predict(x_test)

            test_model_score = r2_score(y_test, y_test_pred)
            report[model_name] = test_model_score

            if test_model_score > best_score:
                best_score = test_model_score
                best_model = best_model_candidate
                best_model_name = model_name

        return report, best_model_name, best_model

    except Exception as e:
        raise CustomException(e, sys)
