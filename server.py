from flask import Flask, request, jsonify
import db

app = Flask(__name__)

db.ensureDbExists()
db.loadData()
conn = db.getConnection()

# GET endpoint
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": db.getData(conn, "2023-01-01", 1)})

# POST endpoint
@app.route("/getData", methods=["POST"])
def getData():
    data = request.get_json(silent=True)
    return jsonify({"count": db.getData(conn, data["date"], data["city_id"])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)