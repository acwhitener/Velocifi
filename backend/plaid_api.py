import os
from plaid import Client
from flask import current_app
from dotenv import load_dotenv
import datetime

load_dotenv()

client = Client(
    client_id=os.getenv("PLAID_CLIENT_ID"),
    secret=os.getenv("PLAID_SECRET"),
    environment="sandbox"
)

def create_link_token():
    response = client.LinkToken.create({
        'user': {'client_user_id': 'unique-user-id'},
        'client_name': 'Velocifi',
        'products': ['transactions'],
        'country_codes': ['US'],
        'language': 'en',
        'redirect_uri': None
    })
    return response['link_token']

def exchange_public_token(public_token):
    exchange = client.Item.public_token.exchange(public_token)
    return exchange['access_token'], exchange['item_id']

def fetch_transactions(access_token, start_date=None, end_date=None):
    if not start_date:
        start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
    if not end_date:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d')

    response = client.Transactions.get(
        access_token,
        start_date=start_date,
        end_date=end_date
    )
    return response['transactions']
