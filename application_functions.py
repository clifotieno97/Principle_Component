from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px

def pca_maker(data_import):

    numerical_columns_list = []
    categorical_columns_list = []

    for i in data_import.columns:
        if data_import[i].dtype == np.dtype("float64") or data_import[i].dtype== np.dtype("int64"):
            numerical_columns_list.append(data_import[i])
        else:
            categorical_columns_list.append(data_import[i])


    numerical_data = pd.concat(numerical_columns_list, axis= 1)
    categorical_data = pd.concat(categorical_columns_list, axis= 1)

    numerical_data = numerical_data.apply(lambda x: x.fillna(np.mean(x)))

    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(numerical_data)

    pca = PCA()
    pca_data = pca.fit_transform(scaled_values)
    pca_data = pd.DataFrame(pca_data)
    
    new_column_names = ["PCA_"+ str(i) for i in range (1, len(pca_data.columns)+1)]
    

    column_mapper = dict(zip(list(pca_data.columns),new_column_names))
   
    pca_data.rename(columns=column_mapper, inplace= True)

    output = pd.concat([data_import,pca_data], axis=1)

    return output, categorical_data.columns, new_column_names
