from go_to_page import go_to_page as gtp
from go_to_page import teardown as td
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
    td()
    return uniqueLinks

li = get_listings()

f = open("listings_lists.py", "a")
f.write('listingList = [ \n')
for l in li:
    f.write('"' + l + '",\n')

f.write(']')
f.close()
'''
https://www.listingsproject.com/listings/hidden-rear-house-in-prime-williamsburg-with-garden
https://www.listingsproject.com/listings/light-plant-filled-crown-heights-apartment-abc42672-9d0d-4788-a508-7b18a851674a
https://www.listingsproject.com/listings/large-bedroom-great-light-in-spacious-loft-w-in-unit-laundry-dryer-d942505c-825d-4537-ad04-5b5ece6ed5a8
https://www.listingsproject.com/listings/room-for-rent-in-3br-1ba-in-prospect-lefferts-gardens
https://www.listingsproject.com/listings/1-large-bedroom-in-2-bd-apt-crown-heights
'''