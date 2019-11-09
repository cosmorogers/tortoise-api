import Adafruit_DHT
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Environment(Resource):
    def get(self):
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
        return {'temperature': temperature, 'humidity': humidity}


api.add_resource(HelloWorld, '/')
api.add_resource(Environment, '/environment')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
