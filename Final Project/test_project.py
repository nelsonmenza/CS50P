"""Modules"""
from unittest import mock
from unittest.mock import patch, call
import pytest
import requests
from project import _get_api_key, read_user_cli_args, display_weather_info


def main():
    """main function"""
    test_display_weather_info()
    test_read_user_cli_args()
    test_handle_http_error()  # Works without value
    test_request_timeout()
    test_get_api_key_missing_key()


def test_get_api_key_missing_key():
    """Mock the behavior of reading the configuration file with missing key"""
    with mock.patch("builtins.open", mock.mock_open(read_data="[openweather]\nother_key=my_api_key")):
        # Check if the function raises the expected exception
        with pytest.raises(SystemExit):
            _get_api_key()


def test_read_user_cli_args():
    """Simulate command-line arguments"""
    args = ["New", "York", "-i", "-f"]

    # Mock the sys.argv list to simulate command-line arguments
    with patch("sys.argv", ["project.py"] + args):
        parsed_args = read_user_cli_args()
        assert parsed_args.city == args[0:2]
        assert parsed_args.imperial is True
        assert parsed_args.forecast is True


def test_display_weather_info():
    """Simulate weather data"""
    weather_data = {
        "location": {"name": "New York", "country": "USA"},
        "current": {
            "condition": {"text": "Clear"},
            "humidity": 80,
            "temp_c": 20,
            "temp_f": 68,
            "feelslike_c": 22,
            "feelslike_f": 72,
        },
        "forecast": {
            "forecastday": [
                {
                    "date": "2023-07-19",
                    "day": {"avghumidity": 75, "avgtemp_c": 22, "avgtemp_f": 72},
                }
            ]
        },
    }

    # Capture the printed output
    with patch("builtins.print") as mock_print:
        display_weather_info(weather_data, imperial=True, forecast=True)

    # Define the expected calls to the print function
    expected_calls = [
        call("\nForecast date: 2023-07-19"),
        call("            New York,  USA ", end=""),
        call("   ##########   Avg. Temperature: (72°F)"),
        call("------------------------------------------------------------> Avg. Humidity: 75%\n"),
    ]

    # Compare the captured calls to the print function with the expected calls
    assert mock_print.call_args_list == expected_calls


@mock.patch('requests.get')
def test_handle_http_error(mock_request):
    """Test handle http error"""
    mock_resp = requests.models.Response()
    mock_resp.status_code = 400
    mock_request.return_value = mock_resp
    res = requests.get("http://api.weatherapi.com/v1/", timeout=1)
    with pytest.raises(requests.exceptions.HTTPError) as http_error:
        res.raise_for_status()
    print(http_error)

    mock_resp = requests.models.Response()
    mock_resp.status_code = 401
    mock_request.return_value = mock_resp
    res = requests.get("http://api.weatherapi.com/v1/", timeout=1)
    with pytest.raises(requests.exceptions.HTTPError) as http_error:
        res.raise_for_status()
    print(http_error)

    mock_resp = requests.models.Response()
    mock_resp.status_code = 403
    mock_request.return_value = mock_resp
    res = requests.get("http://api.weatherapi.com/v1/", timeout=1)
    with pytest.raises(requests.exceptions.HTTPError) as http_error:
        res.raise_for_status()
    print(http_error)


def test_request_timeout():
    """Test request timeout."""
    with mock.patch("requests.get") as mock_request:
        mock_resp = requests.models.Response()
        mock_resp.status_code = 500
        mock_resp.reason = "Internal Server Error"  # Set a reason for the error status
        mock_resp.url = "http://api.weatherapi.com/v1/"  # Set a URL for the response
        mock_request.return_value = mock_resp
        res = requests.get("http://api.weatherapi.com/v1/", timeout=0.01)
        with pytest.raises(requests.exceptions.HTTPError) as http_error:
            res.raise_for_status()
        assert str(
            http_error.value) == """500 Server Error: Internal Server Error for url: http://api.weatherapi.com/v1/"""


if __name__ == "__main__":
    pytest.main()
