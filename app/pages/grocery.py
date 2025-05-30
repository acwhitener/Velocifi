import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/grocery")

layout = dbc.Container([
    dbc.Card([
        dbc.CardHeader(html.H4("Smart Grocery Inventory")),
        dbc.CardBody([
            html.P("This page will track ingredients, grocery SKUs, and build smart shopping lists."),
            html.Ul([
                html.Li("✅ Inventory-based meal planning"),
                html.Li("🛒 Auto-generated shopping lists"),
                html.Li("💡 Smart meal SKUs based on favorite recipes")
            ]),
            html.P("Coming soon..."),
        ])
    ])
], fluid=True)
