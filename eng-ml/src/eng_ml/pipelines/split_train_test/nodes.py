"""
This is a boilerplate pipeline 'split_train_test'
generated using Kedro 0.18.7
"""

from sklearn.model_selection import train_test_split
from kedro_mlflow.io.metrics import MlflowMetricDataSet
import pandas as pd


def split_base_train_test(df : pd.DataFrame, test_size: float) -> (pd.DataFrame, pd.DataFrame):
    metric_test_rows = MlflowMetricDataSet(key="test_df_rows_count")
    metric_test_columns = MlflowMetricDataSet(key='test_df_columns_count')
    metric_train_rows = MlflowMetricDataSet(key="train_df_rows_count")
    metric_train_columns = MlflowMetricDataSet(key="train_df_columns_count")
    train_df, test_df = train_test_split(df, test_size=test_size)
    metric_test_rows.save(test_df.shape[0])
    metric_test_columns.save(test_df.shape[1])
    metric_train_rows.save(train_df.shape[0])
    metric_train_columns.save(train_df.shape[1])
    return train_df, test_df

