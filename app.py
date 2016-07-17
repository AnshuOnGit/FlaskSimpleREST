#!flask/bin/python
from flask import Flask, jsonify, request
import api


app = Flask(__name__)

cities = api.loadDB()

@app.route('/')
def root():
    return "Hello, World!"

@app.route('/all_cities', methods=['GET'])
def list_all_countries():
    return jsonify({'cities': cities})

@app.route('/city_by_name/<city_name>', methods=['GET'])
def get_a_particular_city(city_name):
    return jsonify({'requested_city' :
                        [x for x in cities if x.get('name') == city_name]})

@app.route('/create_city/', methods=['POST'])
def create_city():
    new_city = {'name' :request.json['name'],
                'lat': request.json['lat'],
                'lon': request.json['lon'] }
    cities.append(new_city)
    api.writeToDB(cities)
    return jsonify(new_city)

@app.route('/update_city/<city_name>', methods=['PUT'])
def update_city(city_name):
    updated = False
    for city in cities:
        if city.get('name') == city_name:
            city['lat'] = request.json['lat']
            city['lon'] = request.json['lon']
            updated = True
    if updated:
        api.writeToDB(cities)
        return jsonify({'successfully Updated': request.json})
    else:
        return('city not found.')



if __name__ == '__main__':
    app.run(debug=True)