import json

import pytest

from say_hello import app


@pytest.fixture()
def lincoln_event():
    return {"body": '{ "name": "Lincoln"}'}


@pytest.fixture()
def teapot_event():
    return {"body": '{ "name": "Teapot"}'}


def test_lambda_handler(lincoln_event):

    response = app.lambda_handler(lincoln_event, "")
    data = json.loads(response["body"])

    assert response["statusCode"] == 200
    assert "message" in response["body"]
    assert data["message"] == "Hello Lincoln!"


def test_lambda_handler_teapot(teapot_event):

    response = app.lambda_handler(teapot_event, "")
    data = json.loads(response["body"])

    assert response["statusCode"] == 418
    assert "message" in response["body"]
    assert data["message"] == "Hello Teapot!"


def test_lambda_handler_without_name_input():
    response = app.lambda_handler("", "")
    status_code = response.pop("statusCode")
    assert status_code == 400
    assert response == {}
