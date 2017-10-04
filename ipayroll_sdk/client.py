from ipayroll_sdk.http import OAuth2Session
from ipayroll_sdk.endpoint import *


class Client(object):
    API_BASE_URL_DEFAULT = 'http://secure2.ipayroll.co.nz'
    AUTHORIZATION_URI_DEFAULT = '/oauth/authorize'
    TOKEN_CREDENTIAL_URI_DEFAULT = '/oauth/token'
    REFRESH_TOKEN_URI_DEFAULT = '/oauth/token'

    SCOPE_DEFAULT = ['leavebalances', 'payelements', 'payrates', 'leaverequests', 'employees', 'costcentres',
                     'payslips', 'timesheets', 'customfields']

    def __init__(self, client_id, client_secret, redirect_uri, scope=SCOPE_DEFAULT,
                 base_url=API_BASE_URL_DEFAULT, authorization_uri=AUTHORIZATION_URI_DEFAULT,
                 token_credential_uri=TOKEN_CREDENTIAL_URI_DEFAULT, refresh_token_uri=REFRESH_TOKEN_URI_DEFAULT,
                 token_updater=None):
        if token_updater is None:
            token_updater = self.token_updater

        self.__base_url = base_url
        self.__session = OAuth2Session(client_id, client_secret, redirect_uri, scope, base_url,
                                       authorization_uri, token_credential_uri, refresh_token_uri, token_updater)

    def token_updater(self, token):
        pass

    def oauth2(self):
        return self.__session

    def cost_centres(self):
        return CostCentersEndpoint(self.__session.requester())

    def employees(self):
        return EmployeesEndpoint(self.__session.requester())

    def employees_custom_field(self, employee_id):
        return EmployeeCustomFieldEndpoint(self.__session.requester(), employee_id)

    def employees_payrates(self, employee_id):
        return EmployeesPayRatesEndpoint(self.__session.requester(), employee_id)

    def employees_leave_balance(self, employee_id):
        return EmployeesLeaveBalancesEndpoint(self.__session.requester(), employee_id)

    def employees_leave_requests(self, employee_id):
        return EmployeesLeaveRequestsEndpoint(self.__session.requester(), employee_id)

    # def employeesPayslips(self, employee_id):
    #     return EmployeesPayslipsEndpoint(self.__session.requester(), employee_id)

    def leave_requests(self):
        return LeaveRequestsEndpoint(self.__session.requester())

    def pay_elements(self):
        return PayElementsEndpoint(self.__session.requester())

        # def payslips(self):
        #     return PayslipsEndpoint(self.__session.requester())
