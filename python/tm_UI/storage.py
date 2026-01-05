#this will handle saving and loading files

import json
from tm import Task

class Storage:
    def __init__(self, filename = "tasks.json"):
        self.filename = filename

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                tasks = json.load(file)

            task_objects = []
            for task_dict in tasks:
                task_obj = Task.from_dict(task_dict)
                task_objects.append(task_obj)
            return task_objects

        except FileNotFoundError:
            return []
        
    def save_tasks(self, tasks):
        task_dicts = []
        for task in tasks:
            task_dict = task.to_dict()
            task_dicts.append(task_dict)

        with open(self.filename, "w") as file:
            json.dump(task_dicts, file)
        

