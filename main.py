#!/usr/bin/env python3

import pathlib
import subprocess
import requests
import os
from dotenv import load_dotenv
load_dotenv()

SLACK_HOOK=os.getenv('SLACK_HOOK')

path = pathlib.Path(__file__).parent.absolute()
# Or
# path2 = pathlib.Path().absolute()

subprocess.call(['python3', 'scrapper.py', '-l', '1', '-p', 'day', '-d', path, 'cats'])

subprocess.call(['python3', 'send-cat-image-to-fb.py'])

headers = {
	'Content-type': 'application/json',
}

data = '{"text":"Todays cat was sent"}'

response = requests.post(SLACK_HOOK, headers=headers, data=data)
