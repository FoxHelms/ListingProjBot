from listings_lists import listingList as li
from get_list_data import get_list_data as gld

listingData = []
i = 0
f = open("listData.py", "a")
f.write('listingData = [ \n')

for l in li:
    i+=1
    listing = gld(l)
    #f = open("listData.py", "a")
    f.write('[')
    for item in listing:
        f.write(item + ', ')
        #print(item)
    f.write('], \n')
    print(i)
    
#f = open("listData.py", "a")
#f.write('listingData = [ \n')
#for l in listingData:
#    f.write('"' + l + '",\n')

f.write(']')
f.close()

print("Done!")