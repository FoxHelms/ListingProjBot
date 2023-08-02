from go_to_page import go_to_page as gtp
from go_to_page import get_el_xpath as get_el
from go_to_page import get_els_xpath as get_els
from go_to_page import driver
import lp_links


reqSubStr = 'https://www.listingsproject.com/listings/'
links = []


# Older selenium syntax
# driver.find_element_by_xpath("//input[@type='submit' and @value='something']").click()
# newer selenium synntax
# browser.find_element(By.XPATH, '//button[text()="Outliers"]')

def get_listings():
    for suffix in lp_links.suffixes:
        gtp(lp_links.base_url + suffix)
        try:
            get_el('//button[text()="Ok, got it"]').click()
            get_el('//input[@type="submit" and @value="I accept. Take me to the listings."]').click()
        except:
            pass

    
        elems = get_els('//a[@href]')
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
    driver.quit()
    return uniqueLinks

'''
https://www.listingsproject.com/listings/1-room-avail-in-prime-lic-2bd
https://www.listingsproject.com/listings/seeking-roommate-for-2-bedroom-bushwick-apartment
https://www.listingsproject.com/listings/happy-one-bedroom-in-bronx-little-italy-92009f34-848d-49cf-9099-4a83a4670728
https://www.listingsproject.com/listings/funky-two-bedroom-sublet-sleeps-3
https://www.listingsproject.com/listings/sublet-in-nolita-ead448c3-ea75-478c-983a-57e3a7664f4e
https://www.listingsproject.com/listings/sunny-penthouse-in-greenwich-village-b312a815-4336-4da6-a6e9-b79892f4261a
https://www.listingsproject.com/listings/exceptional-furnished-studio-and-office-in-best-area-no-fee-99239c1c-aa1b-436b-a84d-8cc64a849aaa

'''