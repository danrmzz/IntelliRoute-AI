import requests
import openai
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Load environment variables from the .env file
load_dotenv()

# Get API keys from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY")

# Initialize Flask app
app = Flask(__name__)

# Function to get latitude and longitude for an address using the TomTom Geocoding API
def get_lat_lon(address):
    url = f"https://api.tomtom.com/search/2/geocode/{address}.json?key={TOMTOM_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if 'results' in data and len(data['results']) > 0:
        lat = data['results'][0]['position']['lat']
        lon = data['results'][0]['position']['lon']
        return lat, lon
    else:
        return None, None

# Function to get traffic data using lat/lon values
def get_traffic_data(origin_lat, origin_lon, dest_lat, dest_lon):
    url = f"https://api.tomtom.com/routing/1/calculateRoute/{origin_lat},{origin_lon}:{dest_lat},{dest_lon}/json?key={TOMTOM_API_KEY}&traffic=true"

    response = requests.get(url)
    data = response.json()

    if "routes" in data and len(data["routes"]) > 0:
        travel_time = data['routes'][0]['summary']['travelTimeInSeconds']
        traffic_delay = data['routes'][0]['summary']['trafficDelayInSeconds']
        total_travel_time = (travel_time + traffic_delay) / 60 # in minutes
        travel_distance_km = data['routes'][0]['summary']['lengthInMeters'] / 1000  # in kilometers
        travel_distance_miles = travel_distance_km * 0.621371  # convert kilometers to miles

        # Display travel time in minutes if < 60, or hours if >= 60
        if total_travel_time < 60:
            time_str = f"{int(total_travel_time)} minutes"
        else:
            hours = total_travel_time // 60  # Get hours as an integer
            minutes = total_travel_time % 60  # Get the remaining minutes
            time_str = f"{int(hours)} hours and {int(minutes)} minutes"

        # Convert distance to an integer for a cleaner output
        travel_distance_miles = int(travel_distance_miles)



        return f"Travel time: {time_str} with traffic, Distance: {travel_distance_miles} miles"
    else:
        return "No route found."
    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        origin = request.form.get('origin') # get origin from form
        destination = request.form.get('destination') # get destination from form


        # Get latitude and longitude for origin and destination
        origin_lat, origin_lon = get_lat_lon(origin)
        dest_lat, dest_lon = get_lat_lon(destination)


        # Get traffic data using TomTom API
        traffic_info = get_traffic_data(origin_lat, origin_lon, dest_lat, dest_lon)

        # Use the traffic info in GPT-4's response
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides traffic advice based on the input data. Do not mention alternative apps."},
                {"role": "user", "content": f"What is the best route to get from {origin} to {destination}? The current traffic information is: {traffic_info}."}
            ]
        )

        # Print the AI response
        ai_response = response['choices'][0]['message']['content']

        return render_template('index.html', traffic_info=traffic_info, ai_response=ai_response)
    
    return render_template('index.html', traffic_info=None, ai_response=None)

if __name__ == "__main__":
    app.run(debug=True)