import requests

def get_police_data(lat, lng, date):
    url = f"https://data.police.uk/api/crimes-street/all-crime?date={date}&lat={lat}&lng={lng}"

    response = requests.get(url)

    return response.json()

# test
if __name__ == "__main__":

    # test data
    geo_data = {
        'postcode': 'HP13 5HS',
        'longitude': -0.751839,
        'latitude': 51.636247,
        'region': 'South East',
        'admin_district': 'Buckinghamshire'
        }

    date = "2024-01"

    data = get_police_data(
        geo_data["latitude"],
        geo_data["longitude"],
        date
    )

    print(f"No. of Reports: {len(data)}")
    print(f"Report No. 1: {data[0]}")

