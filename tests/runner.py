import tests.test_common as test_common
import tests.test_user as test_user
import tests.test_admin as test_admin
import tests.test_birthdays as test_birthdays
import unittest


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_common.TestsCommonMethods))
    suite.addTest(unittest.makeSuite(test_user.TestsUserMethods))
    suite.addTest(unittest.makeSuite(test_admin.TestsAdminMethods))
    suite.addTest(unittest.makeSuite(test_birthdays.TestsBirthdaysMethods))
    print('[i] Count of tests: ' + str(suite.countTestCases()) + '\n')

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
