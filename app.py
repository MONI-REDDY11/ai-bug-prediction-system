from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", lines_of_code="", complexity="", prediction="")

@app.route("/predict", methods=["POST"])
def predict():
    lines_of_code = request.form.get("lines_of_code", "")
    complexity = request.form.get("complexity", "")

    prediction = ""

    if not lines_of_code or not complexity:
        prediction = "Please enter both values"
    else:
        try:
            loc = int(lines_of_code)
            comp = int(complexity)

            if loc > 500 or comp > 10:
                prediction = "High Bug Risk"
            elif loc > 200 or comp > 5:
                prediction = "Medium Bug Risk"
            else:
                prediction = "Low Bug Risk"
        except:
            prediction = "Enter valid numbers only"

    return render_template(
        "index.html",
        lines_of_code=lines_of_code,
        complexity=complexity,
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
      
