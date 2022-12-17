import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from webscrapper import matches


def histogram_goal_plot(match_list, type):
    if type == 'goals_sum':
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=[int(i['final_goal_home']) for i in match_list], texttemplate="%{y}", name='HOME'))
        fig.add_trace(go.Histogram(x=[int(i['final_goal_away']) for i in match_list], texttemplate="%{y}", name='AWAY'))
        fig.update_layout(barmode='stack')
    else:
        fig = go.Figure(data=[go.Histogram(x=[int(i[type]) for i in match_list], texttemplate="%{y}")])

    fig.update_xaxes(categoryorder='category ascending')
    fig.update_layout(title_text=type, xaxis_title_text='Goals', yaxis_title_text='Count', bargap=0.2)
    return fig


app = dash.Dash()


app.layout = html.Div([
    html.H1(children='Matches statistic analysis'),
    dcc.Graph(figure=histogram_goal_plot(matches, 'final_goal_home')),
    dcc.Graph(figure=histogram_goal_plot(matches, 'final_goal_away')),
    dcc.Graph(figure=histogram_goal_plot(matches, 'goals_sum')),
    dcc.Graph(figure=histogram_goal_plot(matches, 'half_goal_home')),
    dcc.Graph(figure=histogram_goal_plot(matches, 'half_goal_away')),
])


if __name__ == '__main__':
    app.run_server()