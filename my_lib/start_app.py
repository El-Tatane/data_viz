import dash


app = dash.Dash(__name__)


def start_app(layout):

    app.layout = layout

    app.run_server(debug=True, use_reloader=True)
    return app