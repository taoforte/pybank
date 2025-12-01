from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a random secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        session['name'] = name
        session['balance'] = 0
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'name' not in session:
        return redirect(url_for('index'))
    
    message = ""
    if request.method == 'POST':
        action = request.form['action']
        try:
            amount = float(request.form.get('amount', 0))
            if amount <= 0:
                message = "Amount must be positive!"
            elif action == 'deposit':
                session['balance'] += amount
                message = f"Deposited ${amount:.2f}. New balance: ${session['balance']:.2f}"
            elif action == 'withdraw':
                if amount <= session['balance']:
                    session['balance'] -= amount
                    message = f"Withdrew ${amount:.2f}. New balance: ${session['balance']:.2f}"
                else:
                    message = "Not enough money!"
        except ValueError:
            message = "Invalid amount!"
    
    return render_template('dashboard.html', 
                          name=session['name'],
                          balance=session['balance'],
                          message=message)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)