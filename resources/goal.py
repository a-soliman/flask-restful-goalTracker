from flask_restful import Resource, reqparse

from models.goal import GoalModel

class Goal(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument('name',
        type=str,
        required=True,
        help="Name is required."
    )

    parser.add_argument('type',
        type=str,
        required=True,
        help="Type is required."
    )

    parser.add_argument('deadline',
        type=str,
        required=True,
        help="Deadline is required."
    )

    def get(self):
        pass

    def post(self):
        pass
    
    def put(self):
        pass
    
    def delete(self):
        pass

class Goals(Resource):
    def get(self):
        # Returns a list of the saved Goals
        pass