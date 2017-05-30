"""Construct messages to be sent as tweet text"""

# Allows using time related functions
from datetime import datetime
# convert times according to time zones
from pytz import timezone

def reply(tweet):
    """Return text to be used as a reply"""
    message = tweet['text']
    user = tweet['user']['screen_name']
    if "Which Pokemon is #1" in message:
        return "Bulbasaur"
    if "Which Pokemon is #2" in message:
        return "Ivysaur"
    if "1999+1" in message:
        return "2000"
    if "1+2" in message:
        return "3"
    if "oh rly?" in message:
        return "YA RLY!"
    return "2"

def idle_text():
    """Return text that is tweeted when not replying"""
    # Construct the text we want to tweet out (140 chars max)
    berlin_time = datetime.now(timezone('Europe/Berlin'))
    text = berlin_time.strftime("@RealDonaldTrump Donuts incoming %H:%M:%S on a %A (%d-%m-%Y)")
    return text

