from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_hidden_radio_button_fail(driver):
    # Navigate to the sample page 
    driver.get("https://paulocoliveira.github.io/mypages/radiobuttons.html")
    driver.maximize_window()
    
    # Explicit wait of 10 seconds
    wait = WebDriverWait(driver, 10)
    
    # Wait for 10 seconds till the Document State is not complete
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    
    # Attempt to locate the radio button by ID and attempt to click it
    hidden_radio_button = driver.find_element(By.ID, "hidden-env")
    
    # Attempt to click the radio button
    hidden_radio_button.click()

def test_check_hidden_radio_button_pass(driver):
    # Navigate to the sample page
    driver.get("https://paulocoliveira.github.io/mypages/radiobuttons.html")
    driver.maximize_window()
    
    # Explicit wait of 10 seconds
    wait = WebDriverWait(driver, 10)
    
    # Wait for 10 seconds till the Document State is not complete
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    
    # Toggle the visibility of the hidden option
    toggle_button = driver.find_element(By.ID, "toggle-hidden")
    toggle_button.click()
    
    # Attempt to locate the radio button by ID and attempt to click it
    hidden_radio_button = driver.find_element(By.ID, "hidden-env")
    
    # Attempt to click the radio button
    hidden_radio_button.click()
   
    print("The radio button is being displayed now.")