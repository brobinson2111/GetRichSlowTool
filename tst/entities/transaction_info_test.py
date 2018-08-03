'''
Created on August 3rd, 2018
Created By: Brandon Robinson (brobinson2111)
'''

import unittest
import datetime

from tst.context import transaction_info

class TransactionInfoTest(unittest.TestCase):

    def test_construct(self):
        expected_number_of_shares = 10
        expected_datetime = datetime.datetime.now()

        actual_transaction_info = transaction_info.TransactionInfo(expected_number_of_shares, expected_datetime)

        self.assertEqual(expected_number_of_shares, actual_transaction_info.number_of_shares)
        self.assertEqual(expected_datetime, actual_transaction_info.datetime)