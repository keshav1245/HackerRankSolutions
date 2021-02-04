# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        if len(attrs) > 0:
            for k,v in attrs:
                print("-> {} > {}".format(k,v))
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        if len(attrs) > 0:
            for k,v in attrs:
                print("-> {} > {}".format(k,v))
                

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += "\n"

parser = MyHTMLParser()
parser.feed(html)
parser.close()
