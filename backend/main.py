from fastapi import FastAPI

app = FastAPI()

@app.get("factchecktools.googleapis.com")
def get_fact_check():
    