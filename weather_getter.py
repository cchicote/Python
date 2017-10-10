#! python2.7.13
# weather_getter.py - Prints the weather for a location from the command line.
# usage: weather_get <location>

from __future__ import print_function
import logging, sys, os, json, requests, pprint
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

def weather_getter():
    logging.debug("Start of weather_getter() function")
    
    logging.debug("Getting the arguments")
    if (len(sys.argv) < 2):
        raise Exception("Wrong number of arguments\nUsage: weather_get <location>")
    location = ' '.join(sys.argv[1:])
    logging.debug("LOCATION: %s" % (location))
    logging.debug("Arguments OK")

    logging.debug("Downloading the JSON data from OpenWeatherMap.org's API")
    url = "http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=9835dbe7f367377ea10f538f68051e6d" % (location)
    response = requests.get(url)
    response.raise_for_status()
    logging.debug("The address works")

    logging.debug("Loading JSON data into Python variable")
    weather_data = json.loads(response.text)
    logging.debug("(formatting text)\n\n\n")
    print("Current weather in %s: " % (weather_data["name"]))
    print(weather_data['weather'][0]['main'], '-', weather_data['weather'][0]['description'])
    print("\n\n")
    logging.debug("Leaving the function")
    
try:
    weather_getter()
except Exception as err:
    print("An exception happened: " + str(err))
logging.debug('End of program')
os.system("pause")

