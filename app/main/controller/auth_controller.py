from flask import request,make_response
from flask_restx import Resource
import requests
from flask import current_app

from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth



@api.route('/user/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        url = current_app.config["CLIENT_BASE_URL"] + "merchant/user/login"
        r = requests.post(url, data=None, json=post_data)

        return make_response(r.json(),r.status_code)
