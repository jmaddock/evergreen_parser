from bs4 import BeautifulSoup
import urllib

url = 'http://evergreenmtb.org/recreation/'
soup = BeautifulSoup(urllib.urlopen(url))
titles = soup.find_all("font")
dates = soup.find_all("td")
results = []
print ">> RIDES <<\n\n>> WORK PARTIES <<\n\n>> RACES <<\n\n>> CLASSES <<\n\n>> COMMUNITY MEETINGS <<\n\nhttp://evergreenmtb.org/recreation/calendar_view.php"
for x in titles[2:]:
    if "#6D8D38" in str(x):
        title = str(x.b)[3:-4]
        if len(title) > 0:
            results.append({'title':title})
count = 0
for x in dates:
    if 'td align="right"' in str(x):
        date = str(x.b)
        if 'PM' in date:
            results[count]['date'] = date[3:-4]
            count += 1
        elif 'AM' in date:
            results[count]['date'] = date[3:-4]
            count += 1
for x in results:
    print x['date'] + ": " + x['title']
print "\n\n"
for x in results:
    print "> " + x['date'].partition('-')[0] + "- " + x['title'] + " @" + x['date'].partition('-')[2]
#print(soup.prettify())