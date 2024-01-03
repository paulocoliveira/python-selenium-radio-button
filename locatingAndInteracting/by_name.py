from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the sample page
driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")

# Locate the radio button by name and click it
female_radio_button = driver.find_elements(By.NAME, "optradio")[1]
female_radio_button.click()

# Close the WebDriver
driver.quit()
