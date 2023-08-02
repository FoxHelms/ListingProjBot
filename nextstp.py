#import the unique links

from go_to_page import go_to_page as gtp
from go_to_page import get_el_xpath as get_el

gtp('https://www.listingsproject.com/listings/seeking-roommate-for-2-bedroom-bushwick-apartment')
try:
    get_el('//button[text()="Ok, got it"]').click()
    get_el('//input[@type="submit" and @value="I accept. Take me to the listings."]').click()
except:
    pass

price_el = get_el('//span[@class="text-white text-2xl font-semibold bg-teal-light py-2 px-4"]')
email_el = get_el('//a[@class="contact__a"]')
name_el = get_el('//strong[@style="display: inline-block; float: left; width: 100px;margin-right: 1rem;"]/following-sibling::span')

print(price_el.text)

'''
Get location and available dates!
'''

print(email_el.text)
print(name_el.text)

me = input('say smthng')