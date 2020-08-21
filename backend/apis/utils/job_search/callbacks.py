import os
import pandas as pd
import plotly.express as px

from config import Config


class DataCallbacks(object):
    @staticmethod
    def load():
        fn = os.path.join(Config.ROOT_DIR, 'backend', 'apis', 'utils', 'job_search', 'applications.csv')
        return pd.read_csv(fn)
