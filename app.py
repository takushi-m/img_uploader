import os
from flask import Flask,render_template,request,url_for,redirect
from werkzeug import secure_filename
app = Flask(__name__)

@app.route("/")
def index():
    files = ["/static/"+file for file in os.listdir("./static") if file!=".gitignore"];
    return render_template("index.html", imgs=files)

@app.route("/send", methods=["GET","POST"])
def send():
    if request.method == "POST":
        img_file = request.files["img_file"]
        filename = secure_filename(img_file.filename)
        img_file.save(os.path.join("./static", filename))

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.debug = True
    app.run()
