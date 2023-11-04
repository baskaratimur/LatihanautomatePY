import unittest
from TestCase.ActionsHomepage import TestVerifyHomepage
from TestCase.ActionsNavbar import TestClickNavbar

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestVerifyHomepage))
    suite.addTest(unittest.makeSuite(TestClickNavbar))
    runner = unittest.TextTestRunner()
    runner.run(suite)