import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/sync")

layout = dbc.Container([
    dbc.Card([
        dbc.CardHeader(html.H4("Plaid Account Sync")),
        dbc.CardBody([
            html.P("Last synced: 2 hours ago"),
            dbc.Button("🔄 Sync Now", id="sync-button", color="primary", className="mb-3"),
            dcc.Loading(id="sync-loading", type="circle", children=html.Div(id="sync-status")),
            html.Hr(),
            html.H5("Linked Institutions"),
            html.Ul([
                html.Li("🏦 Chase Bank"),
                html.Li("💳 Capital One"),
                html.Li("🏠 Ally Mortgage")
            ])
        ])
    ])
], fluid=True)


@callback(
    Output("sync-status", "children"),
    Input("sync-button", "n_clicks")
)
def perform_sync(n_clicks):
    if n_clicks:
        return html.P("✅ Sync completed successfully!", className="text-success")
    return ""
