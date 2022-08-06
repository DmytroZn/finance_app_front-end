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

spending_money = html.Center(html.Div(
    [
        html.Br(),
        dbc.Row(
            [
                dbc.Col([html.P('You have spent money already: '), html.P(children="9 000", id='spent-money')] ),
            ]
        ),

        dbc.Row(
            [
                dbc.Col([html.P('You have money for spending: '), html.P("6 000", id='have-money')] ),
            ]
        ),

        dbc.Row(
            [
                dbc.Col([html.P('You can spend today: '), html.P("676,98", id='can-spend')] ),
            ]
        ),

    ], style={'padding-right': '1em'}
))

add_spending = html.Center(html.Div(
    [
        dbc.Row(
            dbc.Col(
                dbc.Input(id="input-money", placeholder="", type="number", min=0, max=15_000_000,
                          style={'width': '150px'}),
            ),
        ),
        html.Br(),
        dbc.Row(
            dbc.Col(
                dcc.Dropdown(id='dropdown-categories', style={'width': '155px', 'text-align': 'center'}),
            ),
        ),
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Textarea(id="textarea-comment", rows=2, style={'width': '300px'}),
            )
        ),
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Button("Submit", id='button-add', n_clicks=0, color="primary"),
            )
        ),
        html.Br(),
    ], style={'padding-right': '1em'}
))


sing_in = html.Center(html.Div(
    [
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Input(id="input-username-sing-in", placeholder="username", type="text", style={'width': '150px'}),
            ),
        ),
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Input(id="input-password-sing-in", placeholder="password", type="password", style={'width': '150px'}),
            ),
        ),
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Button("Singin", id='button-sing-in', n_clicks=0, color="primary"),
            )
        ),
        html.Br(),

    ]
))


sing_up = html.Center(html.Div(
    [
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Input(id="input-username-sing-up", placeholder="username", type="text", style={'width': '150px'}),
            ),
        ),
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Input(id="input-firstname", placeholder="First name", type="text", style={'width': '150px'}),
            ),
        ),
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Input(id="input-lastname", placeholder="Last name", type="text", style={'width': '150px'}),
            ),
        ),
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Input(id="input-email", placeholder="Email", type="email", style={'width': '150px'}),
            ),
        ),
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Input(id="input-password-sing-up", placeholder="password", type="password", style={'width': '150px'}),
            ),
        ),
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Input(id="input-re-password-sing-up", placeholder="again password", type="password", style={'width': '150px'}),
            ),
        ),
        html.Br(),
        dbc.Row(
            dbc.Col(
                dbc.Button("Singup", id='button-sing-up', n_clicks=0, color="primary"),
            )
        ),
        html.Br(),

    ]
))


main = html.Div([navbar, sidebar, content, sing_up])
