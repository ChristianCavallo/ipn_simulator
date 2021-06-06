import requests
from rest_server import PaypalServer

paypal_server = PaypalServer()
paypal_server.start()

# Local Docker Test
ipn_host = "http://localhost:2222/payment/ipn"

# Local gateway test
ipn_host = "http://localhost:2221/payment/ipn"

# Kubernetes Test
ipn_host = "http://127.0.0.1:49458/payments-service/payment/ipn"


def send_ipn(id="bbb"):
    print("Sending IPN.")
    data = {
        "invoice": id,
        "item_id": "0",
        "mc_gross": "0.2",
        "mc_currency": "EUR",
        "payer_email": "gm_1231902590_per@paypal.com",
        "receiver_email": "carsharing@payments.com",
        "business": "carsharing@payments.com"
    }
    paypal_server.request = data
    resp = requests.post(ipn_host, data)

    if resp.status_code == 200:
        print("IPN received successfully");
    else:
        print("Failed to sent IPN  to " + ipn_host);


send_ipn("6094323f3f63e1403607ab8a")
