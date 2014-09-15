from HTMLParser import HTMLParser

#Creates subclass to override handler methods
class html_parser(HTMLParser):
	def handle_data(self, data):
		print "Saw some data:", data
		#if data == "Black Print Cartridge":
		#Get next line of data, save in a variable
			
#Creates a parser
parser = html_parser()

#opens an html file, stores text in varaible data
#Replace test/test.html with html file to parse
with open('test/test.html', 'r') as html_input:
	html_text = html_input.read().replace('\n','')

#Runs parser on text contents of the html file
parser.feed(html_text)
parser.close()


