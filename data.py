import requests

# Constants
TOTAL_QUESTIONS = 20

parameters = {
    "amount": TOTAL_QUESTIONS,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response_data = response.json()

questions_data = response_data["results"]
