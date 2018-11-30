import re
import requests

# Scraper Class
# Grabs content from the web
# Returns a list of all the URLs
class Scraper(object):
	List = []

	# Initalize with a web address
	# <parameter="address"> accessable url string</parameter>
	def __init__(self, address):
		self.address = address
		self._get(address)

	# loads web content into cache
	def _get(self, address):
		self.request = requests.get(address)
		self.ListURLs(self.request.text)

	# scrapes data for a regex
	# <parameter="content">content to search for URL's, stores it in scraperObject.List</parameter>
	def ListURLs(self, content):
		# https://gist.github.com/gruber/249502
		pattern = "(?i)\\b((?:[a-z][\\w-]+:(?:/{1,3}|[a-z0-9%])|www\\d{0,3}[.]|[a-z0-9.\\-]+[.][a-z]{2,4}/)(?:[^\\s()<>]+|\\(([^\\s()<>]+|(\\([^\\s()<>]+\\)))*\\))+(?:\\(([^\\s()<>]+|(\\([^\\s()<>]+\\)))*\\)|[^\\s`!()\\[\\]{};:'\".,<>?«»“”‘’]))"
		groups = re.findall(pattern, content)
		self.List = [item[0] for item in groups]

