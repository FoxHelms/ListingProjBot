from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
timeout = 20

def go_to_page(url):
    driver.get(url)

def presence_of(el):
    try:
        element_present = EC.presence_of_element_located((By.XPATH, el))
        WebDriverWait(driver, timeout).until(element_present)
        return True
    except:
        print('Timed out waiting for page to load')


def get_el_xpath(el):
    if presence_of(el):
        return driver.find_element(By.XPATH, el)
        print("success")
    else:
        print("No element found")
    

def get_els_xpath(el):
    if presence_of(el):
        return driver.find_elements(By.XPATH, el)
        print("success")
    else:
        print("No elements found")