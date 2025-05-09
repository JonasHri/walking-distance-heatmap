# %%
from dotenv import load_dotenv
import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")

# %%


def get_walking_distance(origin, destination, api_key):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
    params = {
        'origins': origin,
        'destinations': destination,
        'mode': 'walking',
        'key': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Extracting distance and duration
    if data['status'] == 'OK':
        distance = data['rows'][0]['elements'][0]['distance']['text']
        duration = data['rows'][0]['elements'][0]['duration']['text']
        return distance, duration
    else:
        return None, None

# Example usage:
origin = 'Dircksenstraße 2, 10179 Berlin'
destination = 'Hardenbergpl. 11, 10623 Berlin'

distance, duration = get_walking_distance(origin, destination, api_key)

# %%
distance, duration