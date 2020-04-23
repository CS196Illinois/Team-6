from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def homepage():
	if request.method == "POST":
		inputimage = request.form["img"]
		return redirect(url_for("imageprocessed"))
	else:
		return render_template("index.html")

@app.route("/results", methods=["GET"] )
def imageprocessed():
	return "<h1> test </h1>"

@app.route("/contact", methods=["GET"])
def contact():
	return render_template("contact.html")

@app.route("/about", methods=["GET"])
def contact():
	return render_template("about.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=1234)
	
