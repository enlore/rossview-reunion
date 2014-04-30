from ..__init__ import create_app
import pytest

from ..helpers import EmailBase as Email

@pytest.fixture()
def app():
    app = create_app(instance_path='/home/no/projects/rossview.reunion.net/instance', test=True)

    def fake_csrf():
        return 'boobs'
    app.jinja_env.globals['csrf_token'] = fake_csrf

    return app.test_client()

def test_email_to_field_is_list():
    email = Email('bob', 'edd', 'Hi Edd', 'Hey man how are you')
    assert list == type(email.to)

def test_email_gets_to_where_its_going(app):
    resp = app.post('/', data={
            "name": "bob",
            "email": "oneofy@gmail.com",
            "phone": "123456"
        })

    assert 200 == resp.status_code
