from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Initialize the WebDriver (assuming you've set up the environment)
driver = webdriver.Chrome()

# Navigate to the sample page
# file_url = "C:\\Github\\python-selenium-radio-buttons-test\\resources\\index-by-id.html"

# Building relative path to HTML project file at ../resources/index.html and navegating to project page
base_path = os.path.dirname(__file__) 
file_path = os.path.join(base_path, '..', 'resources', 'index.html')
file_url = 'file://' + os.path.abspath(file_path)
driver.get(file_url)

# Locate the radio button by ID and click it
stgenv_radio_button = driver.find_element(By.ID, "stg-env")
stgenv_radio_button.click()

# Close the WebDriver
driver.quit()
