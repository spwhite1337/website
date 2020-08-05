import dash
import dash_html_components as html


def add_cc_dash(server, routes_pathname_prefix: str = '/api/dash/cardclassifier/'):
    """
    Add a
    """
    dashapp = dash.Dash(
        __name__,
        routes_pathname_prefix=routes_pathname_prefix,
        server=server
    )
    dashapp.layout = html.H1('Hi From Dash (card classifier)')

    return dashapp.server
