import unittest
from  BasePage import BasePage

class DefaulTest(unittest.TestCase):
    def setUp(self):
        print('Start Testing')


    def tearDown(self):
        # BasePage.browser_quit()
        print('End Testing')





