from selenium.webdriver.common.by import By

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