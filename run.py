from flask import Flask, request, jsonify, send_from_directory, redirect, url_for

app = Flask(__name__, static_url_path='', static_folder='web-frontend/dist/spa-mat')

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

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

@app.route('/<path:path>')
def frontend(path):
	if (path == ''):
		path = 'index.html'
	return send_from_directory('web-frontend/dist/spa-mat', path)

@app.route('/')
def home():
	return frontend('index.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')