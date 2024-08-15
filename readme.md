# Streamlit demo

## Streamlit server

Uses python venv

```bash
source .venv/bin/activate
pip install -r requirements.txt
streamlit run main.py
```

Access the webpage on `http://localhost:8501`.

## mongoDB server

```bash
docker-compose up
```

See file docker-compose.yml for the username and password for this database.
Can connect via mongodb compass with connection string: `mongodb://localhost:27017/`.


## Goals for this project:

- [X] streamlit server
- [X] streamlit multi page
- [X] mongodb server
- [X] mongodb access in streamlit app
- [x] explore mongodb database
- [ ] upload json blob to DB
- [ ] upload csv to DB
- [ ] dockerise the streamlit server
- [X] dockerise the mongodb server
