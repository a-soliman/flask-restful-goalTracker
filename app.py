from flask import Flask
from flask_restful import Api
from db import db


from resources.goal import Goal, Goals

app = Flask(__name__, static_url_path='/dist')
api = Api(app)

@app.route('/')
def root():
    return app.send_static_file('index.html')

api.add_resource(Goals, '/goals')
api.add_resource(Goal, '/goals/<string:_id>')

if __name__ == '__main__':
    app.run(port=5555 , debug=True)