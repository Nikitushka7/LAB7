import requests


def get_holidays(api_key, country, year, month=None, day=None):
    url = "https://holidayapi.com/v1/holidays"
    params = {
        "key": api_key,
        "country": country,
        "year": year,
        "month": month,
        "day": day,
    }
    response = requests.get(url, params=params)
    if response.status_code != 404:
        return response.json()
    else:
        return {"error": f"Failed to fetch data: {response.status_code}"}


def print_holidays(holidays):
    if "holidays" in holidays:
        for holiday in holidays["holidays"]:
            print(f"{holiday['date']}: {holiday['name']}")
    else:
        print("No holidays found or an error occurred.")
    if int(month) > 12:
        print("Введён несуществующий месяц")


# Пример использования
API_KEY = "a61c2fcd-c5d7-45a5-93e9-60bb57f7369d"  # Замените на свой API-ключ
country = "RU"  # Код страны (например, US, RU, DE)
year = 2024
month = input("Введите номер месяца (например, 01 для января): ")

holidays = get_holidays(API_KEY, country, year, month)
print_holidays(holidays)
