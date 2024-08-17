import streamlit as st
import pymongo
import json


# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(host="localhost", **st.secrets["mongo"])

client = init_connection()

# select database to insert into
db_choice = st.text_input("choose a database")
# check database exists

# select collection to insert into
col_choice = st.text_input("choose a collection")
# check collection exists

# input some data
input = st.text_area(label="input json")
st.write(f"input is {len(input)} characters")

valid_filled_json_object = False

# check its valid
try:
    input_json = json.loads(input)
    if len(input_json):
        valid_filled_json_object = True
except json.decoder.JSONDecodeError:
    valid_filled_json_object = False

# write it to database
if valid_filled_json_object:
    st.write("looks liek we got us some json!")
    if st.button("write to database"):
        database = client[db_choice]
        col = database[col_choice]
        result = col.insert_one(input_json)
        st.write(result)
else:
    st.write("Either invalid or empty json")