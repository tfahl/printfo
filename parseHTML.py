from HTMLParser import HTMLParser

#Creates subclass to override handler methods
class html_parser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print "Encountered a start tag"
	
#Creates a parser
parser = html_parser()

#opens an html file, stores text in varaible data
#Replace test/test.html with html file to parse
with open('test/test.html', 'r') as html_input:
	html_text = html_input.read().replace('\n','')

#Runs parser on text contents of the html file
#Need to find a way to parse a particular line, maybe use string parse
parser.feed(html_text)


