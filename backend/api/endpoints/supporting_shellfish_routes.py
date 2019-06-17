import logging
import json
from flask import jsonify, request, make_response
from flask_restplus import Api, Resource, fields
from api import restplus
from ibm_watson import VisualRecognitionV3
log = logging.getLogger(__name__)

# Namespace for app.py
ns = restplus.api.namespace('supporting_shellfish', description='Testing operations for cutie supporting shellfish!')

# Payload Model
imageurl = restplus.api.model("ImageURL", {"image" : fields.String(required=True, description='Picture of user to classify')})

# Init Visual Recognition
visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='2u8IHpivxsV6Lf1vb08Pe8eCbWEb1FjlelRZ1xWLwKCC')

# Test URL - an Alpaka
url = 'https://tinyurl.com/yycgnzzh'

# One-Pager-SupportingShellfish
@ns.route('/')
class SupportingShellfish(Resource):
    @ns.doc('welcome')
    def get(self):
        """
        Welcome the user!
        :return Welcome String!
        """

        msg = jsonify({"result": "Hello! Welcome to Supporting Shellfish!"})
        response = make_response(msg, 200)
        return response

    @ns.doc('advice')
    @ns.expect(imageurl)
    def post(self):
        """
        User is now able to upload a picture or take one.
        :return: An advice and recognized attributes
        """
        userImage = request.get_json()['image']

        classes_result = visual_recognition.classify(url=userImage).get_result()
        print(classes_result)
        result = json.dumps(classes_result, indent=2)
        response = make_response(result, 200)
        print(result)
        return response




