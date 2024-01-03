from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the sample page
driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")

# Locate the "Male" radio button
male_radio_button = driver.find_element(By.XPATH, "//input[@value='Male']")

# Check if the "Male" radio button is being displayed and if yes, click on it
if male_radio_button.is_displayed():
    print("The 'Male' radio button is being displayed.")
    male_radio_button.click()
else:
    print("The 'Male' radio button is not being displayed.")
