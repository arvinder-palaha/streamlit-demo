import streamlit as st
import pymongo
from src.functions import find_documents_from_collection
import json

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(host="localhost", **st.secrets["mongo"])

client = init_connection()

db_choice = st.text_input("choose a database")
col_choice = st.text_input("choose a collection")
query_filter = st.text_input('{ "<field to match>" : "<value to match>" }')
query_filter = json.loads(query_filter)

if all([db_choice, col_choice, query_filter]):
    # show entries that match:
    collection = client[db_choice][col_choice]
    documents = find_documents_from_collection(collection, query_filter)
    st.write(documents)
    if len(documents) and st.button("delete?"):
        collection.delete_one(query_filter)