from flask import Flask, request,  jsonify
from controllers import controller

app = Flask(__name__)


@app.route('/send', methods=['POST'])
def send_email():
    name = request.args.get('name').replace('+', ' ')
    author = request.args.get('author').replace('+', ' ')
    book = request.files.get('file')
    return controller.send_email(book, name, author)


@app.route('/', methods=('GET',))
def get_json():
    return 'Use /send route to send books'


app.run()
