import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys




class testEmployeeSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/Anitha/Desktop/A4P2test/venv/Scripts/chromedriver.exe")

    def test_blog(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://anithadowntimetracker.herokuapp.com/accounts/login/?next=/home")

        #Login
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("testEmp")
        time.sleep(1)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys("test@2019")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]")
        elem.click()
        time.sleep(0.5)
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/div/div/div[2]/ul[1]/li[2]/a")
        elem.click()
        time.sleep(1)

        #Add Downtime
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_id")
        elem.send_keys("D595")
        time.sleep(1)
        elem = driver.find_element_by_id("id_machine")
        elem.send_keys("Machine1")
        time.sleep(1)
        elem = driver.find_element_by_id("id_employee")
        elem.send_keys("testEmp")
        time.sleep(1)
        elem = driver.find_element_by_id("id_stoppage")
        elem.send_keys("OilChange")
        time.sleep(1)
        elem = driver.find_element_by_id("id_date")
        elem.send_keys("2019-10-10")
        time.sleep(1)
        elem = driver.find_element_by_id("id_startTime")
        elem.send_keys("1:00:00")
        time.sleep(1)
        elem = driver.find_element_by_id("id_endTime")
        elem.send_keys("3:00:00")
        time.sleep(1)
        elem = driver.find_element_by_id("id_stoppageHours")
        elem.send_keys("2")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
        elem.click()
        time.sleep(1)

        #Edit Downtime
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[2]/td[9]/a")
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_machine")
        elem.send_keys("Anitha")
        elem = driver.find_element_by_id("id_stoppage")
        elem.send_keys("Washing")
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
        elem.click()
        time.sleep(1)

        # Logout
        elem = driver.find_element_by_xpath("/html/body/nav/div/div/div/div/div[2]/ul[2]/ul/li/a")
        elem.click()
        time.sleep(.5)


def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()





