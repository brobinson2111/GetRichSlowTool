'''
Created on August 2nd, 2018
Created By: Brandon Robinson (brobinson2111)
'''

import logging
import unittest
import json

from tst.context import logger_config
from tst.context import security_info

class SecurityInfoTest(unittest.TestCase):

    def setUp(self):
        logger_config.set(logging.getLogger('SecurityInfoTest'))

    def test_construct(self):
        security_configuration = json.loads(
        """
            {
                "name": "Amazon",
                "contribution": 0.50,
                "current_price": 100.00
            }
        """)
        total_capitol = 1000
        requested_length = 100

        actual_object = security_info.SecurityInfo(security_configuration, total_capitol, requested_length)

        self.assertEqual('Amazon', actual_object.name)
        self.assertEqual(5, actual_object.number_of_shares)
        self.assertEqual(5, actual_object.num_transactions)
        self.assertEqual(1, actual_object.batch_size)
        self.assertEqual(500.00, actual_object.actual_contribution)
        self.assertEqual(0.0, actual_object.excess)
        self.assertEqual(20, actual_object.frequency)
        self.assertEqual(5, len(actual_object.purchase_days))

    def test_construct_with_excess(self):
        security_configuration = json.loads(
        """
            {
                "name": "Apple",
                "contribution": 0.15,
                "current_price": 24.79
            }
        """)
        total_capitol = 1000
        requested_length = 100

        actual_object = security_info.SecurityInfo(security_configuration, total_capitol, requested_length)

        self.assertEqual('Apple', actual_object.name)
        self.assertEqual(6, actual_object.number_of_shares)
        self.assertEqual(6, actual_object.num_transactions)
        self.assertEqual(1, actual_object.batch_size)
        self.assertEqual(148.74, actual_object.actual_contribution)
        self.assertEqual(1.25, actual_object.excess)
        self.assertEqual(16, actual_object.frequency)
        self.assertEqual(6, len(actual_object.purchase_days))

    def test_construct_with_batch_size(self):
        security_configuration = json.loads(
        """
            {
                "name": "Microsoft",
                "contribution": 0.80,
                "current_price": 50.00
            }
        """)
        total_capitol = 100000
        requested_length = 100

        actual_object = security_info.SecurityInfo(security_configuration, total_capitol, requested_length)

        self.assertEqual('Microsoft', actual_object.name)
        self.assertEqual(1584, actual_object.number_of_shares)
        self.assertEqual(11, actual_object.num_transactions)
        self.assertEqual(144, actual_object.batch_size)
        self.assertEqual(79200.00, actual_object.actual_contribution)
        self.assertEqual(800.00, actual_object.excess)
        self.assertEqual(9, actual_object.frequency)
        self.assertEqual(11, len(actual_object.purchase_days))

    def test_construct_illegal_configuration(self):
        security_configuration = json.loads(
        """
            {
                "name": "Amazon",
                "contribution": 0.22,
                "current_price": 734.40
            }
        """)

        with self.assertRaises(Exception):
            security_info.SecurityInfo(security_configuration, 100, 100)

