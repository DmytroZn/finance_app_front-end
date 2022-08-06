import dash_bootstrap_components as dbc
from dash import dash_table, html, dcc


PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

###########################################################################

content = html.Div(id='content')


sidebar = html.Div(
    [
        dbc.Offcanvas(
                dbc.ListGroup(
                    [
                        dbc.ListGroupItem("Main page", id="button-item-1", n_clicks=0, action=True),
                        dbc.ListGroupItem("Category", id="button-item-2", n_clicks=0, action=True),
                        dbc.ListGroupItem("Settings", id="button-item-3", n_clicks=0, action=True),
                    ]
                ),
            id="offcanvas",
            title="Title",
            # scrollable=True,
            # backdrop=False,
            is_open=False,
        ),
    ]
)


navbar = dbc.Navbar(
    dbc.Container(
        [
            # dbc.NavbarToggler(id="open-offcanvas", n_clicks=0),
            dbc.Button("Menu", id="open-offcanvas", n_clicks=0),
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ms-2")),
                    ],
                    align="flex-start",
                    className="g-0",
                ),
                # href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
        ]
    ),
    color="dark",
    dark=True,
)


table = dbc.Container([
    dash_table.DataTable(id='main-table')
])


# spending_money = html.Center([
#     html.Br(),
#     html.Table([
#         html.Tbody([
#             html.Tr([
#                 html.P('You have spent money already: '), html.Td(html.P(children="9 000", id='spent-money')),
#             ]),
#             html.Tr([
#                 html.P('You have money for spending: '), html.Td(html.P("6 000", id='have-money')),
#             ]),
#             html.Tr([
#                 html.P("You can spend today: "), html.Td(html.P("676,98", id='can-spend'))
#             ])
#         ])
#     ])
# ])

spending_money = html.Center(html.Div(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col([html.P('You have spent money already: '), html.P(children="9 000", id='spent-money')] ),
                # dbc.Col([html.P(children="9 000", id='spent-money')] ),
            ]
        ),

        dbc.Row(
            [
                dbc.Col([html.P('You have money for spending: '), html.P("6 000", id='have-money')] ),
                # dbc.Col([html.P("6 000", id='have-money')] ),
            ]
        ),

        dbc.Row(
            [
                dbc.Col([html.P('You can spend today: '), html.P("676,98", id='can-spend')] ),
                # dbc.Col([html.P("676,98", id='can-spend')] ),
            ]
        ),

    ], style={'padding-right': '1em'}
))



# add_spending = html.Div([
#     html.Center([
#         html.Table([
#             html.Tbody([
#                 html.Tr([
#                     (dbc.Input(id="input-money", value='sdf', placeholder="", type="number", min=0, max=15_000_000, style={'width': '150px'})),
#                     html.Td(dcc.Dropdown(id='dropdown-categories', style={'width': '155px'})),
#                 ]),
#             ]),
#         ]),
#         html.Br(),
#         dbc.Container(dbc.Textarea(id="textarea-comment", rows=2, style={'width': '300px'})),
#     ]),
#     html.Center(dbc.Button("Submit", id='button-add', n_clicks=0, color="primary"), style={"display": "right"})
#
# ])

add_spending = html.Center(html.Div(
    [
        dbc.Row(
            html.Center(
                dbc.Col(
                    dbc.Input(id="input-money", value='sdf', placeholder="", type="number", min=0, max=15_000_000,
                              style={'width': '150px'}),
                ),
            )
        ),
        html.Br(),
        dbc.Row(
            html.Center(
                dbc.Col(
                    dcc.Dropdown(id='dropdown-categories', style={'width': '155px', 'text-align': 'center'}),
                ),
            )
        ),
        html.Br(),
        dbc.Row(
            html.Center(
                dbc.Col(
                    dbc.Textarea(id="textarea-comment", rows=2, style={'width': '300px'}),
                )
            )
        ),
        html.Br(),
        dbc.Row(
            html.Center(
                dbc.Col(
                    dbc.Button("Submit", id='button-add', n_clicks=0, color="primary"),
                )
            )
        ),
        html.Br(),
    ], style={'padding-right': '1em'}
))



main = html.Div([navbar, sidebar, content])
