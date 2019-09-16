import socket
from flask import Flask, request
from flask_restful import Api, Resource
from pythonping import ping

app = Flask(__name__)
api = Api(app)
port = 9400

class get_latency(Resource):
    def post(self):
        content = request.get_json(silent=True)
        response_list = ping(content.get('client_ip'), size=40, count=3)
        return {'average_latency':response_list.rtt_avg_ms}




class get_collecter_ip(Resource):
    def get(self):
        return socket.gethostbyname(socket.gethostname())


api.add_resource(get_latency,'/get_latency')
api.add_resource(get_collecter_ip,'/get_collecter_ip')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True, port=port)