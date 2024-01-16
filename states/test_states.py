from selenium.webdriver.common.by import By

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