from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import lp_links



driver = webdriver.Chrome()
timeout = 5
linksPresent = False
reqSubStr = 'https://www.listingsproject.com/listings/'
links = []

driver.get(lp_links.base_url)
# Older selenium syntax
# driver.find_element_by_xpath("//input[@type='submit' and @value='something']").click()
# newer selenium synntax
# browser.find_element(By.XPATH, '//button[text()="Outliers"]')

try:
    driver.find_element(By.XPATH, '//button[text()="Ok, got it"]').click()
    driver.find_element(By.XPATH, '//input[@type="submit" and @value="I accept. Take me to the listings."]').click()
except:
    pass



try:
    element_present = EC.presence_of_element_located((By.XPATH, '//a[@href]'))
    WebDriverWait(driver, timeout).until(element_present)
    linksPresent = True
except TimeoutException:
    print('Timed out waiting for page to load')

if linksPresent:
    elems = driver.find_elements(By.XPATH, '//a[@href]')
    print(type(elems))
    print(len(elems))
    for elem in elems:
        elemLink = elem.get_attribute("href")
        if reqSubStr not in elemLink:
            place = elems.index(elem)
            elems.pop(place)
            continue
        # type: class 'selenium.webdriver.remote.webelement.WebElement'
        links.append(elemLink) # class 'str'
    
uniqueLinks = [*set(links)]
print(len(uniqueLinks))

me = input("say something")


'''

THIS WHOLE PY FILE LISTS UNIQUE URLS for LISTING

Wrap this in a method that returns the unique list. 

'''



#driver.quit()
