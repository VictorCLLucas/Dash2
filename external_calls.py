import urllib

def get_bored_data():
	link = "http://http://www.boredapi.com/api/activity"
	f = urllib.urlopen(link)
	myfile = f.read()
	return(myfile)