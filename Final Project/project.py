"""Modules"""
import argparse
import sys
from configparser import ConfigParser

import requests

# Main function that orchestrates weather info retrieval and display


def main():
    """Main function that retrieves weather data and displays it."""
    user_args = read_user_cli_args()
    weather_data = request_data(user_args.city, user_args.forecast)
    display_weather_info(weather_data, user_args.imperial, user_args.forecast)

# Request weather data from the API


def request_data(city_input, forecast=False):
    """
    Request weather data from the API.

    Args:
        city_input (list): List of city name or country name.
        forecast (bool, optional): Whether to fetch a forecast. Defaults to False.

    Returns:
        dict: JSON response containing weather data.
    """
    city_input = " ".join(city_input)
    api_key = _get_api_key()

    if forecast:

        print("\nDate between 14 days and 300 days from today in the future in yyyy-mm-dd format")
        date_input = input("Enter a valid date in format yyyy-mm-dd: ")
        url = f"http://api.weatherapi.com/v1/future.json?key={api_key}&q={city_input}&dt={date_input}"
    else:
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_input}&aqi=no"

    try:
        request_json = requests.get(f"{url}", timeout=0.8)
        request_json.raise_for_status()
    except requests.exceptions.HTTPError as http_error:
        handle_http_error(http_error)
    except requests.exceptions.ReadTimeout:
        sys.exit("Timeout Error.")
    else:
        return request_json.json()

# Fetch the API key from the configuration file


def _get_api_key():
    """
    Fetch the API key from the configuration file.

    Returns:
        str: API key.
    """
    config = ConfigParser()
    config.read("secrets.ini")
    try:
        return config["openweather"]["api_key"]
    except KeyError:
        sys.exit("Check file with the API key.")

# Parse command-line arguments provided by the user


def read_user_cli_args():
    """
    Parse command-line arguments provided by the user.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Get weather and temperature information for a city."
    )
    parser.add_argument(
        "city", nargs="+", type=str, help="""Name of the city or country, or both. 
        Example: <city> or <country, city>"""
    )
    parser.add_argument(
        "-i", "--imperial", action="store_true", help="""Display the temperature in 
        imperial units (Fahrenheit). Example: <city -i>""",
    )
    parser.add_argument(
        "-f",
        "--forecast",
        action="store_true",
        help="""Request a weather forecast for a specific date in the future
        (in yyyy-mm-dd format). Example: <city -f>"""
    )
    return parser.parse_args()

# Prints formatted weather information about a city


def display_weather_info(weather_data, imperial=False, forecast=False):
    """
    Prints formatted weather information about a city.

    Args:
        weather_data (dict): API response weatherapi by city name
        imperial (bool): Whether or not to use imperial units for temperature
        forecast (bool): Whether it's a forecast request

    More information at https://www.weatherapi.com/docs/
    """
    city = weather_data["location"]["name"]
    country = weather_data["location"]["country"]

    if forecast:
        forecast_date = weather_data["forecast"]["forecastday"][0]["date"]
        avg_humidity = weather_data["forecast"]["forecastday"][0]["day"]["avghumidity"]
        if imperial:
            avg_temp = weather_data["forecast"]["forecastday"][0]["day"]["avgtemp_f"]
        else:
            avg_temp = weather_data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]

        print(f"\nForecast date: {forecast_date}")
        print(f"{city:>20}, {country:^5}", end="")
        print(
            f"   {'#' * 10}   Avg. Temperature: ({avg_temp}°{'F' if imperial else 'C'})")
        print(
            f"{'-' * 60}> Avg. Humidity: {avg_humidity}%\n")

    else:
        local_time = weather_data["location"]["localtime"]
        weather_description = weather_data["current"]["condition"]["text"]
        humidity = weather_data["current"]["humidity"]
        if imperial:
            temperature = weather_data["current"]["temp_f"]
            feels_like = weather_data["current"]["feelslike_f"]
        else:
            temperature = weather_data["current"]["temp_c"]
            feels_like = weather_data["current"]["feelslike_c"]

        print(f"\nLocal Time: {local_time:^15}")
        print(f"{city:>20}, {country:^5}", end="")
        print(f"\t{weather_description.capitalize():^25}", end=" ")
        print(f"({temperature}°{'F' if imperial else 'C'})\n")
        print(
            f"{'-' * 60}> Humidity: {humidity}%")
        print(
            f"{'-' * 60}> Feels like: ({feels_like}°{'F' if imperial else 'C'})\n")

# Handles HTTP errors during the API request


def handle_http_error(http_error):
    """
    Handles HTTP errors during the API request.

    Args:
        http_error (requests.exceptions.HTTPError): HTTP error object.
    """
    if http_error.response.status_code == 400:
        sys.exit("Can't find weather data for this city. Check your input.")
    elif http_error.response.status_code in (401, 403):
        sys.exit("Access denied. Check your API key.")


if __name__ == "__main__":
    main()
