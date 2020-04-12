import unittest
import json
from app.test.base import BaseTestCase
from flask_api import status


def client_service(self,transactionId,token):
    reqData=dict()
    if transactionId!=None:
        reqData['transactionId']=transactionId

    return self.client.post(
        'client',
        data=json.dumps(reqData),
        content_type='application/json',
        headers={'Authorization':token}
    )

class TestClientDetail(BaseTestCase):

    def test_client_service_without_token(self):
        with self.client:
            response=client_service(self,"1-1444392550-1","")
            content=json.loads(response.data.decode())
            self.assertEqual(content.get("status"),"fail")
            self.assertEqual(content.get("message"),"Token is required")
            self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_client_service_with_token_expired(self):
        with self.client:
            response=client_service(self,"1-1444392550-1",self.invalidToken)
            content=json.loads(response.data.decode())
            self.assertEqual(content.get("status"),"DECLINED")
            self.assertEqual(content.get("message"),"Token Expired")
            self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_client_service_with_token_valid(self):
        with self.client:
            response = client_service(self, "1-1444392550-1", self.validToken)
            self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_client_service_without_transactionId(self):
        with self.client:
            response = client_service(self, None, self.validToken)
            content = json.loads(response.data.decode())
            self.assertEqual(content.get("message"), "Input payload validation failed")
            self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)



if __name__ == '__main__':
    unittest.main()