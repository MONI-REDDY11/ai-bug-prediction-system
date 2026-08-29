from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_risk(loc, complexity):
    if loc > 500 or complexity > 10:
        return "High Bug Risk"
    elif loc > 200 or complexity > 5:
        return "Medium Bug Risk"
    return "Low Bug Risk"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    loc = int(data.get("loc", 0))
    complexity = int(data.get("complexity", 0))
    risk = get_risk(loc, complexity)
    return jsonify({"risk": risk})

if __name__ == "__main__":
    app.run(debug=True)
