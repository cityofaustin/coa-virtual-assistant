import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import json

from datetime import datetime


load_dotenv()

API_KEY = os.getenv("API_KEY")
# get it from watson, set in your .env file
auth = HTTPBasicAuth('apikey', API_KEY)

# URL = "https://api.us-south.assistant.watson.cloud.ibm.com/instances/c82fa351-bf33-4f9a-a315-c8473ed4a7fc/"
workspace_id = "45bdc579-811f-46a1-83af-0c80b8f81d18"
URL = "https://gateway.watsonplatform.net/assistant/api/v1/workspaces/" + workspace_id
# see https://cloud.ibm.com/apidocs/assistant/assistant-v1#versioning
version = "2020-04-01"


def export_skill(**args):

    response = requests.get(URL, params={
        'version': version,
        'export': 'true',
        'sort': 'stable'

    }, auth=auth)
    return response.json()


skill = export_skill()

with open(f"./exports/{datetime.today().strftime('%m-%d-%Y')}_{workspace_id}.json", 'w') as file:
    json.dump(skill, file, indent=4)
