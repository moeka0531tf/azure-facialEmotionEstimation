import pandas as pd
import plotly.express as px


def shape_data(emotion_dict):

    # label,valueを取得しDataFrameへと整形
    label = [
        'anger',
        'contempt',
        'disgust',
        'fear',
        'happiness',
        'neutral',
        'sadness',
        'surprise'
    ]
    value = []

    for l in label:
        value.append(emotion_dict[l])

    df = pd.DataFrame(value, index=label, columns=['value'])
    print(df)

    return df, label, value


def draw(emotion_dict):
    df, label, value = shape_data(emotion_dict)

    # グラフ出力
    fig = px.bar(data_frame=df, x=label, y=value, color=label, width=640, height=360,
                 title='emotion value')
    fig.update_xaxes(title_text='emotion')
    fig.update_yaxes(title_text='score', range=[0, 1])
    fig.update_layout(showlegend=False, title_x=0.5)
    fig.show()
