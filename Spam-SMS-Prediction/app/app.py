from flask import Flask,render_template,request
from model import predict

app = Flask(__name__)

@app.route('/')
def index():
   return render_template("./index.html")

@app.route('/check_email_status', methods=["POST"])
def check_email_status():
   text = request.form["message"]
   return predict(text)

if __name__ == '__main__':
   app.run(host='0.0.0.0')