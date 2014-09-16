from bs4 import BeautifulSoup

dir = '../printer_sources/'

j = 1
i = str(j)
file = open('../data/data' + i + '.csv', 'w+')

def write_file(data):
	file.write(data + ",")



#uses beautiful soup to parse html file
#finds the correct span tag
#Gets the percentage of ink left in the printer
soup = BeautifulSoup(open(dir + 'html/dirtest.html'))
res =  soup.find('span',{'class':'hpConsumableBlockHeaderText'}).text
num = res[23] + res[24]
if res[25] == '0':
	num = num + res[25]

write_file(num)
file.close()
