import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



class testSupervisor(unittest.TestCase):

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
        time.sleep(0.5)
        elem = driver.find_element_by_xpath("// *[ @ id = \"login-form\"] / div[3] / input")
        elem.click()
        time.sleep(1)

        # Add Supervisor
        elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div/table/tbody/tr[4]/td[1]/a")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_user")
        elem.send_keys("aSup")
        time.sleep(1)
        elem = driver.find_element_by_id("id_id")
        elem.send_keys("S999")
        time.sleep(1)
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("xSup")
        time.sleep(1)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("xSup@gmail.com")
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"supervisor_form\"]/div/div/input[1]")
        elem.click()
        time.sleep(1)

        # Delete Supervisor
        elem = driver.find_element_by_xpath("//*[@id=\"result_list\"]/tbody/tr[1]/th/a")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"supervisor_form\"]/div/div/p/a")
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
