import os
from dotenv import load_dotenv
import requests
import asyncio
import httpx

load_dotenv()

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

def get_fact_check(query: str) -> dict:
    response = requests.get("https://factchecktools.googleapis.com/v1alpha1/claims:search",
                            params={"query": query, "key": GOOGLE_API_KEY})
    
    response.raise_for_status()
    return response.json()