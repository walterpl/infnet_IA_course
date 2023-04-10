"""
This is a boilerplate pipeline 'cleaning_data'
generated using Kedro 0.18.7
"""
from kedro.config import ConfigLoader
from kedro.framework.project import settings
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import clean_and_select_data

conf_path = str('/Users/walterpereira/projetcs/IA_infnet/eng-ml/' + settings.CONF_SOURCE)
conf_loader = ConfigLoader(conf_source=conf_path, env="local")
parameters = conf_loader["parameters"]

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(func=clean_and_select_data,
             inputs=['raw_data','params:list_of_columns_to_select'],
             outputs='data_filtred',
             name='data_cleaner'
             )
    ])
