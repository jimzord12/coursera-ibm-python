# Import libraries
from flask import Flask, request, redirect, render_template, url_for
# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

def calcBalance(txs):
    _balance = 0
    for tx in txs:
        _balance += float(tx["amount"])
    return _balance

balance = calcBalance(transactions)
# Read operation
@app.route("/<id>")
def getTx(id):
    for tx in transactions:
        if tx["id"] == id:
            return tx
    return {"message": "Transaction not found"}, 404

@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions, balance=balance )


# Create operation
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "GET":
        return render_template("form.html")

    if request.method == "POST":
        date = request.form["date"]
        amount = request.form["amount"]
        newTx = {
                'id': len(transactions) + 1,
                'date': date,
                'amount': float(amount)
                }
        transactions.append(newTx)
        balance += amount
        return redirect(url_for("get_transactions"))


# Update operation
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    global balance
    if request.method == "GET":
        for transaction in transactions:
            if transaction["id"] == transaction_id:
                return render_template("edit.html", transaction=transaction)
        return {"message": "Transaction not found"}, 404

    if request.method == "POST":
        for transaction in transactions:
            if transaction["id"] == transaction_id:
                transaction["date"] = request.form["date"]
                transaction["amount"] = request.form["amount"]
                balance = calcBalance(transactions)
                return redirect(url_for("get_transactions"))
        return 404

# Delete operation
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    global balance
    for idx, tx in enumerate(transactions):
        if tx["id"] == transaction_id:
            del transactions[idx]
            balance = calcBalance(transactions)
            return redirect(url_for("get_transactions"))
    return 404

@app.route("/search", methods=["GET", "POST"])
def search_transactions():
    if request.method == "GET":
        return render_template("search.html")
    
    if request.method == "POST":
        filteredTx = []
        for tx in transactions:
            min = float(request.form["min_amount"])
            max = float(request.form["max_amount"])
            if float(tx["amount"]) >= min and float(tx["amount"]) <= max:
                filteredTx.append(tx)

        if len(filteredTx) > 0:
            filteredTxBalance = calcBalance(filteredTx)
            return render_template("transactions.html", transactions=filteredTx, balance=filteredTxBalance)
# Run the Flask app
def main():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()