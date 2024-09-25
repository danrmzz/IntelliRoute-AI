import requests
import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get API keys from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY")

def get_traffic_data(origin_lat, origin_lon, dest_lat, dest_lon):
    url = f"https://api.tomtom.com/routing/1/calculateRoute/{origin_lat},{origin_lon}:{dest_lat},{dest_lon}/json?key={TOMTOM_API_KEY}&traffic=true"

    response = requests.get(url)
    data = response.json()

    if "routes" in data and len(data["routes"]) > 0:
        travel_time = data['routes'][0]['summary']['trafficDelayInSeconds'] / 60  # in minutes
        travel_distance_km = data['routes'][0]['summary']['lengthInMeters'] / 1000  # in kilometers
        travel_distance_miles = travel_distance_km * 0.621371  # convert kilometers to miles
        return f"Travel time: {travel_time:.2f} minutes with traffic, Distance: {travel_distance_miles:.2f} miles"
    else:
        return "No route found."



try:

    # Define the coordinates for origin and destination
    origin_lat = 40.7580  # Times Square latitude
    origin_lon = -73.9855  # Times Square longitude
    dest_lat = 40.785091  # Central Park latitude
    dest_lon = -73.968285  # Central Park longitude

    # Fetch traffic data using the TomTom API
    traffic_info = get_traffic_data(origin_lat, origin_lon, dest_lat, dest_lon)


    # Use the traffic info in GPT-4's response
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides traffic advice."},
            {"role": "user", "content": f"What is the best route to get to Central Park from Times Square? The current traffic information is: {traffic_info}."}
        ]
    )

    # Print the AI response
    print(response['choices'][0]['message']['content'])


except Exception as e:
    print(f"Error communicating with OpenAI API: {e}")