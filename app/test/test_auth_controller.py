import unittest
import json
from app.test.base import BaseTestCase
from flask_api import status

def login_user(self,email,password):

    reqData=dict()
    if email!=None:
        reqData['email']=email

    if password!=None:
        reqData['password']=password

    return self.client.post(
        'auth/user/login',
        data=json.dumps(reqData),
        content_type='application/json'
    )

class TestUserLogin(BaseTestCase):

    def test_login_user_valid(self):
        with self.client:
            response=login_user(self,"demo@financialhouse.io","cjaiU8CV")
            content=json.loads(response.data.decode())
            self.assertEqual(content.get("status"),"APPROVED")
            self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_login_user_invalid(self):
        with self.client:
            response=login_user(self,"demo@financialhouse.io","23432")
            content=json.loads(response.data.decode())
            self.assertEqual(content.get("status"),"DECLINED")
            self.assertEqual(response.status_code,status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_login_user_blank(self):
        with self.client:
            response = login_user(self, "", "")
            content = json.loads(response.data.decode())
            self.assertEqual(content.get("status"), "DECLINED")
            self.assertEqual(response.status_code,status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_login_user_without_email(self):
        with self.client:
            response = login_user(self, None, "cjaiU8CV")
            content = json.loads(response.data.decode())
            self.assertEqual(content.get("message"), "Input payload validation failed")
            self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_login_user_without_password(self):
        with self.client:
            response = login_user(self, "demo@financialhouse.io", None)
            content = json.loads(response.data.decode())
            self.assertEqual(content.get("message"), "Input payload validation failed")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user_without_email_and_password(self):
        with self.client:
            response = login_user(self, None, None)
            content = json.loads(response.data.decode())
            self.assertEqual(content.get("message"), "Input payload validation failed")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



if __name__ == '__main__':
    unittest.main()