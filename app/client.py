"""Call the orders service over HTTP to enrich invoices."""
import requests

import orders_svc  # cross-repo package dependency on orders-service


def fetch_orders():
    return orders_svc.normalize(requests.get("/v1/orders").json())
