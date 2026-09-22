import sys
import requests

if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

# 東京都のシティコード (livedoor天気互換APIの地域コード)
TOKYO_CITY_CODE = "130010"
API_URL = f"https://weather.tsukumijima.net/api/forecast/city/{TOKYO_CITY_CODE}"


def get_tokyo_weather():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()


def main():
    data = get_tokyo_weather()

    print(f"地域: {data['location']['prefecture']} {data['location']['city']}")
    print(f"発表元: {data['copyright']['title']}")
    print()

    for forecast in data["forecasts"]:
        print(f"[{forecast['dateLabel']}] {forecast['date']}")
        print(f"  天気: {forecast['telop']}")
        temp_min = forecast["temperature"]["min"]["celsius"]
        temp_max = forecast["temperature"]["max"]["celsius"]
        print(f"  最低気温: {temp_min if temp_min else '--'}℃ / 最高気温: {temp_max if temp_max else '--'}℃")
        print()

    print("--- 詳細 ---")
    print(data["description"]["text"])


if __name__ == "__main__":
    main()
