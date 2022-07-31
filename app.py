import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
import dash
from dash import html, dcc

from templates import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"


def dec(func):
    def wrap(*args, **kwargs):
        print(args, kwargs)
        return func(*args, **kwargs)
    return wrap

# ____________________________________________________________________________________________________



app.layout = main


@app.callback(
    Output("offcanvas", "is_open"),
    Input("button-item-1", "n_clicks"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
@dec
def toggle_offcanvas1(n1, n2, is_open):
    ctx = dash.callback_context
    dropdown_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(dropdown_id)
    if dropdown_id == "button-item-1":
        return False
    return True


@app.callback(Output('main-table', 'data'),
              [Input('button-item-2', 'n_clicks'), Input('button-item-3', 'n_clicks')])
@dec
def update_graphs(n2, n3):
    ctx = dash.callback_context
    dropdown_id = ctx.triggered[0]['prop_id'].split('.')[0]

    d2 = [{"name": "sdf", "id": "sdfsf"},
         {"name": "sdf", "id": "sdfsf"},
         {"name": "sdf", "id": "sdfsf"},
         {"name": "sdf", "id": "sdfsf"}, ]

    d3 = [{"name": "sdf", "id": "sdfsf"}, ]

    if dropdown_id == "button-item-2":
        return d2
    elif dropdown_id == "button-item-3":
        return d3
    return [{"name": "", "id": ""}, ]


# @app.callback(
#     [Output('spent-money', 'children'),
#     Output('have-money', 'children'),
#     Output('can-spend', 'children')],
#     [Input('button-item-1', 'n_clicks')]
# )
# def calculate_spending(n):
#     ctx = dash.callback_context
#     dropdown_id = ctx.triggered[0]['prop_id'].split('.')[0]
#     if dropdown_id == "button-item-1":
#         return '1', '2', '3'


@app.callback(
    [Output('content', 'children')],
    [Input('button-item-1', 'n_clicks'),
    Input('button-item-2', 'n_clicks')
     ],
)
@dec
def change_page(n1, n2):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "button-item-1":
        return (table2,)
    elif button_id == "button-item-2":
        return ('TEST BUTT 2',)
    return ('sdf',)



# ____________________________________________________________________________________________________

if __name__ == '__main__':
    app.run_server(debug=False)
