from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", lines_of_code="", complexity="", prediction="")

@app.route("/predict", methods=["POST"])
def predict():
    lines_of_code = request.form.get("lines_of_code", "").strip()
    complexity = request.form.get("complexity", "").strip()

    if not lines_of_code or not complexity:
        return render_template(
            "index.html",
            lines_of_code=lines_of_code,
            complexity=complexity,
            prediction="Please enter both values"
        )

    try:
        loc = int(lines_of_code)
        comp = int(complexity)
    except ValueError:
        return render_template(
            "index.html",
            lines_of_code=lines_of_code,
            complexity=complexity,
            prediction="Enter valid numbers only"
        )

    if loc > 500 or comp > 10:
        prediction = "High Bug Risk"
    elif loc > 200 or comp > 5:
        prediction = "Medium Bug Risk"
    else:
        prediction = "Low Bug Risk"

    return render_template(
        "index.html",
        lines_of_code=lines_of_code,
        complexity=complexity,
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


