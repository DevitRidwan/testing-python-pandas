from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import facebook
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
cors = CORS(app)

def fc():
    accessToken = 'EAAe7ZCd2V69kBADkMqNha16OImrXQO5QHXZCC7UlmrZBVcaYY2cE0T1l7qcmKnpRrhyaWm3uYkItHUKHvlsKvDsCS5ZAtjE1NKKh8LJ8ZAfMRMVEj4DPNoJqfhENWJZCKHpiVIOMlzHZAsVczm63ZBzybgNZALZAvycQm0WbUsr4vsAwZDZD'

    graph = facebook.GraphAPI(accessToken)
    profile = graph.get_object('me/feed', fields='name,status_type,message,created_time,description')
    return profile


@app.route("/apis/user-feed")
def user_feed():
    return jsonify(fc())

@app.route('/apis/view-feed')
def view_feed():
    return render_template('view-feed.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')