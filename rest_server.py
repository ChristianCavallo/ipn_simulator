import json
from threading import Thread

import connexion


class PaypalServer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.app = connexion.App(__name__, specification_dir='./')
        self.request = {}

    def run(self):
        @self.app.route('/webscr', methods=['POST'])
        def ipn_callback():
            data = connexion.request.form.to_dict()

            # First item should be cmd=_notify-validate
            first_item = list(data.items())[0]
            if first_item[0] == "cmd" and first_item[1] == "_notify-validate":
                print("First item check passed.")
            else:
                print("First item check failed.")
                return "INVALID"

            # The request must contains the previous elements in the same order.
            l = list(data.items())
            data = dict(l[1:]) # First item removed. The rest must be the same.

            if data != self.request:
                print("Same requests check failed.")
                return "INVALID"

            print("IPN verified correctly.")
            return "VERIFIED";

        self.app.run(port=8079)
