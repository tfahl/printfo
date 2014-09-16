dir = '../printer_sources/'
dis_dir = 'dispatch/'
html_dir = 'html/'

with open(dir + dis_dir + 'this.LCDispatcher','r') as printer_file:
    html_file = printer_file.read().replace('\n','')
file  = open(dir + html_dir + 'dirtest.html', 'w+')
file.write(html_file)
