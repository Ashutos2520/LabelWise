from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

harmful_chemicals = {
    "aspartame": "Artificial sweetener linked to headaches and potential neurological effects",
    "monosodium glutamate": "Can cause headaches and other symptoms in sensitive individuals",
    "sodium nitrite": "Used in processed meats; linked to increased cancer risk",
    "trans fats": "Increase risk of heart disease and raise bad cholesterol levels",
    "high fructose corn syrup": "Linked to obesity, diabetes, and metabolic disorders"
"butylated hydroxyanisole (BHA)": "Synthetic antioxidant preservative; possible human carcinogen, may disrupt hormones",
    "butylated hydroxytoluene (BHT)": "Synthetic antioxidant preservative; linked to liver damage and endocrine disruption",
    "potassium bromate": "Flour improver in bread; associated with kidney damage and cancer in animal studies",
    "sodium benzoate": "Preservative in soft drinks and acidic foods; may form benzene (a carcinogen) when combined with vitamin C",
    "propylene glycol": "Humectant and stabilizer; can cause skin irritation and allergic reactions in sensitive individuals",
    "sorbitol": "Sugar alcohol sweetener; excessive intake may cause bloating, gas, and diarrhea",
    "sodium aluminum phosphate": "Leavening agent in baked goods; long-term exposure may be linked to neurotoxicity",
    "aluminum ammonium sulfate": "Used in baking powders; may accumulate in the body and affect nervous system",
    "artificial food coloring (Allura Red AC - Red 40)": "Synthetic dye in candies and drinks; linked to hyperactivity and allergic reactions in children",
    "artificial food coloring (Tartrazine - Yellow 5)": "Synthetic dye; may cause allergic reactions and hyperactivity in sensitive individuals",
    "artificial food coloring (Sunset Yellow FCF - Yellow 6)": "Synthetic dye; linked to hyperactivity and possible carcinogenic effects",
    "azodicarbonamide": "Dough conditioner and bleaching agent; associated with respiratory issues and banned in some countries",
    "tert-butylhydroquinone (TBHQ)": "Preservative in fried and frozen foods; linked to nausea, allergies, and potential carcinogenic effects"
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
