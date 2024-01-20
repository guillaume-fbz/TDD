import requests


class WeatherService:

    def __init__(self):
        self.api_key = "ASK ME FOR THE API_KEY :)"

    def get_temperature(self, city):
        response = requests.get(
            f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={self.api_key}")
        return response.json()['data']['values']['temperature']

