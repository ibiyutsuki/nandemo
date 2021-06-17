from flask import Flask, render_template,request
from flask.templating import render_template_string
from werkzeug.wrappers import Request

app = Flask(__name__)


@app.route("/")
def top_page():
    return render_template("index.html")

@app.route("/square_input")
def square_input():
    return render_template("square_input.html")

@app.route("/square_result")
def square_result():
    hei = int(request.args.get("hei"))
    bot = int(request.args.get("bot"))
    result = hei * bot
    return render_template("square_result.html",result=result)

if __name__ == "__main__":
    app.run(debug=True)