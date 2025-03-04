import requests


def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]

        temperature = main["temp"]
        humidity = main["humidity"]
        pressure = main["pressure"]
        weather_description = weather["description"]

        print(f"Погода в городе {city_name}:")
        print(f"Температура: {temperature}°C")
        print(f"Влажность: {humidity}%")
        print(f"Давление: {pressure} hPa")
        print(f"Описание: {weather_description.capitalize()}")
    else:
        print("Город не найден.")


if __name__ == "__main__":
    city_name = "Orsk"  # Замените на нужный город
    api_key = "26838dda1cb9f9aeb1082cfcc2e34216"  # Замените на ваш API ключ от OpenWeatherMap
    get_weather(city_name, api_key)