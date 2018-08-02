import datetime
import unittest

from tst.context import calendar_util

class CalendarUtilTest(unittest.TestCase):

    def setUp(self):
        self.calendar_util = calendar_util.CalendarUtil()

    def test_days_from_today(self):
        expected_day = datetime.date.today().day + 5
        actual_datetime = self.calendar_util.days_from_today(5)
        self.assertEqual(expected_day, actual_datetime.day)