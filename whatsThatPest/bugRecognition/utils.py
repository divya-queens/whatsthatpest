import os
import secrets
from PIL import Image
from flask import current_app, url_for
# import json
# from watson_developer_cloud import VisualRecognitionV3


def save_picture(bug_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(bug_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/bug_pics', picture_fn)

    i = Image.open(bug_picture)
    i.save(picture_path)

    return picture_fn


# visual_recognition = VisualRecognitionV3(
#     '2018-03-19',
#     iam_apikey='KGSz0-fDoeCCyQQLQeWtfXro_RgjEa0PK44S5FPHNlU5')


# with open('/home/divya/divya-queens/analytics-and-ai/dev-ai/comm493_whatsThatPest/whatsThatPest/static/bug_pics/lady.jpg', 'rb') as images_file:
#     classes = visual_recognition.classify(
#         images_file,
#         threshold='0.6',
# 	classifier_ids='PestRecognitionModel_39839098').get_result()
# print(json.dumps(classes, indent=2))