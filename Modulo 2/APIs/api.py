# from flask import Flask, jsonify
# app = Flask(__name__)
# @app.route('/api', methods=['GET'])
# def hello_apí():
#     return jsonify({"message": "Hello, API!"})
# app.run()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "olá, flask!"


app.run(debug=True)