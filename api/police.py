import requests

def get_police_data(lat, lng, date="2026-01"):
    url = f"https://data.police.uk/api/crimes-street/all-crime?date={date}&lat={lat}&lng={lng}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            return None, "Records not found"
        if response.status_code == 429:
            return None, "Too many requests, try later"
        if 500 <= response.status_code < 600:
            return None, "API service unavailable"

        response.raise_for_status()
        return response.json(), None

    except requests.exceptions.ConnectionError:
        return None, "Connection error:\nCheck your internet connection"

    except requests.exceptions.Timeout:
        return None, "Timeout error:\nThe request took too long"

    except requests.exceptions.HTTPError as http_error:
        return None, f"Police service error:\n{http_error}"

    except requests.exceptions.RequestException as req_error:
        return None, f"Request error:\n{req_error}"

def get_most_common_crime(data):
    crime_category = {}

    for record in data:
        current_category = record["category"]
        if current_category in crime_category:
            crime_category[current_category] += 1
        else:
            crime_category[current_category] = 1

    most_common_crime = max(crime_category, key=crime_category.get)
    return most_common_crime, crime_category[most_common_crime]


# test
if __name__ == "__main__":

    # test data
    geo_data = {
        'postcode': 'SW1A 1AA',
        'longitude': -0.141563,
        'latitude': 51.50101,
        'region': 'London',
        'admin_district': 'Westminster'
    }

    date = "2023-07"

    data, msg = get_police_data(
        geo_data["latitude"],
        geo_data["longitude"],
        date
    )

    if data is None:
        print(msg)
    else:
        print(f"No. of Reports: {len(data)}")
        print(f"Report No. 1: {data[0]}")

