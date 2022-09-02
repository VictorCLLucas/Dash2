import urllib
from urllib.request import urlopen

def get_bored_data():
	link = "http://www.boredapi.com/api/activity"
	f = urlopen(link)
	myfile = f.read()
	return(myfile)