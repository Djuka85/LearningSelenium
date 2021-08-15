from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.rcvacademy.com")
driver.maximize_window()
print(driver.title)
driver.close()

