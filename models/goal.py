# from db import db
from bson.objectid import ObjectId

class GoalModel():
    def __init__(self, _id, name, _type, deadline):
        self._id = str(_id)
        self.name = name
        self.type = _type
        self.deadline = deadline
    
    def json(self):
        return {"_id": self._id, "name": self.name, "type": self.type, "deadline": self.deadline}
    
    def save_to_db(self):
        goals_collection = db.goals
        goal_id = goals_collection.insert_one({"name": self.name, "type": self.type, "deadline": self.deadline}).inserted_id
        return goal_id
    
    def delete_from_db(self):
        goals_collection = db.goals
        result = goals_collection.delete_one({'_id': ObjectId(self._id)})
        return result

    def update_in_db(self):
        goals_collection = db.goals
        goals_collection.update({ "_id": ObjectId(self._id)}, {"$set": {"name": self.name, "type": self.type, "deadline": self.deadline}}, upsert=False)
        return 

    @classmethod
    def isValid_id(cls, _id):
        return ObjectId.is_valid(_id)
        
    @classmethod
    def get_all(cls):
        goals_collection = db.goals
        goals = []

        for goal in goals_collection.find():
            goal = GoalModel(goal['_id'], goal['name'], goal['type'], goal['deadline'])
            goals.append(goal)
        return goals

    @classmethod
    def find_by_id(cls, _id):
        goals_collection = db.goals
        result = goals_collection.find_one({'_id': ObjectId(_id)})
        
        try:
            goal = GoalModel(result['_id'], result['name'], result['type'], result['deadline'])
        except:
            return None

        return goal



    