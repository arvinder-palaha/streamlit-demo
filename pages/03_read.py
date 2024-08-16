import streamlit as st
import pymongo
import ast
from src.functions import find_documents_from_collection, parse_db_inspect_input

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()

input = st.text_input("Inspect database with comma separated keys:")

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
