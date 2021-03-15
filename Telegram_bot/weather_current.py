import requests
import json
from datetime import datetime

api_key = '123456789'
city_id ='686967' #Zhytomyr
lang = 'ru'
units = 'metric'
error = 'Ошибка получения данных :-('

weather_url = requests.get ('http://api.openweathermap.org/data/2.5/weather' , params = {'id' : city_id , 'units' : units, 'appid' : api_key, 'lang' : lang})
json_item = json.loads(weather_url.text)

try:
    for item in json_item:
        city = json_item["name"]
        sky = (json_item["weather"][0]["description"]).capitalize()
        humidity = 'Влажность: ' + str (int (json_item["main"]["humidity"])) + '%'
        temp = 'Температура: ' + str (int (json_item["main"]["temp"])) + ' ℃'
        feels_like = 'Ощущается как: ' + str (int (json_item["main"]["feels_like"]))
        date = 'Обновлено: ' + datetime.fromtimestamp(json_item["dt"]).strftime('%d-%m-%Y %H:%M:%S')
        wind_spped = 'Ветер: ' + str (int (json_item["wind"]["speed"] * 3.6))  + ' km/h'
        
        current = [city, sky, humidity, temp, feels_like, date, wind_spped]
except:
    current = [error]

current = [city, sky, humidity, temp, feels_like, date,wind_spped]
#print (json_item["weather"][0]["description"])
#print (city)
#print (sky)
#print (humidity)
#print (temp)
#print (feels_like)
#print (date)
#print (wind_spped)