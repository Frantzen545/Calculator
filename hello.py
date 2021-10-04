from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

def validate_call(request):
    key = request.headers.get('security_key')
    token = request.headers.get('security_token')
    if key != 'U1xrbVINgxKUEnXuzxS3':
        return (False, 'Security Key is invalid')
    if token != '23d4d57ab18b13c81b7ad07cd0503029':
        return (False, 'Security Token is invalid')
    print(key)
    print(token)
    return (True, '')

@app.route("/")
def hello_world():
    result = validate_call(request)
    message = ''
    if result[0]:
        message = "Hello, World!"
    else:
        message = result[1]
    data = { "message":message}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/<name>")
def hello_name(name):
    print(name)
    result = validate_call(request)
    message = ''
    if result[0]:
        message = "Hello, " + name + "!"
    else:
        message = result[1]
    data = { "message":message}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
