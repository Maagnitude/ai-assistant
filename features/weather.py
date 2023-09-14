import requests
import sys
from datetime import datetime
import json
from creds import weather_key

def get_weather(location, date=datetime.now().strftime("%Y-%m-%d")):
    api_key = weather_key
    
    try:
        # Make the API request
        response = requests.request("GET", f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location.lower()}?unitGroup=metric&include=current&key={api_key}&contentType=json")
        data = response.json()
        
        # Extract weather information from the response
        temperature = data['days'][0]['temp']
        conditions = data['days'][0]['conditions']
        
        # Convert the information into a spoken response
        msg = f"Today's weather in {location} is {conditions} with an average temperature of {temperature} degrees Celsius."
        
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        msg = "Sorry, I couldn't get the weather information at this time."
    
    return msg