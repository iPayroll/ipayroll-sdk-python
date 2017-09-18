import logging
from ipayroll_sdk.models import IpayrollModel
from booby import fields


class Error(IpayrollModel):
    id = fields.String()
    messages = fields.List(fields.String())
    status = fields.String()

    def messages_joined(self):
        return ','.join(self.messages)

    def __str__(self):
        return 'Error[Id:%s Status:%s Messages:%s ]' % (self.id, self.messages_joined(), self.status)


class IpayrollError(Exception):
    pass


class IpayrollAuthenticationError(IpayrollError):
    def __init__(self, value):
        super(Exception, self).__init__(value)


class IpayrollRequestError(IpayrollError):
    def __init__(self, http_status_code, http_reason, error):
        super(Exception, self).__init__(http_reason)
        self.http_status_code = http_status_code
        self.http_reason = http_reason
        self.error = error

    def __str__(self):
        return 'HTTP[Code:%d Status:%s] %s' % (self.http_status_code, self.http_reason, self.error)
