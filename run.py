from flask import Flask, request, jsonify

app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/')
def home():
	return 'Hello, World!'

@app.route('/scrape', methods=['POST'])
def scrape():
	if request.method == 'POST':
		from scraper import Scraper
		scraper = Scraper(request.json['address'])
		return jsonify(
			source=request.json['address'], 
			status=scraper.request.status_code,
			detections=scraper.List
			)