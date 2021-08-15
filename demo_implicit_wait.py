import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class DemoImplicitWait:

    def demo_implicit_wait(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/")
        driver.find_element(By.ID, "username").send_keys("Milos")
        driver.find_element(By.ID, "password").send_keys("Milos85")
        time.sleep(3)


impwait = DemoImplicitWait()
impwait.demo_implicit_wait()




