import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



class testLoginLogout(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome("C:/Users/Anitha/Desktop/A4P2test/venv/Scripts/chromedriver.exe")

    def test_blog(self):
        driver = self.driver
        driver.maximize_window()

        driver.get("https://anithadowntimetracker.herokuapp.com/admin/login/?next=/admin/")

        #Login
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("anitha")
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("anitha1a")
        time.sleep(0.5)
        elem = driver.find_element_by_xpath("// *[ @ id = \"login-form\"] / div[3] / input")
        elem.click()
        time.sleep(0.5)

        #logout
        elem = driver.find_element_by_xpath("// *[ @ id = \"user-tools\"] / a[3]")
        elem.click()
        time.sleep(0.5)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()