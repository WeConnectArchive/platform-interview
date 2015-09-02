from flask import Flask,request,render_template
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('welcome.html')

@app.route("/data")
def show_data():
   #file_name = "/var/www/interview/interview/firstlines.log"
   file_name = "/var/www/interview/interview/data/test_data.log"
   if file_name:
        return open(file_name).read()
   return  'No file selected.'

if __name__ == "__main__":
    app.run()
