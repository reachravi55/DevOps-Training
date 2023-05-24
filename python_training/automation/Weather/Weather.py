import requests
import datetime as dt
from dateutil import tz
API_KEY = input("Enter your OpenWeatherMap API key: ") # you can also hard code it, but its a good practice not to hardcode it.
API_URL = "http://api.openweathermap.org/data/2.5/weather"
BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"

'''
def get_weather(CITY):
    url = f"{API_URL}?appid={API_KEY}&q={CITY}"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())
    else:
        print ("None")
'''
city = input("Enter city name: ")
example_url = f"{BASE_URL}?q={city}&limit=5&appid={API_KEY}"
request_url = f"{API_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)
    
if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temp = round((data["main"]["temp"] - 273.15)* (9/5) + 32)
    timezone = dt.datetime.utcfromtimestamp(data["dt"] + data["timezone"])
    sunset = dt.datetime.utcfromtimestamp(data["sys"]["sunset"] + data["timezone"])
    sunrise = dt.datetime.utcfromtimestamp(data["sys"]["sunrise"] + data["timezone"])
    print(f"weather is {weather} \ntemperature is {temp}° farenheit\ncurrent time is {timezone}\nsunrises at {sunrise}\nsunset's at {sunset}")
else:
    if response.status_code == 404:
        print("City not found")
    elif response.status_code == 500:
        print("Internal server error")
    elif response.status_code == 400:
        print("Bad request")
    elif response.status_code == 401:
        print("Unauthorized")
    elif response.status_code == 403:
        print("Forbidden")
    elif response.status_code == 429:
        print("Too many requests")
    elif response.status_code == 503:
        print("Service unavailable")
    elif response.status_code == 504:
        print("Gateway timeout")
    elif response.status_code == 408:
        print("Request timeout")
    elif response.status_code == 409:
        print("Conflict")
    elif response.status_code == 410:
        print("Gone")
    elif response.status_code == 411:
        print("Length required")
    elif response.status_code == 412:
        print("Precondition failed")
    elif response.status_code == 413:
        print("Payload too large")
    elif response.status_code == 414:
        print("URI too long")
    elif response.status_code == 415:
        print("Unsupported media type")
    elif response.status_code == 416:
        print("Range not satisfiable")
    elif response.status_code == 417:
        print("Expectation failed")
    elif response.status_code == 418:
        print("I'm a teapot")
    elif response.status_code == 421:
        print("Misdirected request")
    elif response.status_code == 422:
        print("Unprocessable entity")
    elif response.status_code == 423:
        print("Locked")
    elif response.status_code == 424:
        print("Failed dependency")
    elif response.status_code == 426:
        print("Upgrade required")
    elif response.status_code == 428:
        print("Precondition required")
    elif response.status_code == 429:
        print("Too many requests")
    elif response.status_code == 431:
        print("Request header fields too large")
    elif response.status_code == 451:
        print("Unavailable for legal reasons")
    
    

    print (response.status_code)