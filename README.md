# Alarm

A wakeup announcement of the date/time and current weather (in Dublin).

The `alarm.sh` file contains shell code for announcing the time. This should always work and run.

The `alarm.py` file attempts to fetch the weather from an external service. This is announced if succeeding, or apologised for if failing.

Don't @ me.

## Requirements

* Python, requests lib.
* DarkSky API key in file called `API_KEY`.
