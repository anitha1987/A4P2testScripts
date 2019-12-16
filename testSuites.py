import unittest
from unittest import TestLoader, TestSuite, TextTestRunner
from admin_Login_Logout import testLoginLogout
from admin_Add_Delete_User  import testUser
from admin_Add_Delete_Employee import testEmployee
from admin_Add_Delete_Supervisor import testSupervisor
from site_Employee_features import testEmployeeSite
from site_Supervisor_features import testSupervisorSite




if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(testLoginLogout),
        loader.loadTestsFromTestCase(testUser),
        loader.loadTestsFromTestCase(testEmployee),
        loader.loadTestsFromTestCase(testSupervisor),
        loader.loadTestsFromTestCase(testEmployeeSite),
        loader.loadTestsFromTestCase(testSupervisorSite),

    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)




































