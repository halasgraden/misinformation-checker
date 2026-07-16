import os
from dotenv import load_dotenv
import requests

load_dotenv()

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

def get_fact_check():
    ...