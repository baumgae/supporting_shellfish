from ibm_watson import VisualRecognitionV3

# Init Visual Recognition
visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='2u8IHpivxsV6Lf1vb08Pe8eCbWEb1FjlelRZ1xWLwKCC')

def predictMood(image):
    predicted_class = visual_recognition.detect_faces(url=image).get_result()
    return predicted_class
