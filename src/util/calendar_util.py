'''
Created on August 2nd, 2018
Created By: Brandon Robinson (brobinson2111)
'''

import datetime

"""
Returns a datetime object that represents number_of_days in the future from today's datetime

:number_of_days The amount of days in the future for which the datetime is requested
"""
def days_from_today(number_of_days):
    return datetime.datetime.today() + datetime.timedelta(days=number_of_days)

"""
Shifts the date provided if it is in fact a weekend day. If it is a Saturday it will move back to a Friday.
If it is a Sunday, it will move forward to a Monday.

:datetime_value the provided datetime to account for a weekend.
"""
def account_for_weekend(datetime_value):
    # If Saturday, move back to Friday
    if(datetime_value.weekday() == 5):
        return datetime_value - datetime.timedelta(days=1)
    # If Sunday, move forward to Monday
    elif(datetime_value.weekday() == 6):
        return datetime_value + datetime.timedelta(days=1)
    return datetime_value