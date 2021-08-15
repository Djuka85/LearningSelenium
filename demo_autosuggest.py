import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class DemoAutosuggest:

    def demo_autosuggest_dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/ae")

        depart_from = driver.find_element_by_xpath("//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(3)

        going_to = driver.find_element_by_xpath("//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        time.sleep(4)

        search_results = driver.find_elements_by_xpath("//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        for result in search_results:
            print(result.text)
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(4)
                break

        departure_date = driver.find_element_by_xpath("//label[@for='BE_flight_origin_date']")
        departure_date.click()
        time.sleep(4)
        """
        driver.find_element_by_xpath("//td[@id='21/07/2021']").click()
        time.sleep(4)"""

        all_dates = driver.find_elements_by_xpath("//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "03/07/2021":
                date.click()
                time.sleep(3)
                break





dauto = DemoAutosuggest()
dauto.demo_autosuggest_dropdown()



