"""Call the orders service over HTTP to enrich invoices."""
import requests


def fetch_orders():
    return requests.get("/v1/orders").json()
