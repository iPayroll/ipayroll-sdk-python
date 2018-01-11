from ipayroll_sdk.models import *
from ipayroll_sdk.parameter import PageParams


class Oauth2Endpoint(object):

    def __init__(self, oauth2_session, ):
        self.__oauth2_session = oauth2_session

    def get_authorization_url(self):
        authorization_url, self.__oauth2_session.__state = self.__oauth2_session.authorization_url(
            self.__oauth2_session.get_authorization_uri())
        return authorization_url

    def exchange_authorization_code_for_access_token(self, code):
        token = self.__oauth2_session.fetch_token(
            self.__oauth2_session.get_token_credential_uri(),
            code=code,
            client_secret=self.__oauth2_session.get_client_secret())
        return self.__update_token(token);

    def refresh_access_token(self, refresh_token=None):
        token = self.__oauth2_session.refresh_token(self.__oauth2_session.get_token_credential_uri(),
                                                    refresh_token=refresh_token)
        return self.__update_token(token);

    def connect_with_refresh_token(self, refresh_token):
        return self.refresh_access_token(refresh_token);

    def connect_with_access_token(self, oauth2_access_token):
        return self.refresh_access_token(oauth2_access_token.refresh_token);

    def __update_token(self, token):
        access_token = OAuth2Token()
        access_token.update(token)
        if self.__oauth2_session.token_updater:
            self.__oauth2_session.token_updater(token)
        return access_token


class Endpoint(object):
    _url = ''
    _resource = None
    _resources = None

    def __init__(self, requester):
        self._requester = requester

    def _list(self, page, size, params={}, path=None):
        page_params = PageParams(page=page, size=size)
        params.update(page_params.__dict__)
        if path is None:
            path = self._url
        response = self._requester.get(path, params=params)
        return response.as_resource(self._resources)

    def _get(self, id):
        return self._requester.get(self._url + '/' + str(id)).as_resource(self._resource)

    def _get_url(self, url):
        return self._requester.get(url).as_resource(self._resource)

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


class EmployeeCustomFieldsEndpoint(Endpoint):
    def __init__(self, requester, employee_id):
        self._url = '/api/v1/employees/%s/customfields' % (employee_id)
        self._resource = EmployeeCustomField
        self._resources = EmployeeCustomFields
        super(EmployeeCustomFieldsEndpoint, self).__init__(requester)

    def list(self, category=None, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size, {'category': category})

    def get(self, id):
        return self._get(id)

    def list_by_category(self, category, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self.list(category, page, size)

    def get_by_category_and_id(self, category, id):
        url = "%s/%s/%s" % (self._url, category, id);
        return self._get_url(url)


class EmployeeLeaveBalancesEndpoint(Endpoint):
    def __init__(self, requester, employee_id):
        self._url = '/api/v1/employees/%s/leaves/balances' % (employee_id)
        self._resource = LeaveBalance
        self._resources = LeaveBalances
        super(EmployeeLeaveBalancesEndpoint, self).__init__(requester)

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, id):
        return self._get(id)


class EmployeeLeaveRequestsEndpoint(Endpoint):
    def __init__(self, requester, employee_id):
        self._url = '/api/v1/employees/%s/leaves/requests' % employee_id
        self._resource = LeaveRequest
        self._resources = LeaveRequests
        super(EmployeeLeaveRequestsEndpoint, self).__init__(requester)

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

    def create(self, employee):
        return self._create(employee)

    def update(self, employee):
        return self._update(employee.employeeId, employee)


class PayElementsEndpoint(Endpoint):
    _url = '/api/v1/payelements'
    _resources = PayElements
    _resource = PayElement

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, id):
        return self._get(id)


class PayrollsEndpoint(Endpoint):
    _url = '/api/v1/payrolls'
    _resources = Payrolls
    _resource = Payroll

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, id):
        return self._get(id)

    def get_current(self):
        return self.get('current')


class PayrollPayslipsEndpoint(Endpoint):
    def __init__(self, requester, payroll_id):
        self._url = '/api/v1/payrolls/%s/payslips' % payroll_id
        self._resource = Payslip
        self._resources = Payslips
        super(PayrollPayslipsEndpoint, self).__init__(requester)

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, id):
        return self._get(id)


class TimesheetTransactionsEndpoint(Endpoint):
    def __init__(self, requester, timesheet_id):
        self._url = "/api/v1/timesheets/%s/transactions" % timesheet_id
        self._resource = TimesheetTransaction
        super(TimesheetTransactionsEndpoint, self).__init__(requester)

    def delete(self, id):
        return self._delete(id)


class TimesheetsEndpoint(Endpoint):
    _url = '/api/v1/timesheets'
    _resources = Timesheets
    _resource = Timesheet

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, id):
        return self._get(id)

    def create(self, timesheets):
        return self._create(timesheets)

    def get_by_payroll_id(self, timesheet_id, payroll_id):
        url = "%s/payrolls/%s" % (self._url, timesheet_id, payroll_id)
        return self._get_url(url)

    def transactions(self, timesheet_id):
        TimesheetTransactionsEndpoint(self._requester, timesheet_id);

    def delete_transaction(self, timesheet_id, id):
        return self.transactions(timesheet_id).delete(id)
