from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def display_message():
    message = request.data.decode('UTF-8')
    print(message)
    return 'Message received'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

