from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


@app.route("/deposit/<account_id>")
def deposit(account_id):
    return "Deposit money on account : " + account_id


@app.route("/withdraw/<account_id>")
def withdraw():
    return "Withdraw money"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

