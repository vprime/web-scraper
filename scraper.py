import re
import requests

from detection import Detection

# Scraper Class
# Grabs content from the web
# Returns a list of all the URLs
class Scraper(object):
	List = []

	def __init__(self, address):
		self.address = address
		self._get(address)

	# loads web content into cache
	def _get(self, address):
		self.request = requests.get(address)
		self.ListURLs(self.request.text)

	# scrapes data for a regex
	def ListURLs(self, content):
		pattern = "(?i)\\b((?:[a-z][\\w-]+:(?:/{1,3}|[a-z0-9%])|www\\d{0,3}[.]|[a-z0-9.\\-]+[.][a-z]{2,4}/)(?:[^\\s()<>]+|\\(([^\\s()<>]+|(\\([^\\s()<>]+\\)))*\\))+(?:\\(([^\\s()<>]+|(\\([^\\s()<>]+\\)))*\\)|[^\\s`!()\\[\\]{};:'\".,<>?«»“”‘’]))"
		self.List = re.findall(pattern, content)

