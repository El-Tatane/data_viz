import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from .start_app import app
from .HTMLChart import HTMLChart
from . import chart


assert chart.data_processing is not None

MAX = 9999999
ALL_FILTER = ["filter_level", "filter_subject", "filter_price_min", "filter_price_max", "filter_rating_min",
              "filter_rating_max", "filter_nb_sub_min", "filter_nb_sub_max"]


def fill_data_filter_dict(**kwargs_raw):
    kwargs = {k: v for k, v in kwargs_raw.items() if v is not None and v != ""}
    data_filter_dict = {}
    if "filter_level" in kwargs:
        data_filter_dict["level"] = kwargs.pop("filter_level")

    if "filter_subject" in kwargs:
        data_filter_dict["subject"] = kwargs.pop("filter_subject")

    if "filter_price_min" in kwargs:
        data_filter_dict["price_min"] = int(kwargs.pop("filter_price_min", 0))

    if "filter_price_max" in kwargs:
        data_filter_dict["price_max"] = int(kwargs.pop("filter_price_max", MAX))

    if "filter_rating_min" in kwargs:
        data_filter_dict["rating_min"] = int(kwargs.pop("filter_rating_min", 0))

    if "filter_rating_max" in kwargs:
        data_filter_dict["rating_max"] = int(kwargs.pop("filter_rating_max", MAX))

    if "filter_nb_sub_min" in kwargs:
        data_filter_dict["nb_sub_min"] = int(kwargs.pop("filter_nb_sub_min", 0))

    if "filter_nb_sub_max" in kwargs:
        data_filter_dict["nb_sub_max"] = int(kwargs.pop("filter_nb_sub_max", MAX))

    assert len(kwargs) == 0, f"Problems filter not empty at end: {kwargs}"
    return data_filter_dict


@app.callback(
    Output("time_bar", "figure"),
    Input("time_type", "value"),
    Input("analysis_target", "value"),
    Input("filter_level", "value"),
    Input("filter_subject", "value"),
    Input("filter_price_min", "value"),
    Input("filter_price_max", "value"),
    Input("filter_rating_min", "value"),
    Input("filter_rating_max", "value"),
    Input("filter_nb_sub_min", "value"),
    Input("filter_nb_sub_max", "value"),
)
def update_time(time_type, analysis_target, *args):
    kwargs = {name: value for name, value in zip(ALL_FILTER, args)}
    data_filter_dict = fill_data_filter_dict(**kwargs)
    return chart.get_time_bar_chart(time_type, analysis_target, data_filter_dict)


@app.callback(
    Output("parallel_coordinates", "figure"),
    Input("analysis_target", "value"),
    Input("filter_level", "value"),
    Input("filter_subject", "value"),
    Input("filter_price_min", "value"),
    Input("filter_price_max", "value"),
    Input("filter_rating_min", "value"),
    Input("filter_rating_max", "value"),
    Input("filter_nb_sub_min", "value"),
    Input("filter_nb_sub_max", "value"),
)
def update_parallel_coordinates(analysis_target, *args):
    kwargs = {name: value for name, value in zip(ALL_FILTER, args)}
    data_filter_dict = fill_data_filter_dict(**kwargs)
    return chart.get_parallel_coordinates(analysis_target, data_filter_dict)


@app.callback(
    Output("target_histogram", "figure"),
    Input("analysis_target", "value"),
    Input('xaxistype', 'value'),
    Input("filter_level", "value"),
    Input("filter_subject", "value"),
    Input("filter_price_min", "value"),
    Input("filter_price_max", "value"),
    Input("filter_rating_min", "value"),
    Input("filter_rating_max", "value"),
    Input("filter_nb_sub_min", "value"),
    Input("filter_nb_sub_max", "value"),
)
def update_target_histogram(analysis_target, xaxistype, *args):
    kwargs = {name: value for name, value in zip(ALL_FILTER, args)}
    data_filter_dict = fill_data_filter_dict(**kwargs)
    return chart.get_target_histogram(analysis_target, data_filter_dict, xaxistype=xaxistype)


@app.callback(
    Output("bubble_chart", "figure"),
    Input("analysis_target", "value"),
    Input("color_axis_level", "value"),
    Input("filter_level", "value"),
    Input("filter_subject", "value"),
    Input("filter_price_min", "value"),
    Input("filter_price_max", "value"),
    Input("filter_rating_min", "value"),
    Input("filter_rating_max", "value"),
    Input("filter_nb_sub_min", "value"),
    Input("filter_nb_sub_max", "value"),
)
def update_bubble_chart(analysis_target, color_axis_level, *args):
    kwargs = {name: value for name, value in zip(ALL_FILTER, args)}
    data_filter_dict = fill_data_filter_dict(**kwargs)
    return chart.get_bubble_chart_histogram(analysis_target, color_axis_level, data_filter_dict)


@app.callback(
    Output("level_pie_chart", "figure"),
    Input("filter_level", "value"),
    Input("filter_subject", "value"),
    Input("filter_price_min", "value"),
    Input("filter_price_max", "value"),
    Input("filter_rating_min", "value"),
    Input("filter_rating_max", "value"),
    Input("filter_nb_sub_min", "value"),
    Input("filter_nb_sub_max", "value"),
)
def update_level_pie_chart(*args):
    kwargs = {name: value for name, value in zip(ALL_FILTER, args)}
    data_filter_dict = fill_data_filter_dict(**kwargs)
    return chart.get_level_pie_chart(data_filter_dict)


# modal
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# Card
@app.callback(
    Output("min_target", "children"),
    Input("analysis_target", "value"),
    Input("filter_level", "value"),
    Input("filter_subject", "value"),
    Input("filter_price_min", "value"),
    Input("filter_price_max", "value"),
    Input("filter_rating_min", "value"),
    Input("filter_rating_max", "value"),
    Input("filter_nb_sub_min", "value"),
    Input("filter_nb_sub_max", "value"),
)
def card_min(analysis_target, *args):
    kwargs = {name: value for name, value in zip(ALL_FILTER, args)}
    data_filter_dict = fill_data_filter_dict(**kwargs)
    return chart.data_processing.get_resume_target(data_filter_dict, analysis_target, "min")


@app.callback(
    Output("max_target", "children"),
    Input("analysis_target", "value"),
    Input("filter_level", "value"),
    Input("filter_subject", "value"),
    Input("filter_price_min", "value"),
    Input("filter_price_max", "value"),
    Input("filter_rating_min", "value"),
    Input("filter_rating_max", "value"),
    Input("filter_nb_sub_min", "value"),
    Input("filter_nb_sub_max", "value"),
)
def card_max(analysis_target, *args):
    kwargs = {name: value for name, value in zip(ALL_FILTER, args)}
    data_filter_dict = fill_data_filter_dict(**kwargs)
    return chart.data_processing.get_resume_target(data_filter_dict, analysis_target, "max")


@app.callback(
    Output("mean_target", "children"),
    Input("analysis_target", "value"),
    Input("filter_level", "value"),
    Input("filter_subject", "value"),
    Input("filter_price_min", "value"),
    Input("filter_price_max", "value"),
    Input("filter_rating_min", "value"),
    Input("filter_rating_max", "value"),
    Input("filter_nb_sub_min", "value"),
    Input("filter_nb_sub_max", "value"),

)
def card_mean(analysis_target, *args):
    kwargs = {name: value for name, value in zip(ALL_FILTER, args)}
    data_filter_dict = fill_data_filter_dict(**kwargs)
    return round(chart.data_processing.get_resume_target(data_filter_dict, analysis_target, "mean"), 2)


@app.callback(
    Output("detail_target", "children"),
    Input("analysis_target", "value"),
)
def card_detail(analysis_target):
    ref = {
        "rating-number": "number of stars between 0 and 5, some course don't have score, "
        "they were removed for this filter",
        "num_subscribers": "number of people who subscribe to this courses (free or not)",
        "total_earn": "number total of dollars earn (price * number subscribers)",
    }
    return ref[analysis_target]
