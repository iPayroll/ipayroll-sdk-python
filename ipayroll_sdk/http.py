from requests_oauthlib import OAuth2Session
from ipayroll_sdk.error import IpayrollRequestError, Error


class OAuth2Session(OAuth2Session):
    def __init__(self, client_id, client_secret, redirect_uri, scope, base_url, authorization_uri,
                 token_credential_uri, auto_refresh_url, token_updater):
        extra = {
            'client_id': client_id,
            'client_secret': client_secret,
        }
        super(OAuth2Session, self).__init__(client_id=client_id, redirect_uri=redirect_uri, scope=scope,
                                            auto_refresh_url=base_url + auto_refresh_url, auto_refresh_kwargs=extra,
                                            token_updater=token_updater)

        self.__client_secret = client_secret
        self.base_url = base_url
        self.__authorization_uri = base_url + authorization_uri
        self.__token_credential_uri = base_url + token_credential_uri
        self.__state = None
        self.__allow_http_request()

    @staticmethod
    def __allow_http_request():
        import os
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    def get_authorization_url(self):
        authorization_url, self.__state = self.authorization_url(
            self.__authorization_uri)
        return authorization_url

    def exchange_authorization_code_for_access_token(self, code):
        token = self.fetch_token(
            self.__token_credential_uri,
            code=code,
            client_secret=self.__client_secret)
        return token

    def refresh_access_token(self):
        return self.refresh_token(self.__token_credential_uri)

    def requester(self):
        return Requester(self)


class Requester(object):
    def __init__(self, session):
        self.__session = session

    def post(self, path, data):
        objs = self.__to_dict(data)
        resp = self.__session.post(self.__session.base_url + path, json=objs)
        return Response(resp)

    def get(self, path, **kwargs):
        resp = self.__session.get(self.__session.base_url + path, **kwargs)
        return Response(resp)

    def put(self, path, data):
        objs = self.__to_dict(data)
        resp = self.__session.put(self.__session.base_url + path, json=objs)
        return Response(resp)

    def delete(self, path):
        resp = self.__session.delete(self.__session.base_url + path)
        return Response(resp)

    def __to_dict(self, data):
        if not isinstance(data, list):
            data = [data]
        dicts = []
        for obj in data:
            dicts.append(dict(obj))
        return dicts


class Response(object):
    def __init__(self, response):
        self.response = response

    def content(self):
        try:
            return self.response.json()
        except ValueError:
            return self.response.text

    def ok(self):
        import requests
        status_code = self.response.status_code
        return status_code == requests.codes.ok or status_code == requests.codes.created

    def as_resource(self, klass):
        self.check_error()
        return self.__as_object(self.content(), klass)

    def as_resources(self, klass):
        self.check_error()

        resources_list = []
        for data in self.content():
            resource = self.__as_object(data, klass)
            resources_list.append(resource)

        return resources_list

    def __as_object(self, value, klass):
        instance = klass()
        instance.update(value)
        return instance

    def check_error(self):
        if self.ok():
            return {}
        errors = self.__as_object(self.content(), Error)
        raise IpayrollRequestError(self.response.status_code, self.response.reason, errors)
