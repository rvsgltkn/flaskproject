from flask_testing import TestCase
import json
from manage import app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def setUp(self):
        self.invalidToken="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZXJjaGFudFVzZXJJZCI6NTMsInJvbGUiOiJ1c2VyIiwibWVyY2hhbnRJZCI6Mywic3ViTWVyY2hhbnRJZHMiOlszLDc0LDkzLDExOTEsMTI5NSwxMTEsMTM3LDEzOCwxNDIsMTQ1LDE0NiwxNTMsMzM0LDE3NSwxODQsMjIwLDIyMSwyMjIsMjIzLDI5NCwzMjIsMzIzLDMyNywzMjksMzMwLDM0OSwzOTAsMzkxLDQ1NSw0NTYsNDc5LDQ4OCw1NjMsMTE0OSw1NzAsMTEzOCwxMTU2LDExNTcsMTE1OCwxMTc5LDEyOTMsMTI5NCwxMzA2LDEzMDddLCJ0aW1lc3RhbXAiOjE1ODY1NjQzMjN9.WeBroKjnmnycKXO48gS2FEqQHgaSYRR5rLOjq99mMGI"

        response=self.client.post(
        'auth/user/login',
        data=json.dumps(dict(
            email="demo@financialhouse.io",
            password="cjaiU8CV"
        )),
        content_type='application/json'
        )
        context=json.loads(response.data.decode())
        self.validToken=context.get("token")


    def tearDown(self):
        pass