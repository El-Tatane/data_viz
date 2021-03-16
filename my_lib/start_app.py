import dash
import dash_bootstrap_components as dbc


external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def start_app(layout):

    app.layout = layout
    app.run_server(debug=True, use_reloader=True, host="0.0.0.0")
    return app