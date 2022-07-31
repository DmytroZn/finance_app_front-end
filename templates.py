import dash_bootstrap_components as dbc
from dash import dash_table, html, dcc


PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

###########################################################################


sidebar = html.Div(
    [
        dbc.Offcanvas(
                dbc.ListGroup(
                    [
                        dbc.ListGroupItem(
                            "Button", id="button-item-1", n_clicks=0, action=True
                        ),
                        dbc.ListGroupItem(
                            "Button-2", id="button-item-2", n_clicks=0, action=True
                        ),
                        dbc.ListGroupItem(
                            "Button-3", id="button-item-3", n_clicks=0, action=True
                        ),
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
            dbc.Button("Open Offcanvas1", id="open-offcanvas", n_clicks=0),
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

content = html.Div(id='content')

table = dbc.Container([
    dash_table.DataTable(id='main-table')
])



table2 = html.Center([
    html.Table([
        html.Tbody([
            html.Tr([
                html.P('You have spent money already: '), html.Td(html.P(children="9 000", id='spent-money')),
            ]),
            html.Tr([
                html.P('You have money for spending: '), html.Td(html.P("6 000", id='have-money')),
            ]),
            html.Tr([
                html.P("You can spend today: "), html.Td(html.P("676,98", id='can-spend'))
            ])
        ])
    ])
])

# main = html.Div([navbar, sidebar, content, table2, table])
main = html.Div([navbar, sidebar, content])
