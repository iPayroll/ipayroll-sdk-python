from ipayroll_sdk.http import OAuth2Session, Requester
from ipayroll_sdk.endpoint import *


class Client(object):
    API_BASE_URL_DEFAULT = 'http://secure2.ipayroll.co.nz'
    AUTHORIZATION_URI_DEFAULT = '/oauth/authorize'
    TOKEN_CREDENTIAL_URI_DEFAULT = '/oauth/token'
    REFRESH_TOKEN_URI_DEFAULT = '/oauth/token'

    SCOPE_DEFAULT = ['leavebalances', 'payelements', 'payrates', 'leaverequests', 'employees', 'costcentres',
                     'payslips', 'timesheets', 'customfields', 'payrolls']

    def __init__(self, client_id, client_secret, redirect_uri, scope=SCOPE_DEFAULT,
                 base_url=API_BASE_URL_DEFAULT, authorization_uri=AUTHORIZATION_URI_DEFAULT,
                 token_credential_uri=TOKEN_CREDENTIAL_URI_DEFAULT, refresh_token_uri=REFRESH_TOKEN_URI_DEFAULT,
                 access_token_updater=None):
        self.__base_url = base_url
        self.__session = OAuth2Session(client_id, client_secret, redirect_uri, scope, base_url,
                                       authorization_uri, token_credential_uri, refresh_token_uri, access_token_updater)

    def oauth2(self):
        return Oauth2Endpoint(self.__session)

    def cost_centres(self):
        return CostCentersEndpoint(self.requester())

    def employees(self):
        return EmployeesEndpoint(self.requester())

    def employee_custom_fields(self, employee_id):
        return EmployeeCustomFieldsEndpoint(self.requester(), employee_id)

    def employee_payrates(self, employee_id):
        return EmployeesPayRatesEndpoint(self.requester(), employee_id)

    def employee_leave_balances(self, employee_id):
        return EmployeeLeaveBalancesEndpoint(self.requester(), employee_id)

    def employee_leave_requests(self, employee_id):
        return EmployeeLeaveRequestsEndpoint(self.requester(), employee_id)

    def leave_requests(self):
        return LeaveRequestsEndpoint(self.requester())

    def pay_elements(self):
        return PayElementsEndpoint(self.requester())

    def payslips(self):
        return PayslipsEndpoint(self.requester())

    def timesheets(self):
        return TimesheetsEndpoint(self.requester())

    def timesheets_transactions(self):
        return TimesheetTransactionsEndpoint(self.requester())

    def payrolls(self):
        return PayrollsEndpoint(self.requester())

    def requester(self):
        return Requester(self.__session)
