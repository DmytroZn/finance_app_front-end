import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
import dash
from flask import Flask, session
from dash import html, dcc

from templates import *

server = Flask(__name__)
server.config['SECRET_KEY'] = 'super secret key'


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])
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



# @app.callback(
#     [
#      # Output("button-sing-in2", "children"),
#      # Output("button-sing-up2", "children"),
#      Output('content2', 'children'),
#      Output('button-sidebar', 'children'),
#      ],
#     [Input("start-page", "children"),
#      # Input('button-sing-in2', 'n_clicks'),
#      # Input('button-sing-up2', 'n_clicks'),
#      Input('button-singup-page', 'n_clicks'),
#      Input('button-singin-page', 'n_clicks')
#      ]
# )
# def start_page(a, b=0, c=0):
#     print('sf d d d d d ')
#     if not session.get('token'):
#         ctx = dash.callback_context
#         button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#         if button_id == 'button-singup-page':
#             return sing_in, ''
#         elif button_id == 'button-singin-page':
#             return sing_up, ''
#         else:
#             print(button_id)
#             return sing_in, ''
#     else:
#         return '', button_sidebar\

@app.callback(
    [
     Output('button-sing', 'value'),
     Output('button-sing', 'children'),
     Output('content', 'children'),
     Output('button-sidebar', 'children'),
     ],
    [
        Input('button-sing', 'value'),
        Input('button-sing', 'n_clicks'),

     Input('button-item-1', 'n_clicks'),
     Input('button-item-2', 'n_clicks'),

    ]
)
def start_page(value, b, c, d):
    print('sf d d d d d ', value, session.get('token'))
    if not session.get('token'):
        if value == 'sing_in':
            return 'sing_up', 'sing up', sing_in, ''
        elif value == 'sing_up':
            return 'sing_in', 'sing in', sing_up, ''
        else:
            return 'sing_up', 'sing up', sing_in, ''
    elif session.get('token'):

        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == "button-item-1":
            return 'sing_out', 'sing out', [spending_money, add_spending], button_sidebar
        elif button_id == "button-item-2":
            return 'sing_out', 'sing out', 'TEST BUTT 2', button_sidebar
        # return ([spending_money, add_spending],)
        if value == 'sing_out':
            del session['token']
            return 'sing_up', 'sing up', sing_in, ''

        return 'sing_out', 'sing out', '', button_sidebar


# @app.callback(
#     [Output('button-sing', 'value'),
#     Output('button-sing', 'children'),
#      Output('content2', 'children'),
#      Output('button-sidebar', 'children'),
#      ],
#     Input('button-sing', 'value'),
# )
# def sign_out(a):
#     del session['token']
#     return 'sing_up', 'sing up', sing_in, ''


@app.callback(
    Output('button-sing-in', 'n_click'),
    Input('button-sing-in', 'n_clicks'),
    [State('input-username-sing-in', 'value'),
     State('input-password-sing-in', 'value')]

)
def sign_in(a, b, c):
    print('done')
    session['token'] = b
    return ''



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


@app.callback(
    Output('demo-dropdown', 'data'),
    [Input('button-item-3', 'n_clicks'), Input('button-item-3', 'n_clicks')]
)
@dec
def dropdown_catorories():
    options = [
                  {'label': 'New York City', 'value': 'NYC'},
                  {'label': 'Montreal', 'value': 'MTL'},
                  {'label': 'San Francisco', 'value': 'SF'},
              ],

    return options


@app.callback(
    [Output('spent-money', 'children'),
     Output('have-money', 'children'),
     Output('can-spend', 'children')],
    [Input('button-item-1', 'n_clicks'), ]
)
@dec
def get_spending_money(_):
    return "33", 55, 66


@app.callback(
    [Output('dropdown-categories', 'options'),
     Output('dropdown-categories', 'placeholder')],
    [Input('button-item-1', 'n_clicks'), ]
)
@dec
def get_dropdown_categories(r):
    options = [
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'},
    ]
    return options, 'Choose category'


@app.callback(
    [Output('button-add', 'options')],
    [Input('button-add', 'n_clicks'), ],
    [State('input-money', 'value'),
     State('dropdown-categories', 'value'),
     State('textarea-comment', 'value')]
)
@dec
def adding_spending(a, b, c, d):
    return ('sd',)


# @app.callback(
#     [Output('content', 'children')],
#     [Input('button-item-1', 'n_clicks'),
#      Input('button-item-2', 'n_clicks')
#      ],
# )
# @dec
# def change_page(_, __):
#     ctx = dash.callback_context
#     button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#     if button_id == "button-item-1":
#         return ([spending_money, add_spending],)
#     elif button_id == "button-item-2":
#         return ('TEST BUTT 2',)
#     # return ([spending_money, add_spending],)
#     return ('',)



# ____________________________________________________________________________________________________

if __name__ == '__main__':
    app.run_server(debug=False)
