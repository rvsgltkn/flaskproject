from flask import request,make_response
from flask_restx import Resource
import requests
from flask import current_app

from ..util.dto import ClientDto
from ..util.decorator import token_required

api = ClientDto.api
client_detail=ClientDto.client_detail
head_parser=ClientDto.head_parser

@api.route('')
class ClientDetail(Resource):
    """
        Client Detail Resource
    """
    @token_required
    @api.expect(head_parser,client_detail, validate=True)
    def post(self):

        post_data = request.json
        token=request.headers.get("Authorization",None)
        url = current_app.config["CLIENT_BASE_URL"] + "client"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain','Authorization':token}
        r = requests.post(url, data=None, json=post_data, headers=headers)

        return make_response(r.json(),r.status_code)
