from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    diagnosis = ""
    if request.method == "POST":
        # Example: Retrieve form data
        cal = float(request.form["cal"])
        probing_depth = float(request.form["probing_depth"])
        bop_percentage = float(request.form["bop_percentage"])
        
        # Diagnosis logic here (simplified for demonstration)
        if cal == 0 and bop_percentage <= 10:
            diagnosis = "Clinical Gingival Health on an Intact Periodontium"
        else:
            diagnosis = "Possible Periodontitis"
        
        # Add more complex diagnosis logic as needed
        
    return render_template("index.html", diagnosis=diagnosis)

if __name__ == "__main__":
    app.run(debug=True)
