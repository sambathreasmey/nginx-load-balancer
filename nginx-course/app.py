from flask import Flask, render_template
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

app_name = os.getenv("APP_NAME")

@app.route("/")
def start():
    return render_template("index.html", app_name=app_name)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)