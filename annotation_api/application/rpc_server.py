import simplejson as json
from flask import request
from flask.views import View
from jsonrpc import JSONRPCResponseManager, dispatcher


@dispatcher.add_method
def test():  # TODO remove test method
    return 'ok'


class RpcServer(View):
    methods = ['GET', 'POST']
    """https://flask.palletsprojects.com/en/1.1.x/api/#class-based-views
    https://json-rpc.readthedocs.io/en/latest/quickstart.html
    https://json-rpc.readthedocs.io/en/latest/flask_integration.html
    """

    def dispatch_request(self):

        dispatcher['ping'] = lambda: 'pong'

        try:
            response = JSONRPCResponseManager.handle(request.data, dispatcher)
        except Exception as e:
            raise e

        return json.dumps(response.data, for_json=True)
