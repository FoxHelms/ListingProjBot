from get_last_wed import get_last_wed as wed

last_wed = wed()
base_url = "https://www.listingsproject.com/newsletter/" + str(last_wed) + "/new-york-city/"

room_rent_url = "room_rent"
room_sub_url = "room_sublet"
apt_rent_url = "apt_rent"
apt_sub_url = "apt_sublet"



# https://www.listingsproject.com/newsletter/2023-07-26/new-york-city/room_rent