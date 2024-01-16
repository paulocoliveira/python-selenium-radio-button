from selenium.webdriver.common.by import By
import os

def test_locate_radio_button_by_css_and_click(driver):
    # Navigate to the sample page
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    
    # Locate the radio button by CSS selector and click it
    female_radio_button = driver.find_element(By.CSS_SELECTOR, "input[value='Female']")
    female_radio_button.click()

def test_locate_radio_button_by_id_and_click(driver):
    # Building relative path to HTML project file at ../resources/index.html and navegating to project page
    base_path = os.path.dirname(__file__) 
    file_path = os.path.join(base_path, '..', 'resources', 'index.html')
    file_url = 'file://' + os.path.abspath(file_path)
    driver.get(file_url)

    # Locate the radio button by ID and click it
    stgenv_radio_button = driver.find_element(By.ID, "stg-env")
    stgenv_radio_button.click()


def test_locate_radio_button_by_name_and_click(driver):
    # Navigate to the sample page
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    
    # Locate the radio button by name and click it
    female_radio_button = driver.find_elements(By.NAME, "optradio")[1]
    female_radio_button.click()