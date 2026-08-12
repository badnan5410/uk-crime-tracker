import requests


def get_postcode(postcode):
    url = "https://api.postcodes.io/postcodes/"

    wanted_keys = [
        "postcode",
        "longitude",
        "latitude",
        "region",
        "admin_district"
    ]

    try:
        response = requests.get(
            f"{url}{postcode}",
            timeout=10
        )

        if response.status_code == 404:
            return None, "Postcode not found"

        if response.status_code == 400:
            return None, "Please check the postcode you entered"

        response.raise_for_status()

        big_data = response.json()["result"]
        data = {}

        for key in wanted_keys:
            data[key] = big_data[key]

        return data, None

    except requests.exceptions.ConnectionError:
        return None, "Connection error:\nCheck your internet connection"

    except requests.exceptions.Timeout:
        return None, "Timeout error:\nThe request took too long"

    except requests.exceptions.HTTPError as http_error:
        return None, f"Postcode service error:\n{http_error}"

    except requests.exceptions.RequestException as req_error:
        return None, f"Request error:\n{req_error}"






