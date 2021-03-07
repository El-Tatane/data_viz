import dash_html_components as html
import dash_core_components as dcc
from .decorator import singleton
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from .referentiel import level_list, subject_list

DEFAULT_TARGET = "rating-number"


def to_html_div(figure_id):
    def wrapper_to_html_div(function):
        def modify_function(*args, **kwargs):
            fig = function(*args, **kwargs)
            if kwargs.get("to_html", False) is True:
                return html.Div([dcc.Graph(id=figure_id, figure=fig)])
            return fig

        return modify_function

    return wrapper_to_html_div


@singleton
class HTMLChart:
    def __init__(self, data_processing=None):
        self.data_processing = data_processing

    @to_html_div("time_bar")
    def get_time_bar_chart(self, time_type="year", analysis_target=DEFAULT_TARGET, data_filter_dict=None,
                           to_html=False):
        df = self.data_processing.get_bar_time_df(time_type, analysis_target, data_filter_dict)
        return px.bar(df, x=time_type, y=analysis_target)

    @to_html_div("parallel_coordinates")
    def get_parallel_coordinates(self, analysis_target=DEFAULT_TARGET, data_filter_dict=None, to_html=False):
        df = self.data_processing.get_parallel_coordinates_df(analysis_target, data_filter_dict)
        return px.parallel_coordinates(df,
                                       color=analysis_target,
                                       labels={"num_lectures": "Lecture number",
                                               "content_duration": "Content duration",
                                               "level": "level",
                                               "subject": "subject"},
                                       color_continuous_scale=px.colors.diverging.Tealrose,
                                       color_continuous_midpoint=2,
                                       range_color=[df[analysis_target].min(), df[analysis_target].max()]
                                       )

    @to_html_div("level_pie_chart")
    def get_level_pie_chart(self, data_filter_dict=None, to_html=False):
        df_filter = self.data_processing.get_level_pie_chart_df(data_filter_dict)
        return px.pie(df_filter, values='count', names='level',
                      title='Repartition level')

    @to_html_div("subject_pie_chart")
    def get_subject_pie_chart(self, data_filter_dict=None, to_html=False):
        df_filter = self.data_processing.get_subject_pie_chart_df(data_filter_dict)
        return px.pie(df_filter, values='count', names='subject',
                      title='Repartition subject')

    @to_html_div("target_histogram")
    def get_target_histogram(self, analysis_target=DEFAULT_TARGET, data_filter_dict=None, to_html=False):
        df_filter = self.data_processing.get_target_hist_df(analysis_target, data_filter_dict)
        return px.histogram(df_filter, x=analysis_target)

    @to_html_div("bubble_chart")
    def get_bubble_chart_histogram(self, analysis_target=DEFAULT_TARGET, category="level", data_filter_dict=None,
                                   to_html=False):
        df = self.data_processing.get_bubble_chart_histogram_df(analysis_target, category, data_filter_dict)
        return px.scatter(df, x="content_duration", y="num_lectures", size=analysis_target, color=category)


