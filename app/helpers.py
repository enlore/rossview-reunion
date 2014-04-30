import requests

class EmailBase(object):
    def __init__(self, from_, to, subject, body):
        self.from_ = from_

        if not type(to) == list:
            to = [to]

        self.to = to
        self.subject = subject
        self.body = body

class FlaskMailgunMessage(EmailBase):
    def __init__(self, app):
        self.app        = app
        self.endpoint   = self.app.config['MAILGUN_ENDPOINT']
        self.api_key    = self.app.config['MAILGUN_API_KEY']

        # woo!
        super(FlaskMailgunMessage, self).__init__(
                from_=app.config['EMAIL_FROM'],
                to=app.config['EMAIL_TO'],
                subject=app.config['EMAIL_SUBJECT'],
                body=''
                )
        
    def send(self, body, html=False, **kwargs):
        data = {
            "from"  : self.from_,
            "to"    : self.to,
            "subject": self.subject,
            }

        for key, val in kwargs.items():
            data['o:' + key] = val

        if html:
            data['html'] = body
        else:
            data['text'] = body

        res = requests.post(
                self.endpoint,
                auth=("api", self.api_key),
                data=data
                )

        self.app.logger.info(res.json())
        return res
