from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚗 Sai Motors</h1>
    <h3>Bike Store Website Running ✅</h3>
    <p>Website successfully working!</p>
    """

if __name__ == "__main__":
    app.run()
