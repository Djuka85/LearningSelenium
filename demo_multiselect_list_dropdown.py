import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class DemoDropDown:

    def demo_dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
        dd_demo = driver.find_element_by_id("multi-select")
        dd_multiselect = Select(dd_demo)

        dd_multiselect.select_by_index(1)
        time.sleep(2)
        dd_multiselect.select_by_value("Ohio")
        time.sleep(2)
        dd_multiselect.select_by_visible_text("Washington")
        time.sleep(3)

        dd_multiselect.deselect_by_index(1)
        time.sleep(2)


demo_multiselect = DemoDropDown()
demo_multiselect.demo_dropdown()
