from flask import Flask
import baritone
import json


app = Flask(__name__)

@app.route('/')
def hello():
	print("Hello from terminal")
	return "Hello world"


@app.route('/youtube/<link>')
def youtube(link):
	print("ENTERED")
	url =  'https://www.youtube.com/watch?v='+link
	print(url)
	result,status  = (baritone.pipeline(url,'youtube'))
	convert = {
		'url': url,
		'text': result,
		'converted':status
	}
	return json.dumps(convert)

	
if __name__ == '__main__':
	print("Starting server")
	app.run(host='0.0.0.0')