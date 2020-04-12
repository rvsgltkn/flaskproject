import unittest
import json
from app.test.base import BaseTestCase
from flask_api import status


def transaction_report_service(self,fromDate,toDate,merchant,acquirer,token):
    reqData=dict()
    if fromDate!=None:
        reqData['fromDate']=fromDate
    if toDate!=None:
        reqData['toDate']=toDate
    if merchant!=None:
        reqData['merchant']=merchant
    if acquirer!=None:
        reqData['acquirer']=acquirer

    return self.client.post(
        'transactions/report',
        data=json.dumps(reqData),
        content_type='application/json',
        headers={'Authorization':token}
    )

def transaction_list_service(self,fromDate,toDate,merchant,acquirer,token):
    reqData = dict()
    if fromDate != None:
        reqData['fromDate'] = fromDate
    if toDate != None:
        reqData['toDate'] = toDate
    if merchant != None:
        reqData['merchant'] = merchant
    if acquirer != None:
        reqData['acquirer'] = acquirer

    return self.client.post(
        'transactions/list',
        data=json.dumps(reqData),
        content_type='application/json',
        headers={'Authorization':token}
    )

def transaction_detail_service(self,transactionId,token):
    reqData=dict()
    if transactionId!=None:
        reqData['transactionId']=transactionId

    return self.client.post(
        'transactions',
        data=json.dumps(reqData),
        content_type='application/json',
        headers={'Authorization':token}
    )

class TestTransactionReport(BaseTestCase):

    def test_transaction_report_without_token(self):
        with self.client:
            response=transaction_report_service(self,"2015-07-01","2015-10-01",1,1,"")
            content=json.loads(response.data.decode())
            self.assertEqual(content.get("status"),"fail")
            self.assertEqual(content.get("message"),"Token is required")
            self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_transaction_report_with_token_expired(self):
        with self.client:
            response=transaction_report_service(self,"2015-07-01","2015-10-01",1,1,self.invalidToken)
            content=json.loads(response.data.decode())
            self.assertEqual(content.get("status"),"DECLINED")
            self.assertEqual(content.get("message"),"Token Expired")
            self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_transaction_report_with_token_valid(self):
        with self.client:
            response = transaction_report_service(self,"2015-07-01","2015-10-01",1,1,self.validToken)
            content = json.loads(response.data.decode())
            self.assertEqual(response.status_code,status.HTTP_200_OK)
            self.assertEqual(content.get("status"), "APPROVED")

    def test_transaction_report_without_fromDate(self):
        with self.client:
            response = transaction_report_service(self, None, "2015-10-01", 1, 1, self.validToken)
            content = json.loads(response.data.decode())
            self.assertEqual(content.get("message"), "Input payload validation failed")
            self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_transaction_report_without_toDate(self):
        with self.client:
            response = transaction_report_service(self, "2015-07-01", None, 1, 1, self.validToken)
            content = json.loads(response.data.decode())
            self.assertEqual(content.get("message"), "Input payload validation failed")
            self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_transaction_report_without_fromDate_and_toDate(self):
        with self.client:
            response = transaction_report_service(self, None, None, 1, 1, self.validToken)
            content = json.loads(response.data.decode())
            self.assertEqual(content.get("message"), "Input payload validation failed")
            self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)


class TestTransactionList(BaseTestCase):

    def test_transaction_list_without_token(self):
        with self.client:
            response=transaction_list_service(self,"2015-07-01","2015-10-01",1,1,"")
            content=json.loads(response.data.decode())
            self.assertEqual(content.get("status"),"fail")
            self.assertEqual(content.get("message"),"Token is required")
            self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_transaction_list_with_token_expired(self):
        with self.client:
            response=transaction_list_service(self,"2015-07-01","2015-10-01",1,1,self.invalidToken)
            content=json.loads(response.data.decode())
            self.assertEqual(content.get("status"),"DECLINED")
            self.assertEqual(content.get("message"),"Token Expired")
            self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_transaction_list_with_token_valid(self):
        with self.client:
            response = transaction_list_service(self,"2015-07-01","2015-10-01",1,1,self.validToken)
            self.assertEqual(response.status_code,status.HTTP_200_OK)


class TestTransactionDetail(BaseTestCase):

    def test_transaction_detail_without_token(self):
        with self.client:
            response=transaction_detail_service(self,"1-1444392550-1","")
            content=json.loads(response.data.decode())
            self.assertEqual(content.get("status"),"fail")
            self.assertEqual(content.get("message"),"Token is required")
            self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_transaction_detail_with_token_expired(self):
        with self.client:
            response=transaction_detail_service(self,"1-1444392550-1",self.invalidToken)
            content=json.loads(response.data.decode())
            self.assertEqual(content.get("status"),"DECLINED")
            self.assertEqual(content.get("message"),"Token Expired")
            self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_transaction_detail_with_token_valid(self):
        with self.client:
            response = transaction_detail_service(self,"1-1444392550-1",self.validToken)
            self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_transaction_detail_without_transactionId(self):
        with self.client:
            response = transaction_detail_service(self, None, self.validToken)
            content = json.loads(response.data.decode())
            self.assertEqual(content.get("message"), "Input payload validation failed")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

if __name__ == '__main__':
    unittest.main()