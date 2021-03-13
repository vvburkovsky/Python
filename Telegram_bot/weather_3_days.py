import requests
import json
from datetime import datetime

api_key = '123456789'

#Zhytomyr
lat = '50.2649'
lon = '28.6767'

lang = 'ru'
units = 'metric'
exclude = 'minutely,hourly,alerts'

weather_url = requests.get ('http://api.openweathermap.org/data/2.5/onecall?' , params = {'lat' : lat, 'lon' : lon, 'exclude' : exclude, 'units' : units, 'appid' : api_key, 'lang' : lang})
json_item = json.loads(weather_url.text)

today = json_item["daily"][0] #сегодня
tomorrow = json_item["daily"][1] #завтра
day_after_tomorrow =  json_item["daily"][2] #послезавтра

today_date = datetime.fromtimestamp(today["dt"]).strftime('%d-%m-%Y')
tomorrow_date = datetime.fromtimestamp(tomorrow["dt"]).strftime('%d-%m-%Y')
day_after_tomorrow_date = datetime.fromtimestamp(day_after_tomorrow["dt"]).strftime('%d-%m-%Y')


def weather_today ():
    for item in today:
        return ( 'Сегодня ' + today_date + ':' + '\n' +
                today["weather"][0]["description"].capitalize() + '\n' +
                'Температура днем: ' + str (int (today["temp"]["day"])) + ' ℃' + '\n' +
                'Температура ночью: ' + str (int (today["temp"]["night"])) + ' ℃' + '\n' +
                'Ветер: ' + str (int (today["wind_speed"] * 3.6))  + ' km/h' )

def weather_tomorrow ():
    for item in tomorrow:
        return ('\n' 'Завтра ' + tomorrow_date + ':' + '\n' +
                tomorrow["weather"][0]["description"].capitalize() + '\n' +
                'Температура днем: ' + str (int (tomorrow["temp"]["day"])) + ' ℃' + '\n' +
                'Температура ночью: ' + str (int (tomorrow["temp"]["night"])) + ' ℃' + '\n' +
                'Ветер: ' + str (int (tomorrow["wind_speed"] * 3.6))  + ' km/h' )

def weather_day_after_tomorrow ():
    for item in day_after_tomorrow:
        return ('\n' 'Послезавтра ' + day_after_tomorrow_date + ':' + '\n' +
                day_after_tomorrow["weather"][0]["description"].capitalize() + '\n' +
                'Температура днем: ' + str (int (day_after_tomorrow["temp"]["day"])) + ' ℃' + '\n' +
                'Температура ночью: ' + str (int (day_after_tomorrow["temp"]["night"])) + ' ℃' + '\n' +
                'Ветер: ' + str (int (day_after_tomorrow["wind_speed"] * 3.6))  + ' km/h' )

#print (weather_today())
#print (weather_tomorrow())
#print (weather_day_after_tomorrow())