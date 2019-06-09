import logging
from flask import jsonify, request
from flask_restplus import Api, Resource, fields

from api import restplus

log = logging.getLogger(__name__)

ns = restplus.api.namespace('supporting_shellfish', description='Testing operations for cutie supporting shellfish!')


@ns.route('/')
class Home(Resource):
    def get(self):
        """
        Says Hello for the first time!
        """
        result = jsonify({"result": "Hello!"})
        return result
