'''
Created on August 2nd, 2018
Created By: Brandon Robinson (brobinson2111)
'''

import datetime
import unittest

from tst.context import calendar_util

class CalendarUtilTest(unittest.TestCase):

    def test_days_from_today(self):
        expected_day = datetime.date.today().day + 5
        actual_datetime = calendar_util.days_from_today(5)
        self.assertEqual(expected_day, actual_datetime.day)

    def test_account_for_weekend_weekday(self):
        timestamp = 1533085072
        test_datetime = datetime.datetime.utcfromtimestamp(timestamp)
        self.assertEqual(test_datetime, calendar_util.account_for_weekend(test_datetime))

    def test_account_for_weekend_saturday(self):
        timestamp = 1533344658
        test_datetime = datetime.datetime.utcfromtimestamp(timestamp)
        actual_datetime = calendar_util.account_for_weekend(test_datetime)
        self.assertNotEqual(test_datetime, actual_datetime)
        self.assertEqual(4, actual_datetime.weekday())

    def test_account_for_weekend_sunday(self):
        timestamp = 1533449058
        test_datetime = datetime.datetime.utcfromtimestamp(timestamp)
        actual_datetime = calendar_util.account_for_weekend(test_datetime)
        self.assertNotEqual(test_datetime, actual_datetime)
        self.assertEqual(0, actual_datetime.weekday())