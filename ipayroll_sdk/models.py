from booby import Model, fields


class IpayrollModel(Model):
    other = {}

    def __setitem__(self, k, v):
        if k not in self._fields:
            self.other[k] = v
        setattr(self, k, v)


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
    costCentreId = fields.Integer()
    code = fields.String()
    description = fields.String()
    displayValue = fields.String()


class Address(Resource):
    addressLine1 = fields.String()
    addressLine2 = fields.String()
    suburb = fields.String()
    city = fields.String()
    postCode = fields.String()
    country = fields.String()


class Employee(Resource):
    employeeId = fields.String()
    surname = fields.String()
    firstNames = fields.String()
    startDate = fields.String()
    birthDate = fields.String()
    paidToTate = fields.String()
    defaultCostCentre = fields.String()
    email = fields.String()
    phone = fields.String()
    title = fields.String()
    workState = fields.String()
    gender = fields.String()
    payFrequency = fields.String()
    fullTimeHoursWeek = fields.Float()
    organisation = fields.Integer()
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
    specialExtraPayRate = fields.String()
    specialStudentLoan = fields.Float()
    userDefinedGroup = fields.String()
    isHelpDebt = fields.Boolean()
    isMedicareLevyVariationDeclaration = fields.Boolean()
    isHasSpouse = fields.Boolean()
    isIncomeLessThanRelevantAmount = fields.Boolean()
    isPayrollTaxExempt = fields.Boolean()
    isSfssDebt = fields.Boolean()
    dependentChildren = fields.Integer()
    surchargeIncrease = fields.Float()
    preferredName = fields.String()
    proprietorStatus = fields.String()
    contractorsAbn = fields.String()
    address = fields.Embedded(Address)


class EmployeeCustomField(Resource):
    # EmployeeResource
    category = fields.Integer()
    categoryName = fields.String()
    customFieldId = fields.Integer()
    name = fields.String
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

    leaveBalanceType = fields.Embedded(LeaveBalanceType)


class PayElementRate(Resource):
    reportingGroupName = fields.String()
    description = fields.String()
    rate = fields.Float()
    years = fields.Float()
    taxablePayPerWeek = fields.Float()
    hoursPerWeek = fields.Float()
    multiplier = fields.Float()


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
    rayableOnFinalPay = fields.Boolean()
    itemisedOnPaymentSummary = fields.Boolean()
    allowPartialDeduction = fields.Boolean()
    consolidateTransactions = fields.Boolean()
    payeeReference = fields.String()
    payeeCode = fields.String()
    bankAccountNumber = fields.String()
    bsbAccountNumber = fields.String()
    reduceSuperable = fields.Boolean()
    priority = fields.Integer()
    leaveBalanceType = fields.Embedded(LeaveBalanceType)
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
    rules = fields.Collection(LeaveEntitlementRule)
    derivedFrom = fields.String()
    calculationAccumulator = fields.String()
    debitCostCentreRule = fields.String()
    rates = fields.Collection(PayElementRate)
    excessRedundancy = fields.String()
    customField = fields.String()


class PayRate(Resource):
    hourlyRate = fields.Float()
    annualRate = fields.Float()
    rate = fields.Float()
    code = fields.String()
    divisor = fields.String()
    payScaleCode = fields.String()


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


class YearToDateTotalsEntry(Resource):
    key = fields.String()
    yearToDateTotals = fields.Integer()


# class TimecardActivity(Resource):
#     id = fields.Integer()
#     code = fields.String()
#     type = fields.String()
#
#
# class TimecardEmployee(Resource):
#     id = fields.String()
#     name = fields.String()
#     isInactive = fields.Boolean()
#
#
# class TimecardEntry(Resource):
#     id = fields.Integer()
#     date = fields.String()
#     startTime = fields.String()
#     endTime = fields.String()
#     status = fields.String()
#     hours = fields.Float()
#     version = fields.Integer()
#     linkedResourceId = fields.Integer()  # Long
#     isCreatedByKiosk = fields.Boolean()  # Long
#     kioskNote = fields.String()
#     approverNote = fields.String()
#     breakMinutes = fields.Float()
#     hoursWorked = fields.Float()
#     isOnlyLeaveRequests = fields.Boolean()
#     employee = fields.Embedded(TimecardEmployee)
#     createdBy = fields.Embedded(TimecardEmployee)
#     activity = fields.Embedded(TimecardActivity)
#
#
# class TimecardLog(Resource):
#     employee = fields.Embedded(TimecardEmployee)
#     date = fields.String()
#     standardHours = fields.Float()
#     ordinaryHours = fields.Float()
#     additionalHours = fields.Float()
#     status = fields.String()
#     # Map<Long, Integer> getEntryIds();
#     timeCode = fields.String()
#     isLeavePendingExists = fields.Boolean()
#     isOnlyLeaveRequestss = fields.Boolean()
#     isOnlyNonActionableEntriess = fields.Boolean()
#
#
# class TimecardSetting(Resource):
#     isActivityEnabled = fields.Boolean()
#     isTimesEnabled = fields.Boolean()
#     isLeaveRequestsOnlineEnabled = fields.Boolean()


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


class Payslips(Resources):
    content = fields.Collection(Payslip)


# class TimecardEntries(Resources):
#     content = fields.Collection(TimecardEntry)


class Timesheets(Resources):
    content = fields.Collection(Timesheet)
