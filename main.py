import requests
import sys

def weather_api(city):
    try:
        response = requests.get(f"https://wttr.in/{city}?format=1")
        if response.status_code == 200:
            weather_data = response.text
            return weather_data
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Failed to get weather: {e}")
        return None
    
def city_api():
    try:
        response = requests.get("https://ipwho.is/")
        data = response.json()
        return data.get("city")
    except Exception as e:
        print(f"Failed to get city: {e}")
        return None
    
    
def main():
    if len(sys.argv) == 2:
        city = sys.argv[1]
    else:
        city = city_api()
        if city == None:
            print("Failed to retrieve city data")
            return
    weather_api_response = weather_api(city)
    if weather_api_response:
        print(f"Weather in {city}: {weather_api_response}")
    else:
        print("Failed to retrieve weather data")
    
if __name__ == "__main__":
    main()