import sys
import re
import urllib2
import socket
import HTMLParser
import getopt
from threading import Thread
from time import sleep

def usage():
    	print('\n\t:: [PH] Index Python Main Dumper::')
        print('Usage:')
        print('python pymaildumper.py [domain] [dork] [subdomain]')
        print('\nExample: $ python pymaildumper.py gov.ph @gmail.com ph\n')
        return

def get_result(domain, dork, subdomain):
	pattern = re.compile(r'[\w\.-]+@[\w\.-]+[\w\.-]')
	cnt = 0
	mails = []
	for i in range(1, 2, 20):
	    url = 'https://www.google.com.ph/search?q=%s&start%d=&num=100&saN=&filter=0&sitesearch=%s' %(dork,i,domain)
	    opener = urllib2.build_opener()
	    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	    data = opener.open(url).read() 
	    #print data
	    matches = pattern.findall(data)
	    if len(matches) == 0:
	    	mails.append('No matches found')
	    	break

	    t = Thread(target=printMails,args=(matches,subdomain,))
	    t.start()
	    while(t.isAlive()): sleep(0xA)

	return mails

def printMails(matches,subdomain):
	for match in set(matches):
		if match[-1] == '.': match+=subdomain
		print(match)
		sleep(.05)
		
	
def start(dom, dork, subdomain):
	results = get_result(dom, dork, subdomain)

if __name__ == '__main__':
   if len(sys.argv) == 4:
   		dom = str(sys.argv[1])
   		dork = str(sys.argv[2])
   		subdomain = str(sys.argv[3])
   		print '\n###### Started scanning emails ######\n'
   		thread = Thread(target=start,args=(dom, dork, subdomain))
   		thread.start()
   		thread.join()
   		while(thread.isAlive()): sleep(0xA)
		print '\n############### GAME OVER ###############\n\n' 
   else:
	usage()