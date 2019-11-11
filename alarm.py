import os
import sys
import time

import requests

try:
    url = sys.argv[1]
    response = requests.get(url)

    today = response.json()['daily']['data'][0]
    min_temp = round(today['temperatureLow'])
    max_temp = round(today['temperatureHigh'])
    summary = today['summary']

    os.system("say --rate=180 Today will have a maximum of")
    time.sleep(0.3)
    os.system("say --rate=180 {} ".format(max_temp))
    time.sleep(0.3)
    os.system("say --rate=180 degrees and a minimum of")
    time.sleep(0.3)
    os.system("say --rate=180 {}".format(min_temp))
    time.sleep(0.3)
    os.system("say --rate=180 {}".format(summary))
except:
    os.system("say --rate=180 'There was a problem fetching the weather.'")
