with open('this.LCDispatcher','r') as printer_file:
    html_file = printer_file.read().replace('\n','')
file  = open('test.html', 'w+')
file.write(html_file)
