'''
Created on August 30th, 2018
Created By: Brandon Robinson (brobinson2111)
'''

import unittest
import datetime

from tst.context import transaction_schedule_info

class TransactionScheduleInfoTest(unittest.TestCase):

    def test_construct(self):
        expected_security_name = 'Microsoft'
        expected_number_of_shares = 10
        expected_datetime = datetime.datetime.now()

        actual_transaction_schedule_info = transaction_schedule_info.TransactionScheduleInfo(
            expected_security_name, expected_number_of_shares, expected_datetime)

        self.assertEqual(expected_security_name, actual_transaction_schedule_info.security_name)
        self.assertEqual(expected_number_of_shares, actual_transaction_schedule_info.number_of_shares)
        self.assertEqual(expected_datetime, actual_transaction_schedule_info.datetime)