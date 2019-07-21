from ibm_watson import VisualRecognitionV3
import json

# Init Visual Recognition
visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='2u8IHpivxsV6Lf1vb08Pe8eCbWEb1FjlelRZ1xWLwKCC')


def predict_mood(image):
    with open(image, 'rb') as images_file:
        predicted_class = visual_recognition.classify(
            images_file,
            threshold='0.6',
            classifier_ids='DefaultCustomModel_1997094634').get_result()
    return predicted_class

def get_emotion_json(result_of_image):
    data = json.loads(result_of_image)
    first_dict = data['images']
    first_list = first_dict[0]
    second_dict = first_list['classifiers']
    second_list = second_dict[0]
    third_dict = second_list['classes']
    third_list = third_dict[0]
    emotion = third_list['class']
    return emotion
