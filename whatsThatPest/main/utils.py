import os
import secrets
from PIL import Image
from flask import current_app
from watson_developer_cloud import VisualRecognitionV3
import json


def save_picture(bug_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(bug_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/bug_pics', picture_fn)

    i = Image.open(bug_picture)
    i.save(picture_path)

    return picture_fn

def bug_recognition(bug_image):
    visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        iam_apikey='KGSz0-fDoeCCyQQLQeWtfXro_RgjEa0PK44S5FPHNlU5')

    bug_path = os.path.join(current_app.root_path, 'static/bug_pics', bug_image)

    with open(bug_path, 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            threshold='0.6',
            classifier_ids='PestRecognitionModel_39839098').result

    try:
        return classes['images'][0]['classifiers'][0]['classes'][0]['class']
    except:
        return 'unknown'
