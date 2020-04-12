from flask_restx import Namespace, fields,reqparse

class BaseAuthorizaton:
    head_parser = reqparse.RequestParser()
    head_parser.add_argument('Authorization', location='headers', required=True)

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class TxnReportDto(BaseAuthorizaton):
    api = Namespace('transactions', description='transactions report')
    txn_report = api.model('txn_report_details', {
        'fromDate': fields.Date(required=True, description='YYYY-MM-DD'),
        'toDate': fields.Date(required=True, description='YYYY-MM-DD'),
        'merchant':fields.Integer(description='The merchant identifier'),
        'acquirer':fields.Integer(description='The acquirer identifier'),
    })
    txn_list = api.model('txn_list_details', {
        'fromDate': fields.Date(description='YYYY-MM-DD'),
        'toDate': fields.Date(description='YYYY-MM-DD'),
        'status': fields.String(description='The API request status'),
        'operation': fields.String(description='Request operation'),
        'merchant': fields.Integer(description='The merchant identifier'),
        'acquirer': fields.Integer(description='The acquirer identifier'),
        'paymentMethod': fields.String(description='The payment method'),
        'errorCode': fields.String(description='Error code'),
        'filterField': fields.String(description='Search by special field'),
        'filterValue': fields.String(description='Value of field'),
        'page': fields.Integer(description='Number of page'),

    })
    txn_detail = api.model('txn_get_details', {
        'transactionId': fields.String(required=True,description='transaction id value'),
    })



class ClientDto(BaseAuthorizaton):
    api = Namespace('client', description='client information')
    client_detail = api.model('client_get_details', {
        'transactionId': fields.String(required=True,description='transaction id value'),
    })


