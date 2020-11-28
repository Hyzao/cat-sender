import logging
import fbchat
from fbchat import Client
from fbchat.models import *
import os
from dotenv import load_dotenv
import pathlib

# Get the path
path = str(pathlib.Path(__file__).parent.absolute())
picture_folder= path +"/reddit/"
pic_name= os.listdir(picture_folder)[0]
image_path = picture_folder + pic_name

logging.basicConfig(level=logging.DEBUG)

# Load env variables
load_dotenv()

# FB Connexion parameters
FB_USER=os.getenv('FB_USER')
FB_PASS=os.getenv('FB_PASS')

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
client = fbchat.Client(FB_USER,FB_PASS, user_agent=user_agent)

# Chat Parameters
THREAD_ID = os.getenv('THREAD_ID')
thread_type = ThreadType.GROUP

# Send cat picture to group chat
client.sendLocalImage(image_path,
    message=Message(text="Voici le chat du jour - by Ian"),
    thread_id=THREAD_ID,
    thread_type=thread_type,
)

# Remove the picture (we dont want to store one pic a day)
os.remove(image_path)

cookies = client.getSession()
