from datetime import datetime

class Note:
    def __init__(self, id, title, text, timestamp):
        self.id = id
        self.title = title
        self.text = text
        self.timestamp = timestamp


    def noteCreator(id):
        title = input("Enter note title: ")
        text = input("Enter note text: ")
        timestamp =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return Note(id, title, text, timestamp)