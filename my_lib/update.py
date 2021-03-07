import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from .start_app import app
from .HTMLChart import HTMLChart
from . import chart


assert chart.data_processing is not None


def fill_data_filter_dict(**kwargs):
    data_filter_dict = {}
    if "filter_level" in kwargs:
        data_filter_dict["level"] = kwargs.pop("filter_level")
    if "filter_subject" in kwargs:
        data_filter_dict["subject"] = kwargs.pop("filter_subject")

    assert len(kwargs) == 0, f"Problems filter not empty at end: {kwargs}"
    return data_filter_dict


@app.callback(
    Output('time_bar', 'figure'),
    Input('time_type', 'value'),
    Input('analysis_target', 'value'),
    Input("filter_level", 'value'),
    Input("filter_subject", 'value'),
)
def update_time(time_type, analysis_target, filter_level, filter_subject):
    data_filter_dict = fill_data_filter_dict(filter_level=filter_level, filter_subject=filter_subject)
    return chart.get_time_bar_chart(time_type, analysis_target, data_filter_dict)


@app.callback(
    Output('parallel_coordinates', 'figure'),
    Input('analysis_target', 'value'),
    Input("filter_level", 'value'),
    Input("filter_subject", 'value'),
)
def update_parallel_coordinates(analysis_target, filter_level, filter_subject):
    data_filter_dict = fill_data_filter_dict(filter_level=filter_level, filter_subject=filter_subject)
    return chart.get_parallel_coordinates(analysis_target, data_filter_dict)


@app.callback(
    Output('target_histogram', 'figure'),
    Input('analysis_target', 'value'),
    Input("filter_level", 'value'),
    Input("filter_subject", 'value'),
)
def update_target_histogram(analysis_target, filter_level, filter_subject):
    data_filter_dict = fill_data_filter_dict(filter_level=filter_level, filter_subject=filter_subject)
    return chart.get_target_histogram(analysis_target, data_filter_dict)


@app.callback(
    Output('bubble_chart', 'figure'),
    Input('analysis_target', 'value'),
    Input("filter_level", 'value'),
    Input("filter_subject", 'value'),
)
def update_bubble_chart(analysis_target, filter_level, filter_subject, category="level"):
    data_filter_dict = fill_data_filter_dict(filter_level=filter_level, filter_subject=filter_subject)
    return chart.get_bubble_chart_histogram(analysis_target, category, data_filter_dict)


@app.callback(
    Output('level_pie_chart', 'figure'),
    Input("filter_level", 'value'),
    Input("filter_subject", 'value'),
)
def update_level_pie_chart(filter_level, filter_subject):
    data_filter_dict = fill_data_filter_dict(filter_level=filter_level, filter_subject=filter_subject)
    return chart.get_level_pie_chart(data_filter_dict)
