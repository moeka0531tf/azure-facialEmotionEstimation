import plotly.express as px
import pandas as pd
import json

if __name__ == '__main__':
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

    # グラフ出力
    fig = px.bar(data_frame=df, x=label, y=value, color=label, width=640, height=360,
                 title='emotion value')
    fig.update_xaxes(title_text='emotion')
    fig.update_yaxes(title_text='score', range=[0, 1])
    fig.update_layout(showlegend=False, title_x=0.5)
    fig.show()