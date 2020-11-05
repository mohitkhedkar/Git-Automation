import argparse
import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN =os.getenv("GITHUB_TOKEN")

# TODO: creating the .env file and storing the github access token in there

parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private", "-p", dest="is_private", action="store_true")
args = parser.parse_args()
repo_name = args.name
is_private = args.is_private

REPO_PATH = "E:\Git"
GITHUB_USER = 'meghapal02'
GITHUB_URL = "https://api.github.com"

if is_private:
    payload = '{"name": "' + repo_name + '", "private": true }'
else:
    payload = '{"name": "' + repo_name + '", "private": false }'

headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.v3+json"
}

# TODO: Niraj -> Create a local repo commands and initialize first commit 