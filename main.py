import my_lib

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from my_lib.update import *
from my_lib.referentiel import *
from my_lib import components


if __name__ == "__main__":
    pass

    layout = html.Div(
        [
            components.get_title(),
            # button
            dbc.Row(
                [
                    dbc.Col(
                        components.get_modal(),
                        width={"offset": 11},
                    )
                ]
            ),
            # first line
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    [
                                        html.Span("Resume target : ", style={"font-weight": "bold"}),
                                        html.Span(id="name_target"),
                                    ]
                                ),
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            [
                                                html.Span("detail : ", style={"font-weight": "bold"}),
                                                html.P(id="detail_target"),
                                            ]
                                        ),
                                        html.Br(),
                                        html.Div(
                                            [
                                                html.Span("min : ", style={"font-weight": "bold"}),
                                                html.Span(id="min_target"),
                                            ]
                                        ),
                                        html.Div(
                                            [
                                                html.Span("max : ", style={"font-weight": "bold"}),
                                                html.Span(id="max_target"),
                                            ]
                                        ),
                                        html.Div(
                                            [
                                                html.Span("average : ", style={"font-weight": "bold"}),
                                                html.Span(id="mean_target"),
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        ),
                        width={"offset": 1, "size": 3},
                        style={"padding-top": "70px"},
                    ),
                    dbc.Col(my_lib.chart.get_level_pie_chart(to_html=True), width={"offset": 1, "size": 3}),
                    dbc.Col(my_lib.chart.get_subject_pie_chart(to_html=True), width=3),
                ]
            ),

            dbc.Row(dbc.Col(html.H5("Target repartition value and month"), width={"offset": 2, "size": 3})),
            dbc.Row([
                dbc.Col(
                    [
                        dcc.RadioItems(
                            id='xaxistype',
                            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                            value='Linear',
                            labelStyle={'display': 'inline-block'},
                            style={"padding-left": "100px"}
                        ),
                        my_lib.chart.get_target_histogram(to_html=True),
                     ], width={"offset": 1, "size": 5}, style={"margin-top": 45}),
                dbc.Col([
                    html.Div("Time granularity :", style={"text-decoration": "underline", 'margin': "5px"}),
                    dcc.Dropdown(
                        id='time_type',
                        options=[{'label': i, 'value': i} for i in time_granulation_list],
                        value=time_granulation_list[0]
                    ),
                    my_lib.chart.get_time_bar_chart(to_html=True)], width={"offset": 0, "size": 5})
            ]),

            dbc.Row([
                dbc.Col([
                    my_lib.chart.get_parallel_coordinates(to_html=True)
                ], width={"offset": 1, "size": 10}),
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Col(
                        dcc.Dropdown(
                            id='color_axis_level',
                            options=[{'label': el, 'value': el} for el in ["level", "subject"]],
                            value="level",
                        ), width={"offset": 1, "size": 3},
                    ),
                    my_lib.chart.get_bubble_chart_histogram(to_html=True),
                ], width={"offset": 1, "size": 10}),
            ]),
        ]
    )

    app = my_lib.start_app(layout)


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True, host="0.0.0.0")
