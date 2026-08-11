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

    response = requests.get(f"{url}{postcode}")

    if response.status_code == 200:
        big_data = response.json()["result"]
        data = {}

        for key in wanted_keys:
            data[key] = big_data[key]

        return data
    else:
        return None