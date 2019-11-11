DATE=$(date "+%D")
TIME=$(date "+%l %M")
meridian=$(date "+%p")
if [ $meridian == 'am' ]
then
  TIME_OF_DAY='morning'
  MERIDIAN='ay em'
elif [ $meridian == 'pm' ]
then
  TIME_OF_DAY='day'
  MERIDIAN='pee em'
fi

say --rate=180 "Good $TIME_OF_DAY."
sleep 1
say --rate=180 "Today is $DATE. It is $TIME $MERIDIAN."

DUB_LAT=53.3498
DUB_LONG=-6.2603
API_KEY=$(cat API_KEY)
API_URL="https://api.darksky.net/forecast/$API_KEY/$DUB_LAT,$DUB_LONG?exclude=[currently,minutely,hourly,alerts]&units=si"

pipenv run python alarm.py $API_URL
