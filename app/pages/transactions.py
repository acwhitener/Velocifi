import dash
from dash import html, dcc, dash_table, callback, Output, Input
import pandas as pd
from backend.database.models import Transaction

dash.register_page(__name__, path="/transactions")

layout = html.Div(
    className="card",
    children=[
        html.H2("Transactions"),
        dcc.Loading(
            id="loading-transactions",
            type="circle",
            children=html.Div(id="transactions-table-container")
        )
    ]
)

@callback(
    Output("transactions-table-container", "children"),
    Input("url", "pathname")
)
def update_transactions(_):
    transactions = Transaction.query.order_by(Transaction.date.desc()).limit(100).all()
    if not transactions:
        return html.P("No transactions found.")

    df = pd.DataFrame([{
        "Date": t.date.strftime("%Y-%m-%d"),
        "Name": t.name,
        "Category": t.category,
        "Amount": f"${t.amount:.2f}"
    } for t in transactions])

    return dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        page_size=20,
        sort_action="native",
        filter_action="native",
        style_table={"overflowX": "auto"},
        style_cell={"backgroundColor": "#121212", "color": "#f5f5f5"},
        style_header={"backgroundColor": "#1a1a1a", "color": "#FFD700", "fontWeight": "bold"},
        style_as_list_view=True
    )
