import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class testSupervisorSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/Anitha/Desktop/A4P2test/venv/Scripts/chromedriver.exe")

    def test_blog(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://anithadowntimetracker.herokuapp.com/accounts/login/?next=/home")

        # Login
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("testSup")
        time.sleep(1)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("test@2020")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/div/div/div[2]/ul[1]/li[2]/a")
        elem.click()
        time.sleep(1)

        # Add Machine
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_id")
        elem.send_keys("M393")
        time.sleep(1)
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("Machine9")
        time.sleep(1)
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("Machine - food processing")
        time.sleep(1)
        elem = driver.find_element_by_id("id_supervisor")
        elem.send_keys("testSup")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
        elem.click()
        time.sleep(1)

        # Edit Downtime
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[2]/td[5]/a")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("Machine used for fermentation")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
        elem.click()
        time.sleep(1)

        #Delete Machine
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[3]/td[6]/a")
        elem.click()
        time.sleep(1)
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        time.sleep(1)

        #View Summary
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[7]/a")
        elem.click()
        time.sleep(1)

        # Logout
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/div/div/div[2]/ul[2]/ul/li/a")
        elem.click()
        time.sleep(1)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()





