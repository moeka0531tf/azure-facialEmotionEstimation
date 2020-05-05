import plotly.express as px
import data_preprocessing as dp

if __name__ == '__main__':

    df, label, value = dp.read_data()

    # グラフ出力
    fig = px.pie(data_frame=df, values=value, names=label, color=label, width=640, height=360,
                 title='emotion value')
    fig.update_layout(showlegend=True, title_x=0.5)
    fig.show()
