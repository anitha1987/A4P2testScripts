import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



class testUser(unittest.TestCase):

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
        time.sleep(0.5)

        #Add User
        elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[2]/table/tbody/tr[5]/th/a")
        elem.click()
        time.sleep(0.5)
        elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/ul/li/a")
        elem.click()
        time.sleep(0.5)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("xtest_USer")
        time.sleep(0.5)
        elem = driver.find_element_by_id("id_password1")
        elem.send_keys("anitha_User")
        time.sleep(0.5)
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys("anitha_User")
        time.sleep(0.5)
        elem = driver.find_element_by_xpath("//*[@id=\"user_form\"]/div/div/input[1]")
        elem.click()
        time.sleep(0.5)
        driver.get("https://anithadowntimetracker.herokuapp.com/admin/downtimeApp/user/")
        time.sleep(0.5)

        #Delete User
        elem = driver.find_element_by_xpath("//*[@id=\"result_list\"]/tbody/tr[5]/th/a")
        elem.click()
        time.sleep(0.5)
        elem = driver.find_element_by_xpath("//*[@id=\"user_form\"]/div/div/p/a")
        elem.click()
        time.sleep(0.5)
        elem = driver.find_element_by_xpath("//*[@id=\"content\"]/form/div/input[2]")
        elem.click()
        time.sleep(0.5)

def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()