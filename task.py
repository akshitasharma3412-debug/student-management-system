class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def update_title(self, new_title):
        self.title = new_title
        self.completed = False
