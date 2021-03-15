import my_lib

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

# from my_lib.update import *


if __name__ == '__main__':

    layout = html.Div([

        # html.H1("Dashboard for Udemy courses data", style={"textAlign": "center"}),


        dbc.Row([dbc.Col(html.P("A single, half-width column")),
                dbc.Col(html.P("SUite ede ma présentaiton"))]
                ),

        # dbc.Card(
        #     dbc.CardBody(
        #         [
        #             html.H5("Filter", className="card-title"),
        #
        #             dcc.Checklist(
        #                 id="filter_level",
        #                 options=[{'label': el, 'value': el} for el in my_lib.level_list],
        #                 value=my_lib.level_list
        #             ),
        #
        #
        #         ]
        #     )
        # , outline=True),
        #
        # dcc.Dropdown(
        #     id='analysis_target',
        #     options=[{'label': value, 'value': key} for key, value in my_lib.analysis_target_dict.items()],
        #     value=list(my_lib.analysis_target_dict.keys())[0],
        #     placeholder=list(my_lib.analysis_target_dict.values())[0]
        # ),
        #
        #
        # dcc.Checklist(
        #     id="filter_subject",
        #     options=[{'label': el, 'value': el} for el in my_lib.subject_list],
        #     value=my_lib.subject_list
        # ),
        # dcc.Dropdown(
        #     id='time_type',
        #     options=[{'label': i, 'value': i} for i in my_lib.time_granulation_list],
        #     value=my_lib.time_granulation_list[0]
        # ),
        #
        # my_lib.chart.get_time_bar_chart(to_html=True),
        # my_lib.chart.get_parallel_coordinates(to_html=True),
        # my_lib.chart.get_level_pie_chart(to_html=True),
        # my_lib.chart.get_subject_pie_chart(to_html=True),
        # my_lib.chart.get_target_histogram(to_html=True),
        # my_lib.chart.get_bubble_chart_histogram(to_html=True),

    ])

    # app = my_lib.start_app(layout)


import dash


app = dash.Dash(__name__)
app.layout = layout
app.run_server(debug=True, use_reloader=True)





