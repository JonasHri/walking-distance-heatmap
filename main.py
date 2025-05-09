# %%
from dotenv import load_dotenv
import requests
import os

load_dotenv()
api_key = os.getenv("API_KEY")

# %%


def get_walking_distance(origins, destinations, api_key):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": "|".join(origins),
        "destinations": "|".join(destinations),
        "mode": "walking",
        "key": api_key,
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Check for a successful API call
    if data['status'] != 'OK':
        print("Error with request:", data.get('error_message', data['status']))
        return None

    # Parse results
    results = []
    for i, row in enumerate(data['rows']):
        origin = origins[i]
        for j, element in enumerate(row['elements']):
            destination = destinations[j]
            if element['status'] == 'OK':
                distance = element['distance']['text']
                duration = element['duration']['text']
                results.append({
                    'origin': origin,
                    'destination': destination,
                    'distance': distance,
                    'duration': duration
                })
            else:
                results.append({
                    'origin': origin,
                    'destination': destination,
                    'error': element['status']
                })

    return results


# Example usage:
origin = [
    "Dircksenstraße 2, 10179 Berlin",
    "Georgenstraße 14/17, 10117 Berlin",
    "Brandenburger Tor, 10117 Berlin",
    "Stadtmitte, 10117 Berlin",
    "Jannowitzbrücke, 10179 Berlin",
]
destination = [
    "Hardenbergpl. 11, 10623 Berlin",
    "Friedrichstraße 141-142, 10117 Berlin",
    "Europaplatz 1, 10557 Berlin",
    "Hanne-Sobek-Platz 1, 13357 Berlin",
    "Bahnhof Berlin Alexanderplatz, Alexanderpl. 1, 10178 Berlin",
]

results = get_walking_distance(origin, destination, api_key)

# %%
import pickle

with open("data.pkl", "wb") as f:
    pickle.dump(results, f)


# %%
import pickle

with open("data.pkl", "rb") as f:
    results = pickle.load(f)
    
results