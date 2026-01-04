#task class code

from datetime import datetime

class Task:
    def __init__(self, title, category, due_date, completed=False):
        self.title = title
        self.category = category
        self.due_date = due_date
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def to_dict(self):
        tm_dict = {
            "title": self.title,
            "category": self.category,
            "due_date": self.due_date,
            "completed": self.completed
        }
        return tm_dict
    
    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["category"], data["due_date"], data["completed"])

    def is_overdue(self):
        if self.completed:
            return False
        
        due = datetime.strptime(self.due_date, "%m-%d-%Y")
        today = datetime.now()

        if due.date() < today.date():
                return True
        else:
            return False

            