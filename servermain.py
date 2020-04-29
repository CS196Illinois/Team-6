from flask import Flask, render_template, request, redirect, url_for
import torch, torchvision
from torch import nn
from PIL import Image

model = torchvision.models.resnet34(pretrained=False)
num_feat = model.fc.in_features
model.fc = nn.Linear(num_feat, 196)
model.eval()

state_dict = torch.load('AutoVisionV4.pth', 
map_location = torch.device('cpu'))
model.load_state_dict(state_dict)

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def homepage():
	if request.method == "POST":
		print("startedprocessing")
		inputimage = request.files["img"]
		print("accepted file")
		destination = "/temp.jpg"
		inputimage.save(destination)
		pil_image = Image.open(inputimage)
		imageToPass = pil_image.convert("rgb")
		pred = model(imageToPass)
		print(pred)
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
def about():
	return render_template("about.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=1234)
	
