from flask_api import status

class Auth:

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization',None)
        if auth_token==None or auth_token=="":
            response_object = {
                'status': 'fail',
                'message': 'Token is required'
            }
            return response_object, status.HTTP_401_UNAUTHORIZED
        else:
            response_object = {
                'status': 'success',
                'token': auth_token
            }
            return response_object, status.HTTP_200_OK