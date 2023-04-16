"""
This is a boilerplate pipeline 'Treinamento'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train_lr_model, train_best_ml_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=train_lr_model,
             inputs=['base_train','base_test'],
             outputs='lr_model',
             name='train_lr_model'
             ),
        node(func=train_best_ml_model,
             inputs=['base_train', 'base_test'],
             outputs='best_model',
             name='train_best_ml_model'
             )

    ])
