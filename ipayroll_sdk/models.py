from booby import Model, fields


class IpayrollModel(Model):
    other = {}

    def __setitem__(self, k, v):
        if k not in self._fields:
            self.other[k] = v
        setattr(self, k, v)


class OAuth2Token(IpayrollModel):
    token_type = fields.String()
    refresh_token = fields.String()
    access_token = fields.String()
    scope = fields.String()
    expires_in = fields.Integer()
    expires_at = fields.Float()


class Links(IpayrollModel):
    href = fields.String()
    rel = fields.String()


class Page(IpayrollModel):
    size = fields.Integer()
    totalElements = fields.Integer()
    totalPages = fields.Integer()
    number = fields.Integer()


class Resource(IpayrollModel):
    links = fields.Collection(Links)
    id = fields.String()


class Resources(IpayrollModel):
    links = fields.Collection(Links)
    page = fields.Embedded(Page)


class CostCentre(Resource):
    code = fields.String()
    description = fields.String()
    displayValue = fields.String()


class Address(Resource):
    addressLine1 = fields.String()
    addressLine2 = fields.String()
    suburb = fields.String()
    city = fields.String()
    state = fields.String()
    postCode = fields.String()
    country = fields.String()


class Employee(Resource):
    surname = fields.String()
    firstNames = fields.String()
    startDate = fields.String()
    birthDate = fields.String()
    defaultCostCentre = fields.String()
    email = fields.String()
    phone = fields.String()
    title = fields.String()
    workState = fields.String()
    gender = fields.String()
    payFrequency = fields.String()
    fullTimeHoursWeek = fields.Float()
    organisation = fields.Integer()
    paidToDate = fields.String()
    paymentMethod = fields.String()
    bankAccountNumber = fields.String()
    taxNumber = fields.String()
    finishDate = fields.String()
    terminationReason = fields.String()
    taxCode = fields.String()
    taxScale = fields.String()
    kiwiSaverRate = fields.Float()
    employerSubsidy = fields.Float()
    kiwiSaverOptOutDate = fields.String()
    existingKiwiSaverMember = fields.Boolean()
    deathBenefitSurname = fields.String()
    deathBenefitFirstName = fields.String()
    deathBenefitRecipient = fields.String()
    esctRate = fields.Float()
    specialTax = fields.Float()
    specialEarnerLevy = fields.Float()
    specialExtraPayRate = fields.Float()
    specialStudentLoan = fields.Float()
    userDefinedGroup = fields.String()
    helpDebt = fields.Boolean()
    medicareLevyVariationDeclaration = fields.Boolean()
    hasSpouse = fields.Boolean()
    incomeLessThanRelevantAmount = fields.Boolean()
    payrollTaxExempt = fields.Boolean()
    sfssDebt = fields.Boolean()
    dependentChildren = fields.Integer()
    surchargeIncrease = fields.Float()
    preferredName = fields.String()
    proprietorStatus = fields.String()
    contractorsAbn = fields.String()
    address = fields.Embedded(Address)


class EmployeeCustomField(Resource):
    category = fields.Integer()
    categoryName = fields.String()
    customFieldId = fields.Integer()
    name = fields.String()
    date = fields.String()
    description = fields.String()
    contact = fields.String()
    relationship = fields.String()
    phoneNumber = fields.String()
    email = fields.String()
    address = fields.String()
    hayPoints = fields.Integer()
    haysProfile = fields.Float()
    fte = fields.Float()
    finish = fields.String()
    start = fields.String()
    reportsTo = fields.String()
    reportsFrom = fields.String()
    contractHours = fields.Float()
    periodDays = fields.Float()
    contractEnd = fields.String()
    renumerationType = fields.String()
    annualBenefit = fields.String()


class LeaveBalanceType(Resource):
    leaveType = fields.String()
    name = fields.String()
    unit = fields.String()


class LeaveBalance(Resource):
    employeeId = fields.String()
    entitled = fields.Float()
    accrued = fields.Float()
    taken = fields.Float()
    balance = fields.Float()
    nextAnniversaryDate = fields.String()
    lastAnniversaryDate = fields.String()
    leaveBalanceType = fields.Embedded(LeaveBalanceType)


class LeaveEntitlementRule(Resource):
    startsAfterYears = fields.Integer()
    startsAfterMonths = fields.Integer()
    frequencyYears = fields.Integer()
    frequencyMonths = fields.Integer()
    entitlementDays = fields.Float()
    entitlementMaxDays = fields.Float()
    leaveAccrualMethod = fields.String()
    accrualPercentage = fields.String()


class LeaveRequest(Resource):
    employeeId = fields.String()
    requestId = fields.Integer()
    hours = fields.Float()
    days = fields.Float()
    leaveFromDate = fields.String()
    leaveToDate = fields.String()
    reason = fields.String()
    status = fields.String()
    payElement = fields.String()
    payElementId = fields.Integer()
    leaveBalanceType = fields.Embedded(LeaveBalanceType)


class PayElementRate(Resource):
    reportingGroupName = fields.String()
    description = fields.String()
    taxablePayPerWeek = fields.Float()
    weeklyRate = fields.Float()
    hoursPerWeek = fields.Float()
    rate = fields.Float()
    multiplier = fields.Float()
    years = fields.Float()


class PayElement(Resource):
    code = fields.String()
    description = fields.String()
    displayValue = fields.String()
    calculationRule = fields.String()
    group = fields.String()
    type = fields.String()
    multiplier = fields.Float()
    rateAmount = fields.String()
    expired = fields.Boolean()
    accLevyLiable = fields.Boolean()
    superableEarning = fields.Boolean()
    holidayPayLiable = fields.Boolean()
    notKiwiSaverLiable = fields.Boolean()
    payrollTaxLiable = fields.Boolean()
    rdoLiable = fields.Boolean()
    lslLiable = fields.Boolean()
    casLiable = fields.Boolean()
    reducing = fields.Boolean()
    payableOnFinalPay = fields.Boolean()
    itemisedOnPaymentSummary = fields.Boolean()
    allowPartialDeduction = fields.Boolean()
    consolidateTransactions = fields.Boolean()
    payeeReference = fields.String()
    payeeCode = fields.String()
    bankAccountNumber = fields.String()
    bsbAccountNumber = fields.String()
    reduceSuperable = fields.Boolean()
    priority = fields.Integer()
    costCentresRule = fields.String()
    paymentMethod = fields.String()
    payeeParticulars = fields.String()
    doneAddress = fields.String()
    doneeName = fields.String()
    unusedLeavePayment = fields.Boolean()
    employmentTerminationPayment = fields.Boolean()
    employmentTerminationPaymentNoLumpD = fields.Boolean()
    availableForLeaveRequest = fields.Boolean()
    leaveTaxType = fields.String()
    paymentGroup = fields.String()
    calculationAccumulator = fields.String()
    debitCostCentreRule = fields.String()
    excessRedundancy = fields.String()
    derivedFrom = fields.String()
    customField = fields.String()
    rules = fields.Collection(LeaveEntitlementRule)
    rates = fields.Collection(PayElementRate)
    leaveBalanceType = fields.Embedded(LeaveBalanceType)


class PayRate(Resource):
    hourlyRate = fields.Float()
    annualRate = fields.Float()
    rate = fields.Float()
    code = fields.String()
    divisor = fields.String()
    payScaleCode = fields.String()


class PayrollPayFrequency(IpayrollModel):
    payFrequency = fields.String()
    paidToDate = fields.String()
    included = fields.Boolean()


class Payroll(Resource):
    payrollNumber = fields.String()
    payDate = fields.String()
    message = fields.String()
    status = fields.String()
    payrollType = fields.String()
    payFrequencies = fields.Embedded(PayrollPayFrequency)


class PayslipLeaveBalance(Resource):
    balanceName = fields.String()
    hours = fields.Float()
    days = fields.Float()
    amount = fields.Float()


class PayslipPayroll(Resource):
    payrollNumber = fields.String()
    payDate = fields.String()
    message = fields.String()


class PayslipPayrollEmployeeTransaction(Resource):
    amount = fields.Float()
    quantity = fields.Float()
    charity = fields.String()
    description = fields.String()
    notes = fields.String()
    displayPayslipQuantity = fields.String()


class PayslipTransaction(Resource):
    description = fields.String()
    quantity = fields.Float()
    amount = fields.Float()
    notes = fields.String()
    displayQuantity = fields.String()


class TimesheetTransaction(Resource):
    timesheetTransactionId = fields.Integer()
    amount = fields.Float()
    quantity = fields.Float()
    rate = fields.Float()
    description = fields.String()
    costCentre = fields.String()
    reason = fields.String()
    leaveFrom = fields.String()
    leaveTo = fields.String()
    leaveDays = fields.String()
    payElement = fields.String()


class Timesheet(Resource):
    employeeId = fields.String()
    daysInPeriod = fields.Float()
    totalHours = fields.Float()
    paidToDate = fields.String()
    paidFromDate = fields.String()
    message = fields.String()
    transactions = fields.Collection(TimesheetTransaction)


class YearToDateTotalsEntry(Resource):
    key = fields.String()
    yearToDateTotals = fields.Integer()


class Payslip(Resource):
    totalPayments = fields.Float()
    overpayment = fields.Float()
    taxCredit = fields.Float()
    yearToDateTotals = fields.Collection(YearToDateTotalsEntry)
    nettPay = fields.String()
    abn = fields.String()
    payslipMessage = fields.String()
    deductions = fields.Collection(PayslipPayrollEmployeeTransaction)
    otherBenefits = fields.Collection(PayslipPayrollEmployeeTransaction)
    leaveBalances = fields.Collection(PayslipLeaveBalance)
    timesheet = fields.Embedded(Timesheet)
    payments = fields.Collection(PayslipTransaction)
    payroll = fields.Embedded(PayslipPayroll)


class CostCentres(Resources):
    content = fields.Collection(CostCentre)


class EmployeeCustomFields(Resources):
    content = fields.Collection(EmployeeCustomField)


class Employees(Resources):
    content = fields.Collection(Employee)


class PayRates(Resources):
    content = fields.Collection(PayRate)


class PayElements(Resources):
    content = fields.Collection(PayElement)


class LeaveBalances(Resources):
    content = fields.Collection(LeaveBalance)


class LeaveRequests(Resources):
    content = fields.Collection(LeaveRequest)


class Payrolls(Resources):
    content = fields.Collection(Payroll)


class Payslips(Resources):
    content = fields.Collection(Payslip)


class Timesheets(Resources):
    content = fields.Collection(Timesheet)
