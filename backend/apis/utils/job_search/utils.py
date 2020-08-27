params = {
    'no-show': {'display': 'none'},
    'colors': [
        {'label': 'Field', 'value': 'Field'},
        {'label': 'State', 'value': 'State'},
        {'label': 'Era', 'value': 'Era'},
        {'label': 'Progress', 'value': 'Progress'},
    ],
    'empty-figure': {
        "layout": {
            "xaxis": {
                "visible": False
            },
            "yaxis": {
                "visible": False
            },
            "annotations": [
                {
                    "text": "No matching data found",
                    "xref": "paper",
                    "yref": "paper",
                    "showarrow": False,
                    "font": {
                        "size": 28
                    }
                }
            ]
        }
    }
}
