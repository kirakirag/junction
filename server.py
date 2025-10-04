from flask import Flask, request, jsonify

app = Flask(__name__)

# GET endpoint
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from your local API!"})

# POST endpoint
@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Expecting JSON body"}), 400
    return jsonify({"you_sent": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)