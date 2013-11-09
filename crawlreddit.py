fb = open('twilio.xml', 'w')

from pprint import pprint
import requests
import xml

r = requests.get(r'http://reddit.com/.json')
r.text

data = r.json()

#for child in data['data']['children']:
#    print child['data']['subreddit']

for child in data['data']['children']:
    x = child['data']['subreddit']
    
print x

fb.write("?xml version='1.0' encoding='UTF-8'?>\n");
fb.write("<Response>\n");
fb.write("  <Say voice='woman'> The substring is " + str(x) + "\n");
fb.write("  .</Say>\n");
fb.write("</Response>\n");
fb.close()

