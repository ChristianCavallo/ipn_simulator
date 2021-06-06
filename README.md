# IPN Simulator
This project is related to https://github.com/ChristianCavallo/CarSharing. We used it to simulate a Paypal payment system.


The "PaypalServer" class is a rest server that wait for a POST request to be received on **'/webscr'**. 
It checks if the request is good and then it responds with "INVALID" or "VERIFIED".

"simulator.py" contains just a "send_ipn" method. It's used to simulate an IPN request that would be sent from a Paypal Server to a specific API on the Payment microservice.
