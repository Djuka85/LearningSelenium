import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoElementState:

    def demo_enable_disable(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("http://training.openspan.com/login")
        driver.find_element_by_xpath("//input[@id='user_name']").send_keys("abcd")
        driver.find_element_by_xpath("//input[@id='user_pass']").send_keys("1234")

        demo_state = driver.find_element_by_xpath("//input[@id='login_button']").is_enabled()
        print(demo_state)


demostate = DemoElementState()
demostate.demo_enable_disable()