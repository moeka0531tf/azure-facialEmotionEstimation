import plotly.express as px
import data_preprocessing as dp

if __name__ == '__main__':

    df, label, value = dp.read_data()

    # グラフ出力
    fig = px.bar(data_frame=df, x=label, y=value, color=label, width=640, height=360,
                 title='emotion value')
    fig.update_xaxes(title_text='emotion')
    fig.update_yaxes(title_text='score', range=[0, 1])
    fig.update_layout(showlegend=False, title_x=0.5)
    fig.show()
