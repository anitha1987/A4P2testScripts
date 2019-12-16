import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys




class testEmployee(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/Anitha/Desktop/A4P2test/venv/Scripts/chromedriver.exe")

    def test_blog(self):
        driver = self.driver
        driver.maximize_window()

        driver.get("https://anithadowntimetracker.herokuapp.com/admin/login/?next=/admin/")

        #Log in
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("anitha")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("anitha1a")
        time.sleep(1)
        elem = driver.find_element_by_xpath("// *[ @ id = \"login-form\"] / div[3] / input")
        elem.click()
        time.sleep(1)

        #Add Employee
        elem = driver.find_element_by_xpath("// *[ @ id = \"content-main\"] / div / table / tbody / tr[2] / td[1] / a")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_user")
        elem.send_keys("aEmp")
        time.sleep(1)
        elem = driver.find_element_by_id("id_id")
        elem.send_keys("E999")
        time.sleep(1)
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("testEmp")
        time.sleep(1)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("xEmp@gmail.com")
        time.sleep(1)
        elem = driver.find_element_by_xpath("// *[ @ id = \"employee_form\"] / div / div / input[1]")
        elem.click()
        time.sleep(1)

        # Delete Employee
        elem = driver.find_element_by_xpath("//*[@id=\"result_list\"]/tbody/tr[1]/th/a")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"employee_form\"]/div/div/p/a")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"content\"]/form/div/input[2]")
        elem.click()
        time.sleep(1)

        #Logout
        elem = driver.find_element_by_xpath("// *[ @ id = \"user-tools\"] / a[3]")
        elem.click()
        time.sleep(.5)


def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()


