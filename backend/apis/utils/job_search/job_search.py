import os
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

from apis.utils.job_search.utils import params
from apis.utils.job_search.callbacks import PlotCallbacks
from config import Config, logger


def add_js_dash(server, routes_pathname_prefix: str = '/api/dash/jobsearch'):
    """
    Add a mini-dashboard for job search data display
    """
    dashapp = dash.Dash(
        __name__,
        routes_pathname_prefix=routes_pathname_prefix,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        server=server
    )

    dashapp.layout = html.Div(children=[
        html.Div(id='app-data',
                 style=params['no-show'],
                 children=pd.read_csv(
                     os.path.join(Config.ROOT_DIR, 'backend', 'apis', 'utils', 'job_search', 'applications.csv')
                 )).to_json(),
        html.H1('Job Search Dash'),
        dcc.Dropdown(id='color-select', options=params['colors'], value=params['colors'][0]['value'],
                     placeholder='Select Coloring Field'),
        # Time series
        dcc.Graph(id='time-figure'),
        html.Br(),
        # Map plot
        dcc.Graph(id='map-figure')
    ])

    @dashapp.callback(
        [
            Output('time-figure', 'figure'),
            Output('map-figure', 'figure')
        ],
        [
            Input('app-data', 'children'),
            Input('color-select', 'value'),
        ]
    )
    def color_plots(df, color):
        return PlotCallbacks.figures(df, color)

    return dashapp.server
