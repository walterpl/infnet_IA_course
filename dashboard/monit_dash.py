import streamlit as st
import numpy as np
import pandas as pd
st.title('Monitoração de Saúde do Melhor Modelo de ML')
st.text('Esse Pagina serve como modelo para monitoração das métricas de um modelo de ML.')
st.text('Dados históricos no momento da criação são inexistentes.')
st.header('Matrix de Confusão')

confusion_matrix = np.array([[8520, 2082],[6161, 3522]])
st.table(confusion_matrix)

class_report = {'0.0': {'precision': 0.5803419385600436,
  'recall': 0.8036219581211093,
  'f1-score': 0.6739706522169046,
  'support': 10602},
 '1.0': {'precision': 0.6284796573875803,
  'recall': 0.3637302488898069,
  'f1-score': 0.4607836724013868,
  'support': 9683},
 'accuracy': 0.593640621148632,
 'macro avg': {'precision': 0.6044107979738119,
  'recall': 0.5836761035054581,
  'f1-score': 0.5673771623091457,
  'support': 20285},
 'weighted avg': {'precision': 0.6033203724474993,
  'recall': 0.593640621148632,
  'f1-score': 0.572206317706002,
  'support': 20285}}

metric_df = pd.DataFrame(class_report).T

st.header('Tabela de Métricas')
st.table(metric_df)


