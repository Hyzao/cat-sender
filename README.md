# A new cat every day
I want a cat

My parents don't

We gonna make them like cats by sending them one picture of cat every day

# What it does
Get the most upvoted image on the r/cats subreddit and send it to my parents group chat on messenger

Feel free to use it, but read the disclaimer first
# Setup

Needed : python3.6

All needed python modules are installed by setup.sh - run it with root

An important modification i had to use was provided in this [closed issue](https://github.com/fbchat-dev/fbchat/issues/615#issuecomment-710673863)

Modification is the last part of the setup.sh script, i was too lazy to use a regex to change one line so i uploaded the changed file directly

The path is hard coded, if you want to re-use with an other python version, you will need to change it

# Env variables

PRAW - Reddit scrapper

Create praw.ini using the praw.ini.example file and follow NotYourGuy excellent tutorial in his pre-requisites [here](https://github.com/NotYourGuy/scraperr#pre-requisites)

Fill the credentials [this way](https://www.storybench.org/how-to-scrape-reddit-with-python/)

FBCHAT - messenger client in python

Find the thread id of the group you want to send the cat picture too - on computer, click on a messenger conversion and find the id in the URL

Get your Facebook credentials

For app monitoring, create a slack_app and get the slack_hook for your dedicated monitoring channel

Create .env using the .env.example and fill al thoses secrets

# Daily script

Just add a cronjob for main.py and watch your parents go nuts on day 3 of "Daily cat"

# Acknowledgements

This project is based on a reddit scrapper made by [Lucian Vasile](https://github.com/NotYourGuy)

Github repository : https://github.com/NotYourGuy/scraperr

This project is also based on fbchat : https://github.com/fbchat-dev/fbchat

# Disclaimer

I am NOT responsible for any unlawful or hijacked use of this script

This project is purely made for fun and shall be used only for personnal matters
