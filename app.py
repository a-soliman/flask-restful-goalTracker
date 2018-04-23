from flask import Flask, send_from_directory
from flask_restful import Api
from db import db


from resources.goal import Goal, Goals

app = Flask(__name__, static_url_path='')
api = Api(app)

@app.route('/<path:path>')
def serve_page(path):
    return app.send_static_file('index.html')

      
api.add_resource(Goals, '/goals')
api.add_resource(Goal, '/goals/<string:_id>')

if __name__ == '__main__':
    app.run(port=5555 , debug=True)