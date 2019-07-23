import os
import tempfile

from flask_sqlalchemy import SQLAlchemy
import pytest

from flaskr import flaskr
from flask import Flask, jsonify
from sqlalchemy.testing.pickleable import User

from webapp import app as _app
from webapp import  db as _db
from webapp import  MyModel
from flask import url_for

from flask_testing import TestCase
from flask_testing import LiveServerTestCase
import urllib3
from webapp import create_app, db
import unittest
import flask_testing


app = Flask(__name__)

class TestLogin:
    def test_login_page(self, client):
        response = client.get("/login")


@pytest.fixture
def client(app):
    """Get a test client for your Flask app"""
    return app.test_client()

@pytest.fixture
def app():
    """Yield your app with its context set up and ready"""

    with _app.app_context():
        yield _app


class TestLogin:
    def test_login_page(self, client):
        # Use url_for to generate the URL for the endpoint directing the route "/login".
        # If you want to test the logic of user.login, there is no need to include
        # the route in the tests.
        response = client.get(url_for("user.login"))
        assert response.status_code == 200


def app():
    # Append "_test" to the name of the DB used for tests
    db_uri = _app.config["SQLALCHEMY_DATABASE_URI"]
    test_db_uri = f"{db_uri}_test"
    _app.update(SQLALCHEMY_DATABASE_URI=test_db_uri)

    with _app.app_context():
        yield _app

app = Flask(__name__)
db = SQLAlchemy()
db.init_app(app)

@pytest.fixture
def db(app):
    # Even though the "app" fixture is not used in this function, the context
    # of the app object need to be loaded for everything to work smoothly. Ugh...

    # We clean up the database before running each unit test
    _db.drop_all()
    _db.create_all()

    return _db

@pytest.fixture
def my_model(db):
    # Set up
    model = MyModel(name="Foo Bar")
    db.session.add(model)
    db.session.commit()

    return model

@pytest.fixture(scope="session")
def app():
    db_uri = _app.config["SQLALCHEMY_DATABASE_URI"]
    test_db_uri = f"{db_uri}_test"
    _app.update(SQLALCHEMY_DATABASE_URI=test_db_uri)

    with _app.app_context():
        yield _app

@pytest.fixture(scope="session")
def db(app):
    _db.drop_all()
    _db.create_all()

    return _db


@pytest.fixture
def my_model(db):
    # Set up
    model = MyModel(name="Foo Bar")
    db.session.add(model)
    db.session.commit()

    yield model

    # Tear down
    db.session.delete(model)
    db.session.commit()


@pytest.fixture
def session(db):
    db.session.begin_nested()

    yield db.session

    db.session.rollback()


######################################## ANOTHER EXAMPLE ##################################################

class MyTest(TestCase):

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

class MyTest(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True

        # Set to 0 to have the OS pick the port.
        app.config['LIVESERVER_PORT'] = 0

        return app

    def test_server_is_up_and_running(self):
        response = urllib3.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

# Testing JSON response
@app.route("/ajax/")
def some_json():
    return jsonify(success=True)

class TestViews(TestCase):
    def test_some_json(self):
        response = self.client.get("/ajax/")
        self.assertEquals(response.json, dict(success=True))

class MyTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):

        # pass in test configuration
        return create_app(self)

    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

class SomeTest(MyTest):

    def test_something(self):

        user = User()
        db.session.add(user)
        db.session.commit()

        # this works
        assert user in db.session

        response = self.client.get("/")

        # this raises an AssertionError
        assert user in db.session

# your test cases

if __name__ == '__main__':
    unittest.main()