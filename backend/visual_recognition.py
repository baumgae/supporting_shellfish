from ibm_watson import VisualRecognitionV3
import json

# Init Visual Recognition
visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='2u8IHpivxsV6Lf1vb08Pe8eCbWEb1FjlelRZ1xWLwKCC')


def predict_mood():
    with open('temp.png', 'rb') as images_file:
        predicted_class = visual_recognition.detect_faces(images_file).get_result()
    return predicted_class
