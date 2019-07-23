import visual_recognition
import json
import random

local_image = 'kevin.jpg'

with open('util/advices.json') as json_file:
    advices = json.load(json_file)


def predict_image(image):
    classes_result = visual_recognition.predict_mood(image)
    result = json.dumps(classes_result, indent=2)
    return result


def predict_mood(image):
    with open(image, 'rb') as images_file:
        predicted_class = visual_recognition.classify(
            images_file,
            threshold='0.6',
            classifier_ids='DefaultCustomModel_1997094634').get_result()



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


def get_advice_on_emotion(emotion):
    get_advices = advices[emotion]
    random_advice = get_advices[random.randrange(len(get_advices))]
    return random_advice


if __name__ == "__main__":
    result_ = predict_image(local_image)
    emotion_ = get_emotion_json(result_)
    a = get_advice_on_emotion(emotion_)
    print(a)

