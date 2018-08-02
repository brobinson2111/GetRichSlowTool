import unittest

from .context import application

class MainTest(unittest.TestCase):

    def test_run(self):
        application.Application().run()