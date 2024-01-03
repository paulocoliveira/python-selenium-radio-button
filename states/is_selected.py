from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the sample page
driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")

# Locate the "Male" radio button
male_radio_button = driver.find_element(By.XPATH, "//input[@value='Male']")
male_radio_button.click()

# Check if the "Male" radio button is selected
if male_radio_button.is_selected():
    print("The 'Male' radio button is selected.")
else:
    print("The 'Male' radio button is not selected.")

# Close the WebDriver
driver.quit()
