from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def save():
    return render_template("index.html")
@app.route("/about")
def save1():
    return render_template("about.html")
@app.route("/service")
def save2():
    return render_template("service.html")
if __name__=="__main__" :
    app.run(debug=True)