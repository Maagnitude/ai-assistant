import requests
from datetime import datetime
from creds import weather_key

def get_weather(location='Athens', date=datetime.now().strftime("%Y-%m-%d")):
    api_key = weather_key
    
    try:
        # Make the API request
        response = requests.request("GET", f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location.lower()}?unitGroup=metric&include=current&key={api_key}&contentType=json")
        data = response.json()
        
        # Extract weather information from the response
        temperature = data['days'][0]['temp']
        conditions = data['days'][0]['conditions']
        
        country = get_country_by_city(location)
        
        if country != "City not found" and country != "Data not available":
            msg = f"Today's weather in {location.capitalize()} {country} is {conditions} with an average temperature of {temperature} degrees Celsius."
        else:
            msg = f"Today's weather in {location.capitalize()} is {conditions} with an average temperature of {temperature} degrees Celsius."
        
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        msg = "Sorry, I couldn't get the weather information at this time."
    
    return msg


def get_country_by_city(city_name):
    
    base_url = "https://countriesnow.space/api/v0.1/countries/population/cities"
    
    payload = {
        "city": city_name
    }

    try:
        response = requests.post(base_url, json=payload)
        data = response.json()
        if "data" in data and "country" in data["data"]:
            country = data["data"]["country"]
            return country
        else:
            return "City not found"
    except Exception as e:
        return str(e)