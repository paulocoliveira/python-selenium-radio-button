from selenium.webdriver.common.by import By
def test_locate_radio_button_by_id_and_click(driver):
    # Navigate to the sample page   
    driver.get("https://paulocoliveira.github.io/mypages/radiobuttons.html")
    
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
    # Navigate to the radio button demo page (same as the first test case)
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    
    # Locate the radio button by XPath and click it
    male_radio_button = driver.find_element(By.XPATH, "//input[@value='Male']")
    male_radio_button.click()

def test_locate_radio_button_by_css_and_click(driver):
    # Navigate to the sample page    
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    
    # Locate the radio button by CSS selector and click it
    female_radio_button = driver.find_element(By.CSS_SELECTOR, "input[value='Female']")
    female_radio_button.click()