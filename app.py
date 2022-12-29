from flask import Flask

app = Flask(__name__)

@app.route('/')
def predict():
    return "This is Rohan.This is end of 2022.have a nice year.happy new year"


if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1',port=5000)