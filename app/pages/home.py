import dash
from dash import html

dash.register_page(__name__, path="/")

layout = html.Div(
    className="card",
    children=[
        html.H2("Welcome to Velocifi"),
        html.P("Your luxury personal finance dashboard, powered by Plaid, Python, and AI."),
        html.Div(className="gradient-text", children="Style meets financial clarity.")
    ]
)
