from HTMLParser import HTMLParser

#Creates subclass to override handler methods
class my_hp(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print "Encountered a start tag"

#Creates a parser
parser = my_hp()

#opens an html file, stores text in varaible data
#Replace test/test.html with html file to parse
with open('test/test.html', 'r') as myfile:
	data = myfile.read().replace('\n','')

#Runs parser on text contents of the html file
parser.feed(data)


