import random
import json

with open('util/advices.json') as json_file:
    advices = json.load(json_file)

def get_advice_on_emotion(emotion):
    get_advices = advices[emotion]
    random_advice = get_advices[random.randrange(len(get_advices))]
    return random_advice
