from bs4 import BeautifulSoup

#uses beautiful soup to parse html file
#finds the correct span tag
#Gets the percentage of ink left in the printer
soup = BeautifulSoup(open("test/test.html"))
res =  soup.find('span',{'class':'hpConsumableBlockHeaderText'}).text
num = res[24] + res[25]

file = open('test/data.csv', 'w+') 
file.write(num + ",")

