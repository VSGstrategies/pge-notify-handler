from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_notification():
    data = request.get_json()
    print("Received data:", data)
    return {'status': 'success'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
