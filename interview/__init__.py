from flask import Flask,request
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"

@app.route("/data")
def show_data():
   #file_name = "/var/www/interview/interview/firstlines.log"
   file_name = "/var/www/interview/interview/data/test_data.log"
   if file_name:
        return open(file_name).read()
   return  'No file selected.'

if __name__ == "__main__":
    app.run()
