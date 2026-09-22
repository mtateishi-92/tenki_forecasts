import requests

data = requests.get("https://weather.tsukumijima.net/api/forecast/city/130010").json()

date_today = data["forecasts"][0]["dateLabel"]
date_tomorrow = data["forecasts"][1]["dateLabel"]
temp_today = data["forecasts"][0]["temperature"]["max"]["celsius"]
temp_tomorrow= data["forecasts"][1]["temperature"]["max"]["celsius"]

print(f"今日の東京都の気温: {date_today}の気温は{temp_today}℃")
print(f"明日の東京都の気温: {date_tomorrow}の気温は{temp_tomorrow}℃")
