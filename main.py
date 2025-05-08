import requests

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
        print(f"Error while getting weather: {e}")
        return None
    
    
def main():
    weather_api_response = weather_api("Tomsk")
    if weather_api_response:
        print(f"Weather in Tomsk: {weather_api_response}")
    else:
        print("Failed to retrieve weather data")
    
if __name__ == "__main__":
    main()