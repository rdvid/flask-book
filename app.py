from flask import Flask, request, Response
import json
from controllers import controller
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/send', methods=['POST'])
def send_email():
    try:
        book = request.files.get('data[file]')
        title = request.args.get('title').replace('+', ' ')
        author = request.args.get('author').replace('+', ' ')
        kindle_email = request.args.get('email').replace('+', ' ')
        return controller.send_email(book, title, author, kindle_email)
    except:
        data = {"message": "oh-oh something bad happened :("}
        return Response(status=500, content_type='application/vnd.api+json', response=json.dumps(data))


@app.route('/', methods=('GET',))
def get_json():
    return 'Use /send route to send books'


# TODO: create documentation and implement celery queue feat

app.run(host='0.0.0.0', port=5000)
