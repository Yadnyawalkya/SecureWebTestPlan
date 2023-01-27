# Test to check potential path traversal
from selenium import webdriver

driver = webdriver.Firefox()

# Define a list of potential path traversal payloads
# You can get this list by accessing server
payloads = ["../../etc/passwd", "../..\../..\../etc/passwd", "../../../../etc/shadow", "../../var/www/html", "../../../.env"]

# Iterate through the payloads
for payload in payloads:
    url = "http://www.example.com/" + payload
    try:
        driver.get(url)
        if "File not found" in driver.page_source:
            print("Path traversal vulnerability found: " + payload)
        else:
            print("No vulnerability found for payload: " + payload)
    except:
        print("An error occurred while checking payload: " + payload)

driver.quit()
