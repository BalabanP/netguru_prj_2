import requests
import os

host = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")[1]
ENDPOINT = f"{host}:{os.environ.get('APP_PORT')}/dates/"


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_can_create_fun_dates():
    payload = {"month": 5, "day": 12}
    create_task_response = create_fact(payload=payload)

    assert create_task_response.status_code == 201
    assert create_task_response.json().get("msg") == "Data Created"
    id = create_task_response.json().get("data").get("id")

    # get id
    get_task_response = get_fact(id=id)
    assert get_task_response.json().get("month") == payload.get("month")
    assert get_task_response.json().get("day") == payload.get("day")
    delete(id)


def test_can_create_and_update_fun_dates():
    payload = {"month": 5, "day": 12}
    create_task_response = create_fact(payload=payload)
    update_task_response = create_fact(payload=payload)

    assert update_task_response.status_code == 200
    assert update_task_response.json().get("msg") == "Data Updated"
    id = update_task_response.json().get("data").get("id")

    # get id from
    get_task_response = get_fact(id=id)
    assert get_task_response.json().get("fact") != create_task_response.json().get(
        "data"
    ).get("fact")
    delete(id)


def test_can_update():
    payload = {"month": 5, "day": 12}
    response = create_fact(payload=payload)
    id = response.json().get("data").get("id")
    updated_payload = {"month": 5, "day": 31}
    update_response = update_fact(id, updated_payload)
    assert update_response.status_code == 200
    assert update_response.json().get("msg") == "Data Updated"

    get_task_response = get_fact(id=id)
    assert get_task_response.json().get("day") == update_response.json().get(
        "data"
    ).get("day")
    delete(id)


def test_can_delete():
    payload = {"month": 5, "day": 12}
    response = create_fact(payload=payload)
    id = response.json().get("data").get("id")
    delete_response = delete(id)
    assert delete_response.json().get("msg") == "Data Deleted"
    assert delete_response.json().get("id") == id

    get_response = get_fact(id)
    assert get_response.status_code == 404


def create_fact(payload):
    return requests.post(ENDPOINT, json=payload)


def get_fact(id):
    return requests.get(f"{ENDPOINT}{id}/")


def list_fact():
    return requests.get(f"{ENDPOINT}")


def update_fact(id, payload):
    return requests.put(f"{ENDPOINT}{id}/", json=payload)


def delete(id):
    return requests.delete(
        f"{ENDPOINT}{id}/",
        headers={os.environ.get("DELETE_KEY"): os.environ.get("DELETE_KEY_VALUE")},
    )
