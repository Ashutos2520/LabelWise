from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

harmful_chemicals = {
    "aspartame": "Artificial sweetener linked to headaches and potential neurological effects",
    "monosodium glutamate": "Can cause headaches and other symptoms in sensitive individuals",
    "sodium nitrite": "Used in processed meats; linked to increased cancer risk",
    "trans fats": "Increase risk of heart disease and raise bad cholesterol levels",
    "high fructose corn syrup": "Linked to obesity, diabete
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/check', methods=['POST'])
def check_chemical():
    try:
        # Check if request contains JSON
        if not request.is_json:
            return jsonify({
                "error": "Request must be JSON"
            }), 400

        data = request.get_json()
        
        # Validate input
        if not data or 'name' not in data:
            return jsonify({
                "error": "Missing 'name' parameter"
            }), 400

        name = data.get("name", "").strip().lower()
        
        # Check for empty input
        if not name:
            return jsonify({
                "error": "Chemical name cannot be empty"
            }), 400

        # Check chemical database
        if name in harmful_chemicals:
            return jsonify({
                "chemical": name,
                "reason": harmful_chemicals[name]
            }), 200
        else:
            return jsonify({
                "chemical": name,
                "reason": "We are working on it!!"
            }), 200

    except Exception as e:
        return jsonify({
            "error": "Server error occurred",
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
