import pandas as pd
import json

def read_data():
    # jsonファイル読み込み
    json_file = open('sample.json', 'r')
    json_obj = json.load(json_file)


    # label,valueを取得しDataFrameへと整形
    label = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
    value = []

    for i in label:
        value.append(json_obj[i])

    df = pd.DataFrame(value, index=label, columns=['value'])
    print(df)

    return df, label, value