import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from .referentiel import *

class HTMLComponent:

    def __init__(self):
        pass

    def get_modal(self):
        return html.Div(
            [
                dbc.Button("Open modal", id="open"),
                dbc.Modal(
                    [
                        dbc.ModalHeader(html.H3("Filter data")),

                        dbc.ModalBody([
                            html.H5("Target analysis", style={"font-weight": "bold"}),

                            dcc.Dropdown(
                                id='analysis_target',
                                options=[{'label': value, 'value': key} for key, value in analysis_target_dict.items()],
                                value=list(analysis_target_dict.keys())[0],
                                placeholder=list(analysis_target_dict.values())[0]
                            ),

                            html.Br(),

                            html.H5("Other filter", style={"font-weight": "bold"}),

                            html.Div("Level :"),
                            dcc.Checklist(
                                id="filter_level",
                                options=[{'label': el, 'value': el} for el in level_list],
                                value=level_list,
                            ),
                            html.Div("Subject :"),
                            dcc.Checklist(
                                id="filter_subject",
                                options=[{'label': el, 'value': el} for el in subject_list],
                                value=subject_list
                            ),
                            html.Div("Time granularity :"),
                            dcc.Dropdown(
                                id='time_type',
                                options=[{'label': i, 'value': i} for i in time_granulation_list],
                                value=time_granulation_list[0]
                            ),
                       ]),

                        dbc.ModalFooter(
                            dbc.Button("Close", id="close", className="ml-auto")
                        ),
                    ],
                    id="modal",
                    size="lg",
                ),
            ]
        )

    def get_title(self):
        return html.H1("Dashboard for Udemy courses data", style={"textAlign": "center"})