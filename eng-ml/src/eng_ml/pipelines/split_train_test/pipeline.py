"""
This is a boilerplate pipeline 'split_train_test'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from kedro.config import ConfigLoader
from kedro.framework.project import settings
from .nodes import split_base_train_test

conf_path = str('/Users/walterpereira/projetcs/IA_infnet/eng-ml/' + settings.CONF_SOURCE)
conf_loader = ConfigLoader(conf_source=conf_path, env="local")
parameters = conf_loader["parameters"]

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=split_base_train_test,
             inputs=['data_filtred','params:test_size'],
             outputs=['base_train','base_test'],
             name='split_train_test'
             )
    ])
