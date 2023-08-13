ENDPOINT = "http://0.0.0.0:8000/dates/"
import requests


# data = response.json()
# print(response, data)


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_can_create_fun_dates():
    payload = {"month": 1, "day": 2}
    response = requests.post(ENDPOINT, json=payload)

    assert response.status_code == 201
    assert response.json().get("msg") == "Data  created"

    id = 
    print(response.json())


test_can_create_fun_dates()
