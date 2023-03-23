import pandas as pd
import streamlit as st

pip install openpyxl
conda install openpyxl

column_names = ['id_soma','lastName','firstName','town','profil','dispo','statut','numberOfResumes','diplome','commentaire','lien_CV','experience']


df = pd.read_excel('Staffing.xlsx',header=1, skiprows= 7,index_col=0)

st.header('Staffing')
st.dataframe(data=df)
