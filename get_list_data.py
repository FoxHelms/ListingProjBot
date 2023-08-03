#import the unique links

from go_to_page import go_to_page as gtp
from go_to_page import get_el_xpath as get_el
from go_to_page import teardown as td


starts = ['$','LOCATION','AVAILABLE','TRANSPORTATION']
ends = ['LOCATION','AVAILABLE','TRANSPORTATION','SIZE']
#listing = []
baseURL = 'https://www.listingsproject.com/listings/light-plant-filled-crown-heights-apartment-abc42672-9d0d-4788-a508-7b18a851674a'

def get_sub(baseStr, startStr, endStr):
    oldstr = baseStr[baseStr.find(startStr)+len(startStr):baseStr.rfind(endStr)]
    newstr = oldstr.replace("\n", "")
    return newstr

def get_list_data(baseURL):
    listing = []
    gtp(baseURL)
    try:
        get_el('//button[text()="Ok, got it"]').click()
        get_el('//input[@type="submit" and @value="I accept. Take me to the listings."]').click()
    except:
        pass

    #  Alt price method
    #  price_el = get_el('//span[@class="text-white text-2xl font-semibold bg-teal-light py-2 px-4"]')
    email_el = get_el('//a[@class="contact__a"]')
    name_el = get_el('//strong[@style="display: inline-block; float: left; width: 100px;margin-right: 1rem;"]/following-sibling::span')
    price_loc_avail_trans_el = get_el('//div[@class="listing-meta-container text-listing mr-16"]')

    for start, end in zip(starts, ends):
        listing.append(get_sub(price_loc_avail_trans_el.text,start,end))

    listing.append(email_el.text)
    listing.append(name_el.text)
    listing.append(baseURL)
    #driver.quit()
    return listing