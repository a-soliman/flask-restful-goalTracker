

class GoalModel():
    def __init__(self, _id, name, type, deadline):
        self._id = _id
        self.name = name
        self.type = type
        self.deadline = deadline
    
    def json(self):
        return { "_id": self._id, "name": self.name, "type": self.type, "deadline": self.deadline }
        
    def save_to_db(self):
        pass
    
    @classmethod
    def find_by_id(cls, _id):
        pass