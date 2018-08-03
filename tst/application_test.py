'''
Created on August 2nd, 2018
Created By: Brandon Robinson (brobinson2111)
'''

import unittest
import os

from .context import application

class ApplicationTest(unittest.TestCase):

    def test_run(self):
        total_capitol = 10000
        number_of_days_to_spend = 100
        output_location = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/results.txt'
        application.Application(total_capitol, number_of_days_to_spend, output_location).run()