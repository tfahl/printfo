from bs4 import BeautifulSoup

file = open('test/data.csv', 'w+')

def write_file(data):
	file.write(data + ",")



#uses beautiful soup to parse html file
#finds the correct span tag
#Gets the percentage of ink left in the printer
soup = BeautifulSoup(open("test/test.html"))
res =  soup.find('span',{'class':'hpConsumableBlockHeaderText'}).text
num = res[24] + res[25]

write_file(num)

file.close()
