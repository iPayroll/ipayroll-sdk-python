from ipayroll_sdk.models import *
from ipayroll_sdk.parameter import PageParams


class Oauth2Endpoint(object):
    def __init__(self):
        self.__session

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

    def _list(self, page, size):
        pageParams = PageParams(page=page, size=size)
        response = self._requester.get(self._url, params=pageParams.__dict__)
        return response.as_resource(self._resources)

    def _get(self, id):
        return self._requester.get(self._url + '/' + id).as_resource(self._resource)

    def _create(self, value):
        return self._requester.post(self._url, value).as_resources(self._resource)

    def _update(self, id, value):
        return self._requester.post(self._url + '/' + id, value).as_resource(self._resource)

    def _delete(self, id):
        return self._requester.delete(self._url + '/' + id)


class CostCentersEndpoint(Endpoint):
    _url = '/api/v1/costcentres'
    _resource = CostCentre
    _resources = CostCentres

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, id):
        return self._get(id)

    def create(self, costCentre):
        return self._create(costCentre)


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
        if not category:
            return self._list(page, size)
        else:
            return self._list_category(category, page)

    def _list_category(self, category, page, size):
        pageParams = PageParams(page=page, size=size)
        response = self._requester.get(self._url + '/' + category, params=pageParams.__dict__)
        return response.as_resource(self._resources)

    def get(self, category, id):
        return self._requester.get(self._url + '/' + category + '/' + id).as_resource(self._resource)


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

    def getOutstanding(self):
        return self._get('current')


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


# class LeaveBalanceEndpoint

# class EmployeesPayslipsEndpoint(Endpoint):
#     pass


class LeaveRequestsEndpoint(Endpoint):
    _url = '/api/v1/leaves/requests'
    _resources = LeaveRequests
    _resource = LeaveRequest

    def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
        return self._list(page, size)

    def get(self, id):
        return self._get(id)

    def getOutstanding(self):
        return self._get('current')


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

    def create(self, timecardEntries):
        self._create(timecardEntries)

# class TimecardEntriesEndpoint(Endpoint):
#     _url = '/api/v1/timecard/entry'
#     _resources = TimecardEntries
#     _resource = TimecardEntry
#
#     def list(self, page=PageParams.DEFAULT_PAGE, size=PageParams.DEFAULT_SIZE):
#         return self._list(page, size)
#
#     def get(self, id):
#         return self._get(id)
#
#     def delete(self, id):
#         self._delete(id)
#
#     def create(self, timecardEntry):
#         self._create(timecardEntry)
#
#     def update(self, timecardEntry):
#         self._update(timecardEntry.id, timecardEntry)
#
#
# class TimecardSettingsEndpoint(Endpoint):
#     _url = '/api/v1/timecard/entry'
#     _resource = TimecardSetting
#
#     def get(self, orgNumber):
#         return self._requester.get(self._url, params={'orgNumber': orgNumber}).as_resource(self._resource)
