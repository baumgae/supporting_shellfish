from flask import Flask, jsonify
from sqlalchemy.testing.pickleable import User
from flask_testing import TestCase
from flask_testing import LiveServerTestCase
import urllib3
from app import create_app, db
import unittest


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


@app.route("/ajax/")
def some_json():
    return jsonify(success=True)

class TestViews(TestCase):
    def test_some_json(self):
        response = self.client.get("/ajax/")
        self.assertEquals(response.json, dict(success=True))


class TestNotRenderTemplates(TestCase):

    render_templates = False

    def test_assert_mytemplate_used(self):
        response = self.client.get("/template/")

        self.assert_template_used('index.html')


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