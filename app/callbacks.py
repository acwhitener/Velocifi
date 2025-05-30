from dash import Input, Output, State, ctx, no_update
from backend.models import db, Transaction
from flask import current_app as app
import dash
import pandas as pd
from dash.exceptions import PreventUpdate

def register_callbacks(dash_app):
    @dash_app.callback(
        Output('transaction-table', 'data'),
        Input('sync-button', 'n_clicks'),
        prevent_initial_call=True
    )
    def sync_and_load_data(n_clicks):
        from backend.plaid_api import fetch_transactions
        from backend.models import Transaction

        with app.app_context():
            access_token = os.getenv("PLAID_ACCESS_TOKEN")  # In real app, query User model
            plaid_txns = fetch_transactions(access_token)

            for txn in plaid_txns:
                if not Transaction.query.filter_by(id=txn['transaction_id']).first():
                    t = Transaction(
                        id=txn['transaction_id'],
                        account_id=1,
                        name=txn['name'],
                        amount=txn['amount'],
                        category=txn['category'][0] if txn['category'] else "Uncategorized",
                        date=txn['date'],
                        pending=txn['pending']
                    )
                    db.session.add(t)
            db.session.commit()

            transactions = Transaction.query.order_by(Transaction.date.desc()).limit(100).all()
            return [{
                'date': t.date.strftime('%Y-%m-%d'),
                'name': t.name,
                'amount': t.amount,
                'category': t.category
            } for t in transactions]

    # Add more callbacks here...
