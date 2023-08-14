import requests
import os

host = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")[2]
ENDPOINT = f"{host}:{os.environ.get('APP_PORT')}/popular/"


def test_can_call_endpoint():
    response = list_fact()
    assert response.status_code == 200


def list_fact():
    return requests.get(f"{ENDPOINT}")
