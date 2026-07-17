import os
from dotenv import load_dotenv
import requests
import asyncio
import httpx
from claim import get_claims

load_dotenv()

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

url = "https://www.cnn.com/2026/07/15/health/cyclosporiasis-parasite-food-safe-avoid"

def get_fact_check(query: str) -> dict:
    response = requests.get("https://factchecktools.googleapis.com/v1alpha1/claims:search",
                            params={"query": query, "key": GOOGLE_API_KEY})
    
    response.raise_for_status()
    return response.json()

def get_all_fact_checks(claims: list[str]) -> list[dict]:
    results = []

    for claim in claims:
        try:
            result = get_fact_check(claim)
        except requests.HTTPError:
            result = None

        results.append({"claim": claim, "result": result})
    
    return results

claims = get_claims(url)

claims_with_results = get_all_fact_checks(claims)