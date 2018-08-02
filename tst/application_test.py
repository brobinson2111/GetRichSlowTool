import unittest

from .context import application

class ApplicationTest(unittest.TestCase):

    def test_run(self):
        application.Application().run()