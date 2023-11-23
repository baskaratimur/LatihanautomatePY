import unittest
from TestCase.ActionsHomepage import TestVerifyHomepage
from TestCase.ActionsNavbar import TestClickNavbar
from TestCase.TestActions import TestCLickActions

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestVerifyHomepage))
    suite.addTest(unittest.makeSuite(TestClickNavbar))
    suite.addTest(unittest.makeSuite(TestCLickActions))
    runner = unittest.TextTestRunner()
    runner.run(suite)