import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class DemoHiddenElements:

    def demo_is_displayed(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        element = driver.find_element_by_xpath("//div[@id='myDIV']").is_displayed()
        print(element)

        driver.find_element_by_xpath("//button[normalize-space()='Toggle Hide and Show']").click()
        element2 = driver.find_element_by_xpath("//div[@id='myDIV']").is_displayed()
        print(element2)

    def demo_is_displayed_yatra(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/ae")
        driver.maximize_window()
        time.sleep(2)
        uae_flag = driver.find_element_by_xpath("//a[normalize-space()='UAE']")
        ind_flag = driver.find_element_by_xpath("//a[normalize-space()='IND']")
        action = ActionChains(driver)
        action.move_to_element(uae_flag).move_to_element(ind_flag).click().perform()
        time.sleep(3)

        driver.find_element_by_xpath("//span[@class='demo-icon icon-hotels']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//span[@class='txt-ellipses hotel_passengerBox travellerPaxBox']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//select[@class='ageselect']").is_displayed()
        print(elem)
        driver.find_element_by_xpath("//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()
        elem1 = driver.find_element_by_xpath("//select[@class='ageselect']").is_displayed()
        print(elem1)


demoDisplayed = DemoHiddenElements()
#demoDisplayed.demo_is_displayed()
demoDisplayed.demo_is_displayed_yatra()


