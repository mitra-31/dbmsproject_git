from app import app

if __name__ == "__main__":
    app.secret_key = "QWERTY1234"
    app.run(debug=True)