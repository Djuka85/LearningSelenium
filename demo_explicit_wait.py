import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class DemoExplicitWait:

    def demo_explicit_wait(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/ae")

        depart_from = driver.find_element_by_xpath("//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)
        time.sleep(3)
        going_to = driver.find_element_by_xpath("//input[@id='BE_flight_arrival_city']")
        going_to.click()
        going_to.send_keys("New")

        search_results = driver.find_elements_by_xpath("//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        for result in search_results:
            print(result.text)
            if "New York (JFK)" in result.text:
                result.click()
                break

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='BE_flight_origin_date']"))).click()
        """departure_date = driver.find_element_by_xpath("//label[@for='BE_flight_origin_date']")
        departure_date.click()"""

        all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']" )))\
            .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        #all_dates = driver.find_elements_by_xpath("//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "03/09/2021":
                date.click()
                time.sleep(2)
                break

        driver.find_element_by_xpath("//input[@value='Search Flights']").click()





demowait = DemoExplicitWait()
demowait.demo_explicit_wait()



