from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    lines_of_code = request.form.get("lines_of_code", "").strip()
    complexity = request.form.get("complexity", "").strip()

    if not lines_of_code or not complexity:
        return render_template("index.html", prediction="Please enter both values")

    try:
        lines_of_code = int(lines_of_code)
        complexity = int(complexity)
    except ValueError:
        return render_template("index.html", prediction="Enter valid numbers only")

    if lines_of_code > 500 or complexity > 10:
        prediction = "High Bug Risk"
    elif lines_of_code > 200 or complexity > 5:
        prediction = "Medium Bug Risk"
    else:
        prediction = "Low Bug Risk"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
