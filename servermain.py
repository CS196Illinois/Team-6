from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def homepage():
	if request.method == "POST":
		inputimage = request.form["img"]
		return redirect(url_for("imageprocessed"))
	else:
		return render_template("index.html")

@app.route("/results")
def imageprocessed():
	return "<h1> test </h1>"


if __name__ == "__main__":
	app.run()
	
