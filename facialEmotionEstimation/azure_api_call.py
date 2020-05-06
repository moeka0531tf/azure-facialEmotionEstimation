import ast
import os
from os.path import join
from pathlib import Path

from azure.cognitiveservices.vision.face import FaceClient
from dotenv import load_dotenv
from msrest.authentication import CognitiveServicesCredentials

def prepare():

    # 環境変数の読み込み
    dotenv_path = join(Path(os.getcwd()).parent, '.env')
    load_dotenv(dotenv_path)

    FACE_SUBSCRIPTION_KEY = os.environ.get("FACE_SUBSCRIPTION_KEY")
    FACE_ENDPOINT = os.environ.get("FACE_ENDPOINT")

    # faceClientの作成
    return FaceClient(FACE_ENDPOINT, CognitiveServicesCredentials(FACE_SUBSCRIPTION_KEY))


def estimate_emotion(image_url, face_client):

    image_file_name = os.path.basename(image_url)
    detected_faces = face_client.face.detect_with_url(url=image_url, return_face_attributes=['emotion'])
    if not detected_faces:
        raise Exception('No face detected from image {}'.format(image_file_name))

    # MEMO1: azureのEmotionオブジェクト -> str -> dict型へ変換
    # MEMO2: image内には一人しか映っていない想定
    return ast.literal_eval(str(detected_faces[0].face_attributes.emotion))
