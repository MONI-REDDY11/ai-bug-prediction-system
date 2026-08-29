from flask import Flask, render_template, request

app = Flask(__name__)

def predict_risk(loc, complexity):
    if loc > 500 or complexity > 10:
        return "High Bug Risk"
    elif loc > 200 or complexity > 5:
        return "Medium Bug Risk"
    else:
        return "Low Bug Risk"

@app.route("/", methods=["GET", "POST"])
def index():
    loc = ""
    complexity = ""
    risk = ""
    error = ""

    if request.method == "POST":
        loc = request.form.get("loc", "").strip()
        complexity = request.form.get("complexity", "").strip()

        try:
            loc_val = int(loc)
            complexity_val = int(complexity)

            if loc_val < 0 or complexity_val < 0:
                error = "Enter positive numbers only."
            else:
                risk = predict_risk(loc_val, complexity_val)

        except ValueError:
            error = "Please enter valid numbers."

    return render_template(
        "index.html",
        loc=loc,
        complexity=complexity,
        risk=risk,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
