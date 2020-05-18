# image, videoファイルの処理についての関数
import glob
import os
from os.path import join

from dotenv import load_dotenv
from pathlib import Path
import cv2
import send2trash

import const

# TODO: 他のファイルでも使う際には変数用のファイルを作成する
os.makedirs(const.IMAGE_PATH, exist_ok=True)

def video2image(video_file_path):

    # MEMO: ディレクト内に複数mp4が存在する場合は一番最初に取得したものを使用する
    video_file = glob.glob(video_file_path)[0]
    cap = cv2.VideoCapture(video_file)
    file_name = os.path.basename(video_file).split('.')[0]

    if not cap.isOpened():
        print(os.path.abspath(video_file) + 'が読み込めません')
        return

    # 総フレーム数 / fps で動画の秒数を取得
    # ファイルの桁数を取得
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    seconds = int(num_frames / fps)
    digit = len(str(seconds))

    # 1秒間隔で動画を切り出す
    frame_second = 0
    for i in range(num_frames):
        ret, frame = cap.read()

        if i % int(fps) == 0:
            filled_second = str(frame_second).zfill(digit)
            create_file_name = "{}_{}.png".format(file_name, filled_second)
            create_file_path = os.path.join(const.IMAGE_PATH, create_file_name)
            cv2.imwrite(create_file_path, frame)
            frame_second += 1
    print('動画から画像を切り出しました')
    return frame_second, file_name;


def delete_image_file():

    send2trash.send2trash(const.IMAGE_PATH)


# MEMO: 試験的に実行するための仮置きmain
# TODO: main.pyに組み込む際に消す
if __name__ == "__main__":

    # 環境変数の読み込み
    dotenv_path = join(Path(os.getcwd()).parent, '.env')
    load_dotenv(dotenv_path)

    VIDEO_FILE_PATH = os.environ.get("VIDEO_FILE_PATH")

    num_frames = video2image(VIDEO_FILE_PATH)
    # delete_image_file()
