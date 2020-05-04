import plotly.express as px
import pandas as pd
import json

if __name__ == '__main__':
    # jsonファイル読み込み
    json_file = open('sample.json', 'r')
    json_obj = json.load(json_file)

    # indexとvalueを取得し、DataFrameへと整形
    label = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
    value = []

    for i in label:
        value.append(json_obj[i])

    df = pd.DataFrame(value, index=label, columns=['value'])
    print(df)

    # グラフ出力
    fig = px.pie(data_frame=df, values=value, names=label, color=label, width=640, height=360,
                 title='emotion value')
    fig.update_layout(showlegend=True, title_x=0.5)
    fig.show()