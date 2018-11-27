from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/scrape', methods=['POST'])
def login():
	if request.method == 'POST':
		from scraper import Scraper
		scraper = Scraper(request.form['address'])
		return jsonify(
			source=request.form['address'], 
			status=scraper.request.status_code,
			detections=scraper.List
			)