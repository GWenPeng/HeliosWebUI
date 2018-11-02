from enum import  Enum,unique

@unique
class Expense_Report_Type(Enum):
    daily_report_type=3001
    travel_report_type=3002
    special_report_type=3003
