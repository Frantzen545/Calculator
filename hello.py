from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


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
    return jsonify(data)


@app.route("/<name>")
def hello_name(name):
    result = validate_call(request)
    message = ''
    if result[0]:
        message = "Hello, " + name + "!"
    else:
        message = result[1]
    data = { "message":message}
    return jsonify(data)
