import dash
from dash import html, dcc
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/cashflow")

layout = dbc.Container([
    dbc.Card([
        dbc.CardHeader(html.H4("Monthly Cash Flow")),
        dbc.CardBody([
            dcc.Graph(
                id="cashflow-chart",
                figure=go.Figure(
                    data=[
                        go.Bar(name="Income", x=["Jan", "Feb", "Mar"], y=[5000, 5200, 5300], marker_color="#00cc96"),
                        go.Bar(name="Expenses", x=["Jan", "Feb", "Mar"], y=[3200, 3500, 3400], marker_color="#EF553B"),
                    ],
                    layout=go.Layout(
                        barmode="group",
                        plot_bgcolor="#0a0a0a",
                        paper_bgcolor="#0a0a0a",
                        font=dict(color="#f5f5f5"),
                        title="Net Cash Flow by Month"
                    )
                )
            )
        ])
    ], className="mb-4 card")
], fluid=True)
