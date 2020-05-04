import asyncio
import io
import glob
import os
from os.path import join
import sys
import time
import uuid
import requests
from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType

# 感情値の出力
def getEmotion(faceDictionary):
    print(faceDictionary.face_attributes.emotion)


if __name__ == "__main__":

    # 環境変数の読み込み
    dotenv_path = join(Path(os.getcwd()).parent, '.env')
    load_dotenv(dotenv_path)

    KEY = os.environ.get("FACE_SUBSCRIPTION_KEY")
    FACE_ENDPOINT = os.environ.get("FACE_ENDPOINT")

    # faceClientの作成
    face_client = FaceClient(FACE_ENDPOINT, CognitiveServicesCredentials(KEY))

    # 顔の向きを取得する
    image_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
    image_name = os.path.basename(image_url) # os.path.name -> 拡張子を含むファイル名を取得
    detected_faces = face_client.face.detect_with_url(url=image_url, return_face_attributes=['emotion'])
    if not detected_faces:
        raise Exception('No face detected from image {}'.format(image_name))

    for face in detected_faces:
        getEmotion(face)
