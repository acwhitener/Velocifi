from dash import Dash, html, dcc, page_container
import dash_bootstrap_components as dbc
import os

def init_dashboard(server):
    app = Dash(
        __name__,
        server=server,
        use_pages=True,
        routes_pathname_prefix="/",
        assets_folder=os.path.join(os.path.dirname(__file__), "assets")
    )

    app.title = "Velocifi Dashboard"

    app.layout = dbc.Container([
        # Navbar
        dbc.NavbarSimple(
            brand=html.Div([
                html.Img(
                    src="/assets/velocifi-logo.png",
                    height="30px",
                    className="glow-logo",
                    style={"marginRight": "10px"}
                ),
                html.Span("Velocifi", className="navbar-brand-text")
            ], style={"display": "flex", "alignItems": "center"}),
            brand_href="/",
            color="dark",
            dark=True,
            expand="lg",
            children=[
                dbc.NavItem(dcc.Link("Home", href="/", className="nav-link")),
                dbc.NavItem(dcc.Link("Transactions", href="/transactions", className="nav-link")),
                dbc.NavItem(dcc.Link("Cash Flow", href="/cashflow", className="nav-link")),
                dbc.NavItem(dcc.Link("Spending", href="/spending", className="nav-link")),
                dbc.NavItem(dcc.Link("Sync", href="/sync", className="nav-link")),
                dbc.NavItem(dcc.Link("Grocery", href="/grocery", className="nav-link")),
            ],
            className="mb-4"
        ),

        # Main page content
        html.Div(page_container, className="p-3")
    ], fluid=True)

    return app
