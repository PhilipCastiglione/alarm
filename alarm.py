import os
import sys
import time

import requests

try:
    url = sys.argv[1]
    response = requests.get(url)

    today = response.json()['daily']['data'][0]
    high_temp = round(today['temperatureHigh'])
    low_temp = round(today['temperatureLow'])
    summary = today['summary']

    os.system("say --rate=180 Today will have a high of")
    time.sleep(0.3)
    os.system("say --rate=180 {} ".format(high_temp))
    time.sleep(0.3)
    os.system("say --rate=180 degrees and a low of")
    time.sleep(0.3)
    os.system("say --rate=180 {}".format(low_temp))
    time.sleep(0.3)
    os.system("say --rate=180 {}".format(summary))
except:
    os.system("say --rate=180 'There was a problem fetching the weather.'")
