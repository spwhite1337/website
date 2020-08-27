import pandas as pd
import plotly.express as px

from apis.utils.job_search.utils import params


class PlotCallbacks(object):
    @staticmethod
    def figures(df, color):
        df = pd.read_json(df)
        if df.shape[0] == 0:
            return params['empty-figure'], params['empty-figure']
        t_fig = px.line(df, x='Date', y='Company', color=color)
        return t_fig, t_fig
