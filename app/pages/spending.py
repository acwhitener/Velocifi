import dash
from dash import html, dcc
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/spending")

layout = dbc.Container([
    dbc.Card([
        dbc.CardHeader(html.H4("Spending Breakdown")),
        dbc.CardBody([
            dcc.Graph(
                id="spending-pie",
                figure=go.Figure(
                    data=[
                        go.Pie(
                            labels=["Groceries", "Dining", "Rent", "Transport"],
                            values=[450, 320, 1500, 230],
                            hole=0.4,
                            marker=dict(colors=["#FFD700", "#8E44AD", "#4ADE80", "#3498DB"])
                        )
                    ],
                    layout=go.Layout(
                        title="Spending by Category",
                        paper_bgcolor="#0a0a0a",
                        font=dict(color="#f5f5f5")
                    )
                )
            )
        ])
    ])
], fluid=True)
