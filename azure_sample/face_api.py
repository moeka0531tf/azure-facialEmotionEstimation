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

if __name__ == "__main__":

    # 環境変数の読み込み
    dotenv_path = join(Path(os.getcwd()).parent, '.env')
    load_dotenv(dotenv_path)

    KEY = os.environ.get("FACE_SUBSCRIPTION_KEY")
    FACE_ENDPOINT = os.environ.get("FACE_ENDPOINT")
