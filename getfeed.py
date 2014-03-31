from urllib2 import urlopen
from urllib import quote

print "1001: NEWS TOPIC"
print "1002: NPR.ORG HOMEPAGE FEED"
print "1045: MOVIES"
print "1007: SCIENCE"
print "1032: ECONOMY"
print "1039: NPR MUSIC"
print "2: ALL THINGS CONSIDERED"
print "5500502: KRULWICH WONDERS BLOG"
print "2101154: STORIES BY ARI SHAPIRO"
print "93568166: MONKEY SEE POP CULTURE"

key = "API_KEY"
url = 'http://api.npr.org/query?apiKey='
url += key
url += "&numResults=3&action=Or&requiredAssets=text&format=rss"

npr_id = raw_input("Enter comma-separated NPR IDs or leave blank.")
search_string = raw_input("Enter your search query or leave blank.")
feed_title = raw_input("What's your feed title?")

if npr_id or search_string:
	raw_input("Hit enter to download your podcast.")
	
	if npr_id:
		url+= "&id=" + npr_id
    
	if search_string:
		url += "&searchterm=" + quote(search_string)
	
	if feed_title:
		url += '&title=' + quote(feed_title)
    
	response = urlopen(url)
	output = response.read()
	my_feed = open('my_feed.xml', 'w')
	my_feed.write(output)
	my_feed.close()

else:
	print "You must enter an NPR ID, a search term, or both."