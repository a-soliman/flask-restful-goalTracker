from flask import Flask;
from flask_restful import Api, Resource, reqparse

from resources.goal import Goal, Goals

app = Flask(__name__)
api = Api(app)


api.add_resource(Goal,'/goals/<string:id>')
api.add_resource(Goals, '/goals')

if __name__ == '__main__':
    app.run(port=3333, debug=True)