import my_lib

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from my_lib.update import *
from my_lib import components







if __name__ == '__main__':
    pass

    layout = html.Div([

        components.get_title(),
        components.get_modal(),




        # dbc.Row(
        #     [dbc.Col(
        #          dbc.Card(
        #                 dbc.CardBody(
        #                     [
        #                         html.H5("Filter", className="card-title"),
        #
        #
        #
        #
        #                     ]
        #                 )
        #             , outline=True),
        #         width=3)
        #     ]
        # ),






        my_lib.chart.get_time_bar_chart(to_html=True),
        my_lib.chart.get_parallel_coordinates(to_html=True),
        my_lib.chart.get_level_pie_chart(to_html=True),
        my_lib.chart.get_subject_pie_chart(to_html=True),
        my_lib.chart.get_target_histogram(to_html=True),
        my_lib.chart.get_bubble_chart_histogram(to_html=True),

    ])

    app = my_lib.start_app(layout)


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True, host="0.0.0.0")



