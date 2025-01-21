from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

# an endpoint that returns a random number
# @app.route("/random")
# def random_number():
#     import randomresponse = {
#         'randomNumber': 
#     }