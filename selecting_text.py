
from urllib.request import urlopen
#The urllib.request module defines functions and classes which 
#help in opening URLs (mostly HTTP) in a complex world — 
#basic and digest authentication, redirections, cookies and more.
from bs4 import BeautifulSoup


def fetching_url():

	html = urlopen("http://shakespeare.mit.edu/lll/full.html")
	bsobj = BeautifulSoup(html.read(), "html.parser")
	# print(bsobj.h3)

	# .get_text() strips all tags from the document you are working
	# with and returns a string containing the text only.
	# Calling  .get_text() should always be the last thing you do, immedi‐
	# ately before you print, store, or manipulate your final data.
 


	nameList = bsobj.findAll(text="DUMAIN")
	print(nameList)
	print(len(nameList))


fetching_url()