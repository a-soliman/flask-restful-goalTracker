from flask import Flask, send_from_directory, template_rendered
from flask_restful import Resource, Api

from resources.goal import Goal, Goals

app = Flask(__name__)
api = Api(app)


      
api.add_resource(Goals, '/goals')
api.add_resource(Goal, '/goals/<string:_id>')

if __name__ == '__main__':
    app.run(port=5000 , debug=True)