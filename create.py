import argparse
import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN =os.getenv("GITHUB_TOKEN")

# TODO: creating the .env file and storing the github access token in there

# TODO: Megha =>  creating the argparse command line modules and creating the command for private/public repo define at the time of create.


REPO_PATH = " "
GITHUB_USER = ' '
GITHUB_URL = "https://api.github.com"


headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.v3+json"
}