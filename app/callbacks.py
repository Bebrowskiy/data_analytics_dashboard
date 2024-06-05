from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from app.server import app


def parse_contents(contents, filename):
    import base64
    import io
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        return html.Div([
            'There was an error processing this file.'
        ])

    return df


@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'))
def update_output(contents, filename):
    if contents is not None:
        df = parse_contents(contents, filename)
        return html.Div([
            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df.columns]
            ),
            dcc.Graph(
                figure=px.scatter(df, x=df.columns[0], y=df.columns[1])
            )
        ])


@app.callback(
    Output('graph', 'figure'),
    Input('output-data-upload', 'children'))
def update_graph(children):
    if children:
        data = children[0]['props']['data']
        df = pd.DataFrame(data)
        fig = px.scatter(df, x=df.columns[0], y=df.columns[1])
        return fig
    return {}
