import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "c12e3bb06942d41be5d6d3cda5c99a45"

account_sid = "ACad501b10965ad53866d91a21584800fa"
auth_token = "18260c00f1bdd29f40364823bb016a71"


weather_params={
    "lat":21.831060,
    "lon":85.567047,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body = "It's going to rain Today. Remember to bring an Umbrella.",
        from_ = "+17247345493",
        to = "+91 78150 12669"
    )

