from ..__init__ import create_app
import pytest

from ..helpers import EmailBase as Email
from ..helpers import FlaskMailgunMessage

@pytest.fixture()
def app():

    app = create_app(instance_path='/home/no/projects/rossview.reunion.net/instance', test=True)
    return app

@pytest.fixture()
def client(app):

    def fake_csrf():
        return 'boobs'

    app.jinja_env.globals['csrf_token'] = fake_csrf

    return app.test_client()

def test_flashes(client, app):
    resp = client.post('/', data={
            "name": "bob",
            "email": "oneofy@gmail.com",
            "phone": "123456"
        })

    assert app.config['THANKS_FLASH'] in resp.data

def test_email_to_field_is_list():
    email = Email('bob', 'edd', 'Hi Edd', 'Hey man how are you')
    assert list == type(email.to)

def test_that_we_can_post_to_the_app(client):
    resp = client.post('/', data={
            "name": "bob",
            "email": "oneofy@gmail.com",
            "phone": "123456"
        })

    assert 200 == resp.status_code

def test_mailgun_likes_us(app):
    email = FlaskMailgunMessage(app)
    resp = email.send('hallo boobtick', testmode='true')
    assert 200 == resp.status_code 
    assert 'Queued. Thank you.' == resp.json()['message']

