from flask import Flask, request, render_template, make_response

import visual_recognition
import json


app = Flask(__name__)


# Get Route - Landing Page
@app.route('/')
def index():
    return render_template('index.html')


# Post Route - Receive advice from supporting shellfish
@app.route('/advice', methods=['POST'])
def advice():
    user_image = request.get_json()['image']
    classes_result = visual_recognition.predict_mood(user_image)
    result = json.dumps(classes_result, indent=2)
    response = make_response(result, 200)

    print(result)

    # Generate Advice?
    # return render_template('advice.html', predicted = result, advice = advice)
    return response


def main():
    """
        Main function for running the flask server.
    """
    app.config['SERVER_NAME'] = '0.0.0.0:5000'
    app.run(host='0.0.0.0', debug=True)


if __name__ == "__main__":
    main()
