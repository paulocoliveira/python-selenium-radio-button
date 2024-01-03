from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the sample page
driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")

# Locate the radio button by CSS selector and click it
female_radio_button = driver.find_element(By.CSS_SELECTOR, "input[value='Female']")
female_radio_button.click()

# Close the WebDriver
driver.quit()