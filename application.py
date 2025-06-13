import pandas as pd
import streamlit as st
import plotly.express as px
from application_functions import pca_maker

st.set_page_config(layout="wide")
scatter_column , settings_column = st.columns((4,1))

scatter_column.title("Multi-Dimensional Analysis")

settings_column.title("Settings")

uploaded_file = settings_column.file_uploader("Choose File")

if uploaded_file is not None:
    data_import = pd.read_csv(uploaded_file)
    pca_data, cat_cols, pca_col = pca_maker(data_import)
    categorical_var =settings_column.selectbox(label="select variable", options=cat_cols)
    categorical_var_2 =settings_column.selectbox(label="Select hover variable", options=cat_cols)
    pca_1 = settings_column.selectbox(label ="First principle component", options = pca_col, index=0)
    pca_col.remove(pca_1)
    pca_2 = settings_column.selectbox(label ="Second principle component", options = pca_col)
    
    scatter_column.plotly_chart(px.scatter(data_frame = pca_data, x = pca_1, y = pca_2, color = categorical_var,
                                            title="PCA Scatter Matrix",hover_data =[categorical_var_2]),
                                            use_container_width=True)
else:
    scatter_column.header("Please choose a file to upload")
