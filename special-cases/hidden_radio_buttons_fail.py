from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Initialize the WebDriver (assuming you've set up the environment)
driver = webdriver.Chrome()

# Building relative path to HTML project file at ../resources/index.html and navegating to project page
base_path = os.path.dirname(__file__) 
file_path = os.path.join(base_path, '..', 'resources', 'index.html')
file_url = 'file://' + os.path.abspath(file_path)
driver.get(file_url)

# Attempt to locate the radio button by ID and attempt to click it
hidden_radio_button = driver.find_element(By.ID, "hidden-env")

# Attempt to click the radio button
hidden_radio_button.click()

# Close the WebDriver
driver.quit()
