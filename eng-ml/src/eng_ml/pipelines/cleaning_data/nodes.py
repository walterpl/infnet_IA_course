"""
This is a boilerplate pipeline 'cleaning_data'
generated using Kedro 0.18.7
"""

import pandas as pd
from kedro_mlflow.io.metrics import MlflowMetricDataSet

def clean_and_select_data(df : pd.DataFrame, colums_to_keep : list) -> pd.DataFrame:
    metric_row = MlflowMetricDataSet(key="DF_row_count")
    df.dropna(inplace=True)
    df = df[df.shot_type == '2PT Field Goal']
    df = df[colums_to_keep]
    metric_row.save(float(df.shape[0]))
    metric_columns = MlflowMetricDataSet(key="DF_columns_count")
    metric_columns.save(float(df.shape[1]))
    return df

