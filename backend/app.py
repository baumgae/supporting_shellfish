from flask import Flask, request, render_template, make_response, jsonify
from flask_cors import CORS

import visual_recognition
import randomAdvice
import json
import logging
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)
# To enable logging for flask-cors,
app.logger.setLevel(logging.DEBUG)

CORS(app)

# Get Route - Landing Page
@app.route('/')
def index():
    return render_template('index.html')

# Post Route - Receive advice from supporting shellfish
@app.route('/advice', methods=['POST'])
def advice():
    try:
        image_json = json.dumps(request.get_json())
        data = json.loads(image_json)
        seperatingPosition = data['image'].find(',')
        image_bytes = data['image'][seperatingPosition+1:]

        im = Image.open(BytesIO(base64.b64decode(image_bytes)))
        im.save('temp.png','PNG')
        
        classes_result = visual_recognition.predict_mood('temp.png')
        result = json.dumps(classes_result, indent=2)
        app.logger.debug(result)
        
        emotion = visual_recognition.get_emotion_json(result)
        app.logger.debug(emotion)
        advice = randomAdvice.get_advice_on_emotion(emotion)
        app.logger.debug(advice)

        
        msg = jsonify({"emotion":emotion, "advice": advice})
        return make_response(msg, 200)
    except:
        user_image = None        
        msg = jsonify({"message": "bad-type"})
        return make_response(msg, 400)


def main():
    """
        Main function for running the flask server.
    """
    app.config['SERVER_NAME'] = '127.0.0.1:5000'
    app.run(host='127.0.0.1', debug=True)


if __name__ == "__main__":
    main()
