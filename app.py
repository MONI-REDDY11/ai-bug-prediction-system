from flask import Flask, render_template, request

app = Flask(__name__)

def get_prediction(loc, complexity):
    if loc > 500 or complexity > 10:
        return "High Bug Risk"
    elif loc > 200 or complexity > 5:
        return "Medium Bug Risk"
    return "Low Bug Risk"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", loc="", complexity="", prediction="", error="", suggestion="")

@app.route("/predict", methods=["POST"])
def predict():
    loc = request.form.get("loc", "").strip()
    complexity = request.form.get("complexity", "").strip()

    error = ""
    suggestion = ""
    prediction = ""

    if not loc and not complexity:
        error = "Both fields are empty."
        suggestion = "Enter valid numbers in both fields."
    elif not loc:
        error = "Lines of Code is missing."
        suggestion = "Type a number for Lines of Code."
    elif not complexity:
        error = "Complexity is missing."
        suggestion = "Type a number for Complexity."
    else:
        try:
            loc_val = int(loc)
            complexity_val = int(complexity)

            if loc_val < 0 and complexity_val < 0:
                error = "Both values are negative."
                suggestion = "Use positive numbers only."
            elif loc_val < 0:
                error = "Lines of Code is negative."
                suggestion = "Change Lines of Code to a positive number."
            elif complexity_val < 0:
                error = "Complexity is negative."
                suggestion = "Change Complexity to a positive number."
            elif loc_val == 0 and complexity_val == 0:
                error = "Both values are zero."
                suggestion = "Enter realistic values."
            else:
                prediction = get_prediction(loc_val, complexity_val)

                if prediction == "High Bug Risk":
                    suggestion = "Reduce LOC or split code into smaller modules."
                elif prediction == "Medium Bug Risk":
                    suggestion = "Refactor some parts and reduce complexity."
                else:
                    suggestion = "Code looks simple and manageable."
        except ValueError:
            error = "Invalid input."
            suggestion = "Please enter only numbers."

    return render_template(
        "index.html",
        loc=loc,
        complexity=complexity,
        prediction=prediction,
        error=error,
        suggestion=suggestion
    )

if __name__ == "__main__":
    app.run(debug=True)
             
