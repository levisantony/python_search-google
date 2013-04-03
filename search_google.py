#!/usr/bin/python
import json
import urllib

# Query to be searched in Google 
search='github'

# replaces unsafe ASCII characters with a "%" followed by two hexadecimal digits
srchqry = urllib.urlencode({'q': search})

#url to search
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % srchqry

#get response
response = urllib.urlopen(url)

# result in form of json
rslt = response.read()
results = json.loads(rslt)
data = results['responseData']

#print results
print 'About %s results' % data['cursor']['estimatedResultCount']
rslt_data = data['results']
for r in rslt_data: print ' ', r['url']
#print 'For more %s:' % data['cursor']['moreResultsUrl']
