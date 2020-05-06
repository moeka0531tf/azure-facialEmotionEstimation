# 画像を取得し、AzureのAPIを叩く関数に渡す

import draw_graph
import azure_api_call as azurecall


if __name__ == "__main__":

    image_url = 'https://cdn.pixabay.com/photo/2015/09/02/13/24/girl-919048_960_720.jpg'

    face_client = azurecall.prepare()
    emotion_dict = azurecall.estimate_emotion(image_url, face_client)

    draw_graph.draw(emotion_dict)
