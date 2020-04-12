from flask_restx import Api
from flask import Blueprint

from .main.controller.auth_controller import api as auth_ns
from .main.controller.transaction_controller import api as txn_ns
from .main.controller.client_controller import api as client_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK TEST PROJECT',
          version='1.0',
          description='flask web service for using merchant services'
          )

api.add_namespace(auth_ns)
api.add_namespace(txn_ns)
api.add_namespace(client_ns)