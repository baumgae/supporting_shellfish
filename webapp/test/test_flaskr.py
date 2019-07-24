from flask import Flask, jsonify
from app import app

import json
import flask_testing
import pytest


test_image = open("encoded_kevin.txt", "w+")


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    return client


@pytest.fixture
def fake_image():
    data = {"image": test_image}

    return data


def test_get_route(client):
    url = '/'

    response = client.get(url)
    assert response.status_code == 200


def test_post_route(client, fake_image):
    url = '/advice'

    client.get(url)
    d = {"image": test_image}
    assert fake_image['image'] == d['image']

