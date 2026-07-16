from fastapi import FastAPI
from factcheck import get_fact_check

app = FastAPI()

@app.get("factchecktools.googleapis.com")
def get_fact_check():
    return get_fact_check