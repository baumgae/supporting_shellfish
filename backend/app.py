from flask import Flask, request, render_template, make_response
from flask_cors import CORS

import visual_recognition
import json
import logging
import base64

app = Flask(__name__)
# To enable logging for flask-cors,
# logging.getLogger('flask_cors').level = logging.DEBUG

# logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.DEBUG)

cors = CORS(app)

# Get Route - Landing Page
@app.route('/')
def index():
    return render_template('index.html')

# Post Route - Receive advice from supporting shellfish
@app.route('/advice', methods=['POST'])
def advice():
    user_image = request.get_json()
    user_image_decoded= base64.decodebytes(user_image)
    classes_result = visual_recognition.predict_mood(user_image_decoded)
    result = json.dumps(classes_result, indent=2)
    app.logger.debug('----------------')
    app.logger.debug(user_image)
    app.logger.debug(result)
    response = make_response(result, 200)
    # Generate Advice?
    # return render_template('advice.html', predicted = result, advice = advice)
    return redirect('/')
	

	
def main():
    """
        Main function for running the flask server.
    """
    app.config['SERVER_NAME'] = '0.0.0.0:5000'
    app.run(host='0.0.0.0', debug=True)


if __name__ == "__main__":
    main()
