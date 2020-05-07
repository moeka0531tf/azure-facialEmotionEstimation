# image, videoファイルの処理についての関数
import os
from os.path import join

from dotenv import load_dotenv
from pathlib import Path
import cv2
import send2trash


def video2image(video_pass):

    IMAGE_PASS = './data/image'

    cap = cv2.VideoCapture(video_pass)
    file_name = os.path.basename(video_pass).split('.')[0]

    if not cap.isOpened():
        print('動画ファイルが読み込めません')
        return

    os.makedirs(IMAGE_PASS, exist_ok=True)

    # 総フレーム数 / fps で動画の秒数を取得
    # ファイルの桁数を取得
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    seconds = int(num_frames / fps)
    digit = len(str(seconds))

    # 1秒間隔で動画を切り出す
    num = 0
    for i in range(num_frames):
        ret, frame = cap.read()

        if i % int(fps) == 0:
            filled_second = str(num).zfill(digit)
            cv2.imwrite( os.path.join(IMAGE_PASS, "{}_{}.{}".format(file_name, filled_second, 'png')), frame)
            num += 1
    print('動画から画像を切り出しました')


def delete_image_file():

    IMAGE_PASS = './data/image'
    send2trash.send2trash(IMAGE_PASS)


# MEMO: 試験的に実行するための仮置きmain
# TODO: main.pyに組み込む際に消す
if __name__ == "__main__":

    # 環境変数の読み込み
    dotenv_path = join(Path(os.getcwd()).parent, '.env')
    load_dotenv(dotenv_path)

    VIDEO_PASS = os.environ.get("VIDEO_PASS")

    video2image(VIDEO_PASS)
    # delete_image_file()
