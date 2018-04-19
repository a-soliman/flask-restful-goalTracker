
class GoalModel():
    def __init__(self, _id, name, type, deadline):
        self._id = _id
        self.name = name
        self.type = type
        self.deadline = deadline
    
    def json(self):
        return { "_id": self._id, "name": self.name, "type": self.type, "deadline": self.deadline }

    def save_to_db(self):
        goals.append(self)
    
    def update_in_db(self):
        pass
    def remove_from_db(self):
        index = goals.index(self)
        goals.pop(index)
        return
    
    @classmethod
    def get_goals(cls):
        return goals
    
    @classmethod
    def find_by_id(cls, _id):
        for goal in goals:
            if goal._id == _id:
                return goal

        return None

goal1 = GoalModel('1', 'learn something new', 'Professional', 'tomorrow')
goal2 = GoalModel('2', 'learn something new', 'Professional', 'tomorrow')
goal3 = GoalModel('3', 'learn something new', 'Professional', 'tomorrow')
goals = [ goal1, goal2, goal3 ]