class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments=[]
        self.completed = False

    def change_name(self, new_name: str):
        if self.name ==new_name:
            return "Name cannot be the same."
        self.name = new_name
        return self.name

    def change_due_date(self,new_date: str) :
        if self.due_date == new_date:
            return "Date cannot be the same."
        self.due_date = new_date
        return self.due_date

    def add_comment(self,comment: str):
        self.comments.append(comment)

    def edit_comment(self,comment_number: int, new_comment: str):
        if comment_number not in range(len(self.comments)):
            return "Cannot find comment."
        self.comments[comment_number] = new_comment
        return f"{', '.join ( self.comments)}"

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


class Section :
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in [task.name for task in self.tasks]:
            return f"Could not find task with the name {task_name}"
        task = [t for t in self.tasks if t.name == task_name][0]
        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        counter = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                counter+=1
        return f"Cleared {counter} tasks."

    def view_section(self):
        res = f"Section {self.name}:" + "\n"
        for task in self.tasks:
            res += f"{task.details ()}" + "\n"
        return res





task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
