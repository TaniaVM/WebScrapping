#parsing emails from a web page

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def fetching_url():
	html = urlopen("http://clickaces.com/contact/")
	bsobj = BeautifulSoup(html.read(), "html.parser")
	mail = bsobj.findAll(text="info@clickaces.com")
	#print(mail)
	emails = bsobj.findAll(text=re.compile(r"[A-Za-z0-9\._+]))+@[A-Za-z]+\.(com)
    # para ver como puedes definir una cadena de correo o algo especifico ve a la página : 
    # http://pythex.org/
    for email in emails:
    	print(email)
fetching_url()

#