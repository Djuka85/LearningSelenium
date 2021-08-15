import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoGetAttributeValue:

    def demo_getvalue(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://yatra.com")
        attr_value = driver.find_element_by_xpath("//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        print(attr_value)



attrObj = DemoGetAttributeValue()
attrObj.demo_getvalue()