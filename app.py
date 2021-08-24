from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
@app.route("/index.html")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/products")
@app.route("/products.html")
def change():
    return render_template('produts.html')


@app.route("/insights")
@app.route("/insights.html")
def insights():
    return render_template('insights.html')

@app.route("/tutorial")
@app.route("/tutorial.html")
def tutorial():
    return render_template('tutorial.html')

@app.route("/viz1")
@app.route("/viz1.html")
def viz1():
    return render_template('viz1.html')

@app.route("/viz2")
@app.route("/viz2.html")
def viz2():
    return render_template('viz2.html')

@app.route("/viz3")
@app.route("/viz3.html")
def viz3():
    return render_template('viz3.html')


if __name__ == "__main__":
    app.run(debug=True)