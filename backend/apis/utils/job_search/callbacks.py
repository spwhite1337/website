import pandas as pd
import plotly.express as px

from apis.utils.job_search.utils import params


def time_series(df: pd.DataFrame, color: str):
    df = df.sort_values('Date', ascending=True).reset_index(drop=True)
    if color == 'All':
        df['count'] = df.index
        return px.line(df, x='Date', y='count')
    df['count'] = df.assign(count=1).groupby(color)['count'].cumsum()
    df = df[~df[color].isna()]
    return px.line(df, x='Date', y='count', color=color)


def map_figure(df: pd.DataFrame, color: str):
    df = df[~df['Latitude'].isna() & ~df['Longitude'].isna()]
    return px.scatter_geo(df, lat='Latitude', lon='Longitude', color=color)


class PlotCallbacks(object):
    @staticmethod
    def figures(df, color):
        df = pd.read_json(df)
        if df.shape[0] == 0:
            return params['empty-figure'], params['empty-figure']
        t_fig = time_series(df, color)
        m_fig = map_figure(df, color)
        return t_fig, m_fig
