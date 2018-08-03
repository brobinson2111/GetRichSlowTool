'''
Created on August 2nd, 2018
Created By: Brandon Robinson (brobinson2111)
'''

import unittest

from .context import application

class ApplicationTest(unittest.TestCase):

    def test_run(self):
        application.Application().run()