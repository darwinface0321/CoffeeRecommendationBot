import urllib2
from bs4 import BeautifulSoup                                                   
import json

url = urllib2.urlopen('http://www.starbucks.com/menu/catalog/product?drink=brewed-coffee#view_control=product')

content = url.read()

soup = BeautifulSoup(content, "html.parser")
                                                    
table = soup.find("ol", {"class" : "blocks blocks-four-up thumbs"})
spans = table.find_all("span")
name_arr = []
for span in spans:
	name_arr.append( span.string )

#print name_arr

with open('coffeeType.json', 'r+') as f:
	json_data = json.load(f)
	current_coffee_list = json_data['coffee']
	#print current_coffee_list
	print len(current_coffee_list)
	#new_coffee_list = []
	
	for new_item in name_arr:
		if new_item not in current_coffee_list:
			current_coffee_list.append(new_item)
	json_data['coffee'] = current_coffee_list
	f.seek(0)
	f.write(json.dumps(json_data))
	f.truncate()
	