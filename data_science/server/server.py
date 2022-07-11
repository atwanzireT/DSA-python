from flask import Flask, request, jsonify

app = Flask(__name__)

if __name__ == "__main__":
    print("Starting python flask server for home predictions ...")
    app.run()