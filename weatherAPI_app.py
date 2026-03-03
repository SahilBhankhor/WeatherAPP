import requests
import os
import pprint
from dotenv import load_dotenv  # helps in getting environment variable values

load_dotenv()  # loads the environment variables
# must be called in the beginning of the program


# create a function for greetings , city-input and show the api-result-data
def get_weather_data(city_name="New delhi"):

    request_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city_name}&units=metric"
    # create a variable (request_url) that contains the api_keys , uses the .env variables and also contains the city_name and units as SI(simple units of physics) system

    # print(request_url)
    weather_data = requests.get(request_url).json()
    # weather_data is created to fetch the data from the response_url and jsonify it
    return weather_data


if __name__ == '__main__':
    print(f"\nGet current weather conditions\n")
    city_name = input("\nenter the name of the city:\n")
    weather_data = get_weather_data(city_name)
    print("\n")
    pprint.pprint(weather_data)
