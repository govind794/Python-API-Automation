import requests
import pytest
import csv
import json

test_data_zip_codes = [
    ("Mumbai", 1, 19.1173981, 72.90691),
    ("Bengaluru", 2, 12.9034, 77.63093),
    ("Pune", 4, 18.578815, 73.73547)
]


@pytest.fixture()
def api_Response():
    url = "https://feature3.drivezytest.com/city?includes=venue"
    return requests.get(url)


@pytest.mark.parametrize("city_name, id, latitude, longitude", test_data_zip_codes)
def test_using_test_data_object_get_location_data_check_city_name_id_lat_long(city_name, id, latitude, longitude):
    response = requests.get("https://feature3.drivezytest.com/city?includes=venue")
    response_body = json.loads(response.text)["response"]
    for i in range(len(response_body)):
        if response_body[i]["name"] == city_name:
            assert response_body[i]["name"] == city_name
            assert response_body[i]["id"] == id
            assert response_body[i]["latitude"] == latitude
            assert response_body[i]["longitude"] == longitude

def read_test_data_from_csv():
    test_data = []
    with open('test_data_zip_codes.csv', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data)  # skip header row
        for row in data:
            test_data.append(row)
    return test_data


@pytest.mark.parametrize("city_name, id, latitude, longitude", read_test_data_from_csv())
def test_using_csv_get_location_data_check_city_name_id_lat_long(city_name, id, latitude, longitude):
    response = requests.get("https://feature3.drivezytest.com/city?includes=venue")
    response_body = json.loads(response.text)["response"]
    for i in range(len(response_body)):
        if response_body[i]["name"] == city_name:
            assert response_body[i]["name"] == city_name
            assert response_body[i]["id"] == int(id)
            assert response_body[i]["latitude"] == float(latitude)
            assert response_body[i]["longitude"] == float(longitude)
