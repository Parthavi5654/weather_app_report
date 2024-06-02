from flask import Flask , render_template , request
import requests

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/weatherapp' , methods = ['POST' , "GET"])
def get_weatherdate():
    url = "http://api.weatherapi.com/v1/current.json"

    parameters = {
    'key' : request.form.get('appid')  , 
    'q' : request.form.get("city")
    }

    row_data = requests.get(url ,params = parameters)   
    city = Data['name'] #change
    Data = row_data.json()

    return f"report : {Data}"



if __name__ == '__main__':
    app.run(host ="0.0.0.0")
