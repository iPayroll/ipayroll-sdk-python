from ipayroll_sdk.models import *
from ipayroll_sdk.parameter import PageParams


class Oauth2Endpoint(object):
    # def __init__(self):
    #     self.__session

    @staticmethod
    def __allow_http_request():
        import os
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    def get_authorization_url(self):
        authorization_url, self.__state = self.session.authorization_url(
            self.__authorization_uri)
        return authorization_url

    def exchange_authorization_code_for_access_token(self, code):
        token = self.fetch_token(
            self.__token_credential_uri,
            code=code,
            client_secret=self.__client_secret)
        return token


class Endpoint(object):
    _url = ''
    _resource = None
    _resources = None

    def __init__(self, requester):
        self._requester = requester

    def _list(self, page, size, path=None, params={}):
        page_params = PageParams(page=page, size=size)
        params.update(page_params.__dict__)
        if path is None:
            path = self._url
        response = self._requester.get(path, params=params)
        return response.as_resource(self._resources)

    def _get(self, id):
        return self._requester.get(self._url + '/' + str(id)).as_resource(self._resource)

    def _create(self, value):
        return self._requester.post(self._url, value).as_resources(self._resource)

    def _update(self, id, value):
        return self._requester.post(self._url + '/' + str(id), value).as_resource(self._resource)

    def _delete(self, id):
        return self._requester.delete(self._url + '/' + str(id))


class CostCentersEndpoint(Endpoint):
    _url = '/api/v1/costcentres'
    _resource = CostCentre
    _resources = CostCentres

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, id):
        return self._get(id)

    def create(self, cost_centre):
        return self._create(cost_centre)


class EmployeesEndpoint(Endpoint):
    _url = '/api/v1/employees'
    _resource = Employee
    _resources = Employees

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, id):
        return self._get(id)

    def create(self, employee):
        return self._create(employee)

    def update(self, employee):
        return self._update(employee.employeeId, employee)


class EmployeeCustomFieldEndpoint(Endpoint):
    def __init__(self, requester, employee_id):
        self._url = '/api/v1/employees/%s/customfields' % (employee_id)
        self._resource = EmployeeCustomField
        self._resources = EmployeeCustomFields
        super(EmployeeCustomFieldEndpoint, self).__init__(requester)

    def list(self, category=None, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size, {'category': category})

    def get(self, id):
        return self._get(id)


class EmployeesLeaveBalancesEndpoint(Endpoint):
    def __init__(self, requester, employee_id):
        self._url = '/api/v1/employees/%s/leaves/balances' % (employee_id)
        self._resource = LeaveBalance
        self._resources = LeaveBalances
        super(EmployeesLeaveBalancesEndpoint, self).__init__(requester)

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, id):
        return self._get(id)


class EmployeesLeaveRequestsEndpoint(Endpoint):
    def __init__(self, requester, employee_id):
        self._url = '/api/v1/employees/%s/leaves/requests' % employee_id
        self._resource = LeaveRequest
        self._resources = LeaveRequests
        super(EmployeesLeaveRequestsEndpoint, self).__init__(requester)

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def list_outstanding(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        url_outstanding = self._url + '/current'
        return self._list(page, size, path=url_outstanding)

    def get(self, id):
        return self._get(id)


class EmployeesPayRatesEndpoint(Endpoint):
    def __init__(self, requester, employee_id):
        self._url = '/api/v1/employees/%s/payrates' % employee_id
        self._resource = PayRate
        self._resources = PayRates
        super(EmployeesPayRatesEndpoint, self).__init__(requester)

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, code):
        return self._get(code)


class LeaveRequestsEndpoint(Endpoint):
    _url = '/api/v1/leaves/requests'
    _resources = LeaveRequests
    _resource = LeaveRequest

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def list_outstanding(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        url_outstanding = self._url + '/current'
        return self._list(page, size, path=url_outstanding)

    def get(self, id):
        return self._get(id)


class PayElementsEndpoint(Endpoint):
    _url = '/api/v1/leaves/payelements'
    _resources = PayElements
    _resource = PayElement

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, id):
        return self._get(id)


class PayslipsEndpoint(Endpoint):
    _url = '/api/v1/payslips'
    _resource = Payslip
    _resources = Payslips

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, id):
        return self._get(id)


class TimesheetsEndpoint(Endpoint):
    _url = '/api/v1/timesheets'
    _resources = Timesheets
    _resource = Timesheet

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, id):
        return self._get(id)

    def get_by_payroll_number(self, id):
        "/{employeeId}/payrolls/{payrollNumber}"
        return self._get(id)

    def delete_timesheet_transaction(self, id):
        "/{employeeId}/transactions/{timesheetTransactionId}"
        self._delete(id)

    def create(self, timesheets):
        self._create(timesheets)
