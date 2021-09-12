
"""
    Script_name: openweather_requests.py
       Function: From input city (asked for) returns current temperature,
                 minimum_temperature, maximum_temperature, humidity,
                 current UCT, sunrise UCT, sunset UCT, weather description,
                 and city name.
"""

import requests 
import json
import time

api_key = '[Put your API key here]'

base_url = 'http://api.openweathermap.org/data/2.5/weather?'

city_name = input('Enter city name:') 

complete_url = base_url + 'appid=' + api_key + '&q=' + city_name 

response = requests.get(complete_url) 

data_dictionary = response.json() 

CITY_NOT_FOUND = '404'

if data_dictionary['cod'] != CITY_NOT_FOUND: 
    current_temp = data_dictionary['main']['temp'] 
    minimum_temp = data_dictionary['main']['temp_min'] 
    maximum_temp = data_dictionary['main']['temp_max'] 
    humidity = data_dictionary['main']['humidity']

    current_date_uct = time.asctime(time.gmtime(data_dictionary['dt']))
    sunrise_uct = time.asctime(time.gmtime(data_dictionary['sys']['sunrise']))
    sunset_uct = time.asctime(time.gmtime(data_dictionary['sys']['sunset']))

    weather_description = data_dictionary['weather'][0]['description'] 

    print('                                 City:', city_name)
    print(' Current Temperature (in Kelvin unit):', current_temp)
    print(' Minimum Temperature (in Kelvin unit):', minimum_temp)
    print(' Maximum Temperature (in Kelvin unit):', maximum_temp)
    print()
    print('                   Current Date (UCT):', current_date_uct)
    print('                        Sunrise (UCT):', sunrise_uct)
    print('                         Sunset (UCT):', sunset_uct)
    print()
    print('                  Weather Description:', weather_description)
else: 
    print(' City Not Found ') 
