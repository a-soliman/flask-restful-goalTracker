from flask_restful import Resource, reqparse

from models.goal import GoalModel


class Goal(Resource):
    def get(self, _id):
        if not GoalModel.isValid_id(_id):
            return {'message': 'Invalid ID'}, 400

        goal = GoalModel.find_by_id(_id)
        if goal:
            return goal.json()
        else:
            return 'not found', 404
    
    def delete(self, _id):
        if not GoalModel.isValid_id(_id):
            return {'message': 'Invalid ID'}, 400

        goal = GoalModel.find_by_id(_id)
        if goal is None:
            return { 'messge': 'Goal was not found'}, 400
        
        try:
            goal.delete_from_db()
        except:
            return {'message': 'An Error Occured'}, 500

        return {'message': 'Deleted'}
    
    def put(self, _id):
        if not GoalModel.isValid_id(_id):
            return {'message': 'Invalid ID'}, 400
        
        #To Be CONT....
    
    
class Goals(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('name',
        type = str,
        required = True,
        help = 'name is required'
    )

    parser.add_argument('type',
        type = str,
        required = True,
        help = "Type is required"
    )

    parser.add_argument('deadline',
        type = str,
        required = True,
        help = "deadline is required"
    )


    def get(self):
        return { 'goals': [goal.json() for goal in GoalModel.get_all()]}
    
    def post(self):
        data = Goals.parser.parse_args()
        newGoal = GoalModel(_id= None,name=data['name'], _type=data['type'], deadline=data['deadline'])
        
        try:
            newGoal.save_to_db()
        except:
            return { 'message': 'An error has occured.'}, 500
        return {'message': 'Saved to DB'}, 201