from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello I'm Franz and this is my simple Flask web app on Azure!"

if __name__ == "__main__":
    app.run(debug=True)
