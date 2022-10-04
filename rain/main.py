import requests
from twilio.rest import Client

#Please enter your own keys 
OWM_Endpoint = ""
api_key = ""

account_sid = ""
auth_token = ""


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

