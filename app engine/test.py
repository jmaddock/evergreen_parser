import webapp2
from bs4 import BeautifulSoup
from google.appengine.api import urlfetch
import urllib

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        urlfetch.set_default_fetch_deadline(60)
        url = 'http://evergreenmtb.org/recreation/'
        soup = BeautifulSoup(urllib.urlopen(url))
        titles = soup.find_all("font")
        dates = soup.find_all("td")
        results = []
        self.response.write(">> RIDES <<\n\n>> WORK PARTIES <<\n\n>> RACES <<\n\n>> CLASSES <<\n\n>> COMMUNITY MEETINGS <<\n\nhttp://evergreenmtb.org/recreation/calendar_view.php\n\n")
        for x in titles[2:]:
            if "#6D8D38" in str(x):
                title = str(x.b)[3:-4]
                if len(title) > 0 and "<center>" not in title:
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
            self.response.write("> " + x['date'] + ": " + x['title'] + "\n")
        self.response.write("\n\n")
        for x in results:
            self.response.write("> " + x['date'].partition('-')[0] + "- " + x['title'] + " @" + x['date'].partition('-')[2] + '\n')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
