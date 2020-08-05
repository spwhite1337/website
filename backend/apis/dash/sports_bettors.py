import dash
import dash_html_components as html

dashapp = dash.Dash(
    __name__,
    requests_pathname_prefix='/api/dash/'
)

dashapp.layout = html.Div(id='example-div')

if __name__ == '__main__':
    dashapp.run_server(debug=True, host='127.0.0.1', port=5000)
