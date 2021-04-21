from flask import current_app as app
from api.application.rpc_server import RpcServer

app.add_url_rule('/json-rpc/', view_func=RpcServer.as_view('rpcserver'))
