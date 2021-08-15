import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class DemoDropDown:

    def demo_dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/eu/form/signup/freetrial-sales-pe/?d=70130000000EqoP")
        drop_down = driver.find_element_by_xpath("//select[contains(@name,'CompanyEmployees')]")
        dd_values = Select(drop_down)

        time.sleep(3)
        dd_values.select_by_value("150")

        time.sleep(3)
        dd_values.select_by_index(2)

        time.sleep(3)
        dd_values.select_by_visible_text("2,000+ employees")


demo_select = DemoDropDown()
demo_select.demo_dropdown()
