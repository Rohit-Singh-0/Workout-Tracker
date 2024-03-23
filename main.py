import requests
from datetime import datetime
import os

# Constants for user information
GENDER = 'male'
WEIGHT_KG = 77
HEIGHT_CM = 170
AGE = 22

# API credentials
APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']

# API endpoints
URL = os.environ['URL']
workout_url = os.environ['workout_url']

# Get user input for workout
workout = input("What exercise have you done today?\n")

# Set headers for API request
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

# Set parameters for API request
parameters = {
    "query": workout,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Get current date and time
date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Send API request to get exercise information
response = requests.post(url=URL, headers=headers, json=parameters)
# print(response.json())

# Process each exercise in the response
for exercise in response.json()["exercises"]:
    # Prepare data for adding to the workout sheet
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": str(exercise["duration_min"]),
            "calories": exercise["nf_calories"]
        }
    }
    # Send API request to add exercise to the workout sheet
    work_response = requests.post(url=workout_url, json=sheet_inputs)
    # print(work_response.text)
