from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":

        name = request.form["name"]
        age = int(request.form["age"])
        spouse = request.form["spouse"]
        spouse_age = int(request.form["spouse_age"])
        child1 = request.form["child1"]
        child1_age = int(request.form["child1_age"])
        income = float(request.form["income"])
        expense = float(request.form["expense"])
        savings = float(request.form["savings"])
        life_cover = float(request.form["life_cover"])
        goals = float(request.form["goals"])
        risk = request.form["risk"]

        retirement_age = 60
        working_years = retirement_age - age
        surplus = income - expense

        emergency_fund = expense / 12 * 6
        insurance_required = income * working_years
        insurance_gap = insurance_required - life_cover

        retirement_corpus = expense * 20

        if risk == "High":
            growth_ratio = 0.6
        elif risk == "Moderate":
            growth_ratio = 0.45
        else:
            growth_ratio = 0.3

        liquidity_ratio = 0.2
        savings_ratio = 1 - (growth_ratio + liquidity_ratio)

        liquidity_alloc = surplus * liquidity_ratio
        savings_alloc = surplus * savings_ratio
        growth_alloc = surplus * growth_ratio

        def status(required, current):
            return "SAFE" if current >= required else "UNDERFUNDED"

        result = {
            "name": name,
            "working_years": working_years,
            "surplus": surplus,
            "emergency_fund": emergency_fund,
            "insurance_gap": insurance_gap,
            "retirement_corpus": retirement_corpus,
            "liquidity_alloc": liquidity_alloc,
            "savings_alloc": savings_alloc,
            "growth_alloc": growth_alloc,
            "liq_status": status(emergency_fund, savings),
            "ins_status": status(0, insurance_gap)
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
