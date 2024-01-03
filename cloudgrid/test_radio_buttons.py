import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser
import os

# Load the configuration file
config = configparser.ConfigParser()
config.read('config/config.ini')

@pytest.fixture()
def driver():
    # Initialize the WebDriver
    username = os.getenv("LT_USERNAME")
    accessKey = os.getenv("LT_ACCESS_KEY")

    gridUrl = config.get('CLOUDGRID', 'grid_url')

    web_driver = webdriver.ChromeOptions()
    platform = config.get('ENV', 'platform')
    browser_name = config.get('ENV', 'browser_name')

    lt_options = {
        "user": username,
        "accessKey": accessKey,
        "build": config.get('CLOUDGRID', 'build_name'),
        "name": config.get('CLOUDGRID', 'test_name'),
        "platformName": platform,
        "w3c": config.get('CLOUDGRID', 'w3c'),
        "browserName": browser_name,
        "browserVersion": config.get('CLOUDGRID', 'browser_version'),
        "selenium_version": config.get('CLOUDGRID', 'selenium_version'),
		"visual": True
    }

    options = web_driver
    options.set_capability('LT:Options', lt_options)

    url = f"https://{username}:{accessKey}@{gridUrl}"
    
    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    yield driver
    
    # Close the WebDriver
    driver.quit

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

def test_locate_radio_button_by_xpath_and_click(driver):
    # Navigate to the sample page
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    
    # Locate the radio button by XPath and click it
    female_radio_button = driver.find_element(By.XPATH, "//input[@value='Female']")
    female_radio_button.click()

def test_check_hidden_radio_button_fail(driver):
    # Building relative path to HTML project file at ../resources/index.html and navegating to project page
    base_path = os.path.dirname(__file__) 
    file_path = os.path.join(base_path, '..', 'resources', 'index.html')
    file_url = 'file://' + os.path.abspath(file_path)
    driver.get(file_url)

    # Attempt to locate the radio button by ID and attempt to click it
    hidden_radio_button = driver.find_element(By.ID, "hidden-env")

    # Attempt to click the radio button
    hidden_radio_button.click()

def test_check_hidden_radio_button_pass(driver):
    # Building relative path to HTML project file at ../resources/index.html and navegating to project page
    base_path = os.path.dirname(__file__) 
    file_path = os.path.join(base_path, '..', 'resources', 'index.html')
    file_url = 'file://' + os.path.abspath(file_path)
    driver.get(file_url)

    # Toggle the visibility of the hidden option
    toggle_button = driver.find_element(By.ID, "toggle-hidden")
    toggle_button.click()
    print("The radio button is being displayed now.")

    # Attempt to locate the radio button by ID and attempt to click it
    hidden_radio_button = driver.find_element(By.ID, "hidden-env")

    # Attempt to click the radio button
    hidden_radio_button.click()

def test_check_is_displayed(driver):
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

def test_check_is_enabled(driver):
    # Navigate to the sample page
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    
    # Locate a disabled radio button by its attribute (assuming it's disabled)
    disabled_radio_button = driver.find_element(By.XPATH, "//input[@value='RadioButton3']")
    
    # Check if the radio button is disabled
    if disabled_radio_button.is_enabled():
        print("The radio button is enabled.")
    else:
        print("The radio button is disabled.")

def test_check_is_selected(driver):
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

def test_get_selected_value(driver):
    # Navigate to the sample page
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")

    # Locate all radio buttons with the same name attribute
    radio_buttons = driver.find_elements(By.NAME, "optradio")

    # Click on the Female option
    radio_buttons[1].click()

    # Initialize a variable to store the selected option
    selected_option = None

    # Iterate through the radio buttons to find the selected one
    for radio_button in radio_buttons:
        if radio_button.is_selected():
            selected_option = radio_button.get_attribute("value")
            break

    # Check if a selected option was found
    if selected_option:
        print(f"The selected option is: {selected_option}")
    else:
        print("No option is selected.")
