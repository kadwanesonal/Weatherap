import requests
from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

key = '858903c117ce37e1d58e2e48bf42c458'

@app.route('/cityweather')
def weatherFromCity():
    city = request.args.get('city')
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+key
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/geocoordweather')
def weatherFromGeocoordinates():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    url = 'http://api.openweathermap.org/geo/1.0/reverse?lat='+latitude+'&lon='+longitude+'&limit=5&appid='+key
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(debug=True)