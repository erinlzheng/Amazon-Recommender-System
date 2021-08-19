from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
@app.route("/index.html")
@app.route("/")
def index():
    var1="hello"
    return render_template('index.html',var1=var1)


@app.route("/about")
@app.route("/about.html")
def about():
    var1="hello"
    return render_template('about.html',var1=var1)

@app.route("/products")
@app.route("/products.html")
def change():
    var1="hello"
    return render_template('produts.html',var1=var1)


@app.route("/insights")
@app.route("/insights.html")
def insights():
    var1="hello"
    return render_template('insights.html',var1=var1)

@app.route("/viz1")
@app.route("/viz1.html")
def viz1():
    var1="hello"
    return render_template('viz1.html',var1=var1)

@app.route("/viz2")
@app.route("/viz2.html")
def viz2():
    var1="hello"
    return render_template('viz2.html',var1=var1)

@app.route("/viz3")
@app.route("/viz3.html")
def viz3():
    var1="hello"
    return render_template('viz3.html',var1=var1)

@app.route("/viz4")
@app.route("/viz4.html")
def viz4():
    var1="hello"
    return render_template('viz4.html',var1=var1)

@app.route("/viz5")
@app.route("/viz5.html")
def viz5():
    var1="hello"
    return render_template('viz5.html',var1=var1)

if __name__ == "__main__":
    app.run(debug=True)