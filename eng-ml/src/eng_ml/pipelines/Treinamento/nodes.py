"""
This is a boilerplate pipeline 'Treinamento'
generated using Kedro 0.18.7
"""

from sklearn.metrics import log_loss
from pycaret.classification import ClassificationExperiment
import pandas as pd


def train_lr_model(train_df: pd.DataFrame, test_df: pd.DataFrame):
    full_df = pd.concat([train_df, test_df])
    auto_ia = ClassificationExperiment()
    auto_ia.setup(full_df, target='shot_made_flag', log_experiment='mlflow', experiment_name='treino_lr')
    auto_ia.add_metric('logloss', 'Log Loss', log_loss, greater_is_better = False)
    lr_model = auto_ia.create_model('lr')
    return lr_model


def train_best_ml_model(train_df: pd.DataFrame, test_df: pd.DataFrame):
    full_df = pd.concat([train_df, test_df])
    auto_ia = ClassificationExperiment()
    auto_ia.setup(full_df, target='shot_made_flag', log_experiment='mlflow', experiment_name='treino_best_model')
    auto_ia.add_metric('logloss', 'Log Loss', log_loss, greater_is_better=False)
    best_model = auto_ia.compare_models()
    even_better_model = auto_ia.tune_model(best_model)
    return even_better_model
