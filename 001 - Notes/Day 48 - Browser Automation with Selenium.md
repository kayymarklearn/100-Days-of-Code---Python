d2026-02-28 21:41

Status: Incomplete

Tags: [[Day 45 - Web Scraping with Beautiful Soup]]
[[Day 48 - Browser automation with selenium (Code)]]

# **Selenium Webdriver**
> To use, first install selenium with your package manager of choice.
> ```
> from selenium import webdriver
> # Keep Chrome browser open after program finishes
> chrome_options = webdriver.ChromeOptions()
> chrome_options.add_experimental_option("detach", True)
> driver = webdriver.Chrome(options=chrome_options) # Use same for other browsers .Firefox(), .Edge()
> # so we've basically initialized a new Chrome browser object.
> driver.get("https://www.amazon.com) # Open a browser tab and get the given url.
> # We notice that the tab closes immediately the site loads.
> # This can be fixed by setting chrome options
> ```

##### Code snippet
```
from re import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.amazon.com/Amazon-Basics-Compatible-Adaptive-Response/dp/B0CP7SV7XV/ref=sr_1_1_ffob_sspa?_encoding=UTF8&content-id=amzn1.sym.edf433e2-b6d4-408e-986d-75239a5ced10&dib=eyJ2IjoiMSJ9.57WXLfVt_7dw-PioabOSfdRxEwuBdnSohhjJfDE5xCyKVnEn6WGC_Z6SUJNOgJt1hZ64EMennQvJHtGrt7UceQIaE6WWbVirBFpxuTlXln4HfrbPL3MaPTukT6s43LLoRunWVP7PEvni02BfaO9PhfsOJ8WzxqxzANiwaYL1LlNeypGhfG6zHiAmnB-iCVGUQnRuVcXsiAyXeStqMzitQxKKs8ewjAhhZkJGNcB50UQ.6rHmKCgW-x3y9pftrvl51rcUEvF6WYXTXuFRLjqyIT8&dib_tag=se&keywords=gaming&pd_rd_r=43adaf62-df3a-46c8-8335-f040fbc216dd&pd_rd_w=7WcuO&pd_rd_wg=LMcC5&qid=1772316567&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(URL) # Open amazon.com

wait = WebDriverWait(driver, 10)  # 10 = max seconds to wait

	element = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
)

price_cedi = driver.find_element(By.CLASS_NAME, value="a-price-whole") # Find an element using the class name
price_pesewa = driver.find_element(By.CLASS_NAME, value="a-price-fraction") # Find an element using the class name
print(f"The price is {price_cedi.text}.{price_pesewa.text}")
print(price_cedi.tag_name)
print(price_pesewa.get_attribute("class"))
"""
    We can also find elements by:
    NAME, ID, CLASS NAME and CSS SELECTOR
    We can also access the attributes by using the dot notation.
    As well as get the values of attributes by using the get_attribute() method.
    If all else fails:
        We can use the XPath to find and select an element. (this can be used to find
        elements without a lot fo specificity i.e, class names, ID or name attributes).
"""
driver.quit() # close the browser
```

## Interacting with web pages (filling forms, clicking ...)
> To click on an element, call the click() method on it.
> ```
> button.click()
> Because clicking on links is so common, selenium has a way to select links by their text to make selection easier. using the By.LINK_TEXT, this is specific to links.
> ```
> To send input to a textbox use the send_keys() method on it.
> ```
> search.send_keys("Hello"_)
> For sending commmannds # like Return
> we need to import Keys class
> from selenium.webdriver.common.keys import Keys (This class basically contains keycodes for a lot if not all the keys on the keyboards)
> ```

## References
