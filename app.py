from flask import Flask;
from flask_restful import Api, Resource, reqparse

from resources.goal import Goal

app = Flask(__name__)
api = Api(app)


api.add_resource(Goal,'/goals')

if __name__ == '__main__':
    app.run(port=3333, debug=True)