import requests
import datetime
from pprint import pprint
from config import WEATHER_API_KEY


def get_weather(city, WEATHER_API_KEY):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму, что там за погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        print(f"*** {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')} ***\n"
              f"Погода в городе: {city}\n{wd}\nТемпература: {cur_weather} °C \nВлажность: {humidity} %\n"
              f"Давление: {pressure} мм.рт.ст\n"
              f"Скорость ветра: {wind} м/с\n"
              f"Время восхода солнца: {sunrise_timestamp}\nВремя захода солнца: {sunset_timestamp}\n"
              f"Длина дня в часах: {length_of_the_day}"
              )


    except Exception as ex:
        print(ex)
        print("Проверьте, что указали название города верно.")


def main():
    city = input("Введите название города: ")
    get_weather(city, WEATHER_API_KEY)


if __name__ == '__main__':
    main()
