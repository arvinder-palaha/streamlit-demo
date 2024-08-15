import streamlit as st
import pandas as pd
import numpy as np
import pymongo
import ast

from src.functions import parse_db_inspect_input, find_documents_from_collection

st.title('Uber picks up in nyc')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)


# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()

input = st.text_input("Inspect database with comma separated keys:")

st.write(input)
st.write(len(input))
input_keys = parse_db_inspect_input(input)
num_input_keys = len(input_keys)

if num_input_keys==0:
    st.write(client.list_database_names())
if num_input_keys==1:
    st.write(client[input_keys[0]].list_collection_names())
if num_input_keys==2:
    collection = client[input_keys[0]][input_keys[1]]
    documents = find_documents_from_collection(collection)
    st.write(documents)
if num_input_keys==3:
    collection = client[input_keys[0]][input_keys[1]]
    search_key = ast.literal_eval(input_keys[2])
    documents = find_documents_from_collection(collection, search_key)
    st.write(documents)    
