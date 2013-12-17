#encoding: utf-8
import json
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('main.html')

@app.route("/m")
def mobile():
	print request.headers.get('Authorization')
	arr = []
	dict = {}
	dict["name"] = u"设备1"
	dict["server"] = "192.168.22.199"
	dict["port"] = 52006
	dict["user"] = "admin"
	dict["password"] = "admin"
	dict["type"] = 1

	arr.append(dict)

	dict = {}
	dict["name"] = "yu222"
	dict["server"] = "192.168.22.222"
	dict["port"] = 8888
	dict["user"] = "root"
	dict["password"] = "passwd"
	dict["type"] = 0

	arr.append(dict)


	return json.dumps(arr)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12160)
