from flask import request,make_response
from flask_restx import Resource
import requests
from flask import current_app

from ..util.dto import TxnReportDto
from ..util.decorator import token_required

api = TxnReportDto.api
txn_report = TxnReportDto.txn_report
txn_list=TxnReportDto.txn_list
txn_detail=TxnReportDto.txn_detail
head_parser=TxnReportDto.head_parser

@api.route('/report')
class TransactionReport(Resource):
    """
        Transactions Report Resource
    """
    @token_required
    @api.expect(head_parser,txn_report, validate=True)
    def post(self):

        post_data = request.json
        token=request.headers.get("Authorization",None)
        url = current_app.config["CLIENT_BASE_URL"] + "transactions/report"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain','Authorization':token}
        r = requests.post(url, data=None, json=post_data, headers=headers)

        return make_response(r.json(),r.status_code)


@api.route('/list')
class TransactionList(Resource):
    """
        Transactions List Resource
    """

    @token_required
    @api.expect(head_parser,txn_list, validate=True)
    def post(self):

        post_data = request.json
        token=request.headers.get("Authorization",None)
        url = current_app.config["CLIENT_BASE_URL"] + "transaction/list"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain','Authorization':token}
        r = requests.post(url, data=None, json=post_data, headers=headers)

        return make_response(r.json(),r.status_code)


@api.route('')
class TransactionDetail(Resource):
    """
        Transactions Get Details
    """

    @token_required
    @api.expect(head_parser,txn_detail, validate=True)
    def post(self):

        post_data = request.json
        token=request.headers.get("Authorization",None)
        url = current_app.config["CLIENT_BASE_URL"] + "transaction"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain','Authorization':token}
        r = requests.post(url, data=None, json=post_data, headers=headers)

        return make_response(r.json(),r.status_code)