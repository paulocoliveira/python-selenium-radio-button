from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the sample page
driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")

# Locate a disabled radio button by its attribute (assuming it's disabled)
disabled_radio_button = driver.find_element(By.XPATH, "//input[@value='RadioButton3']")

# Check if the radio button is disabled
if disabled_radio_button.is_enabled():
    print("The radio button is enabled.")
else:
    print("The radio button is disabled.")

# Close the WebDriver
driver.quit()
