import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='2u8IHpivxsV6Lf1vb08Pe8eCbWEb1FjlelRZ1xWLwKCC')

url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/KnapperAlpakkaCorazonFull.jpg/300px-KnapperAlpakkaCorazonFull.jpg'

classes_result = visual_recognition.classify(url=url).get_result()
print(json.dumps(classes_result, indent=2))