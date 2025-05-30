# Velocifi - Personal Finance Dashboard
Velocifi/
├── app/                         # Dash frontend
│   ├── __init__.py
│   ├── layout.py
│   └── pages/
│       ├── __init__.py
│       ├── home.py
│       └── transactions.py
│
├── backend/                     # Backend logic
│   ├── __init__.py
│   ├── plaid_api.py             # Plaid integration logic
│   ├── routes.py                # Flask routes for API endpoints (e.g. Plaid auth)
│   └── database/                # DB schema and models
│       ├── __init__.py
│       └── models.py
│
├── run.py                       # Entry point
├── .env
├── requirements.txt
└── README.md
