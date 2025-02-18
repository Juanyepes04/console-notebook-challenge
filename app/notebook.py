from datetime import datetime


class Note:
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'

    def __init__(self, code: int, title: str, text: str, importance: str):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()
        self.tags = []

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"date: {self.creation_date}\n{self.title}: {self.text}"

class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, title: str, text: str, importance: str):
        code = len(self.notes) + 1
        new_note = note(code, title, text, importance)








