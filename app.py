from flask import Flask, render_template,request, redirect,url_for
from database import initiliaze_database,add_transaction, fetch_all_transactions

app = Flask(__name__)
initiliaze_database()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add', methods=['GET','POST'])
def add_transaction_view():
    if request.method == 'POST':
        date = request.form['date']
        type_ = request.form['type']
        category = request.form['category']
        amount = float(request.form['category'])
        description =request.form['descripton']
        add_transaction(date, type_, category, amount, description)
        return redirect(url_for('index'))
    return render_template('add_transaction.html')

@app.route('/summary')
def summary():
    transactions = fetch_all_transactions()
    total_income = sum(t[4] for t in transactions if t[2] == "income")
    total_expenses = sum(t[4] for t in transactions if[2] == "expenses")
    balance = total_income - total_expenses
    return render_template('summary.html', income = total_income, expenses = total_expenses, balance = balance)

if __name__ == '__main__':
    app.run(debug = True)