from flask import Flask
from flask_restful import Api

from resources.goal import Goal, Goals

app = Flask(__name__)
api = Api(app)


      
api.add_resource(Goals, '/goals')
api.add_resource(Goal, '/goals/<string:_id>')

if __name__ == '__main__':
    app.run(port=5555 , debug=True)