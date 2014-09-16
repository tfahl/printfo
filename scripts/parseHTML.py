from bs4 import BeautifulSoup
dir = '../test/'

file = open(dir + 'data.csv', 'w+')

def write_file(data):
	file.write(data + ",")



#uses beautiful soup to parse html file
#finds the correct span tag
#Gets the percentage of ink left in the printer
soup = BeautifulSoup(open(dir + 'test.html'))
res =  soup.find('span',{'class':'hpConsumableBlockHeaderText'}).text
num = res[24] + res[25]
if res[26] == '0':
	num = num + res[26]

write_file(num)
file.close()
