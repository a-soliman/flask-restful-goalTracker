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

    def get(self, id):
        goal = GoalModel.find_by_id(id)

        if goal is None:
            return {'message': 'Not found'}, 404
        return goal.json()
    
    def put(self, id):
        pass
    
    def delete(self, id):
        goal = GoalModel.find_by_id(id)
        if goal is None:
            return {'message': 'Goal not found'}, 400
        
        try:
            goal.remove_from_db()
        except:
            return {'message': 'An Error accoured'}, 500
        
        return {'message': 'removed Goal'}


class Goals(Resource):
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
        # Returns a list of the saved Goals
        return {'Goals': [goal.json() for goal in GoalModel.get_goals()]}

    def post(self):
        # Addes a new Goal
        data = Goals.parser.parse_args()

        newGoal = GoalModel('someID', data['name'], data['type'], data['deadline'])
        
        try:
            newGoal.save_to_db()
        except:
            return {'message': 'An Error accourd while saving.'}, 500
        
        return {'message': 'Added Goal'}, 201

        
        
