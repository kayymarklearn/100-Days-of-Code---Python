2026-03-01 00:37

Status: Incomplete

Tags: [[Day 48 - Browser Automation with Selenium]]

# Code snippets and Examples

# Check the top 5 upcoming events on python.org
```
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)


upcoming_events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu a")
upcoming_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")


all_events = {}
for i in range(len(upcoming_dates)):

    all_events[i] = {"time": upcoming_dates[i].text, "name": upcoming_events[i].text}

print(all_events)

driver.quit()
```

# Check the total number of wikipedia articles in English
```
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

number_of_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')

print(number_of_articles.text)

driver.quit()
```

# Signup to practice site
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("Jeffrey")
lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("Peterson")
email = driver.find_element(By.CLASS_NAME, value="bottom")
email.send_keys("JeffPete@aol.com", Keys.ENTER)
```