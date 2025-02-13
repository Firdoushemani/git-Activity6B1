class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        return self.tasks

if __name__ == "__main__":
    todo = ToDoList()
    todo.add_task("Complete GitHub project")
    print("Tasks:", todo.show_tasks())
