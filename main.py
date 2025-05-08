import requests
import sys

IPWHO = "https://ipwho.is/"

def get_weather_api_url(city):
    return f"https://wttr.in/{city}?format=1"

def get_weather(city):
    try:
        response = requests.get(get_weather_api_url(city))
        if response.status_code == 200:
            weather_data = response.text
            return weather_data
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Failed to get weather for city: {e}")
        return None
    
def get_city_by_ip():
    try:
        response = requests.get(IPWHO)
        data = response.json()
        return data.get("city")
    except Exception as e:
        print(f"Failed to get city: {e}")
        return None
    
    
def main():
    if len(sys.argv) == 2:
        city = sys.argv[1]
    else:
        city = get_city_by_ip()
        if city == None:
            print(f"Failed to retrieve city data, city is {city}")
            return
    weather_api_response = get_weather(city)
    if weather_api_response:
        print(f"Weather in {city}: {weather_api_response}")
    else:
        print("Failed to retrieve weather data for city {city}")
    
if __name__ == "__main__":
    main()