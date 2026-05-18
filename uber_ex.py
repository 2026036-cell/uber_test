import streamlit as st
import pandas as pd
import numpy as np

st.title("uber pickups in New york city")

DATE_COLUMN="date/time"

DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data=pd.read_csv(DATA_URL,nrows=nrows)
    lowercase=lambda x: str(x). lower()
    data.rename(lowercase, axcis="columns",  inplace=True)
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return data
 
data_load_state=st.text("loading Data...")
data=load_data(10000)
data_load_state.text("Loading Data...Done!")


st.subheader("raw Data")
st.write(data)