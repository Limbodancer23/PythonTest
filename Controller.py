import csv
from datetime import datetime
from Note import Note


class Operations:
    def __init__(self):
        self.notes = []
    
    def makeNote(self, note):
        self.notes.append(note)
    
    def findNote(self):
        target_id = input("Enter id of note: ")
        for note in self.notes:
            if target_id == str(note.id):
                print(f"Note - {note.id};title:{note.title};text:{note.text};date:{note.timestamp}")
        return None
    
    def findByDate(self):
        date = input("Enter date creation of note(yyyy-mm-dd): ")
        try:
            if len(self.notes) == 0:
                print("Notes not found...")
            if self.notes:
                filtered_notes = [note for note in self.notes if str(note.timestamp)[0:-9] == date]
                if not filtered_notes:
                    print("Not found any notes by this period.")
                else:
                    Operations.print_notes(self, filtered_notes)
        except ValueError:
            print("Wrong date format...")
        
    def print_notes(self, notes):
        if not notes:
            print("Notes not found.")
        else:
            for note in notes:
                print(f"Note - {note.id};title:{note.title};text:{note.text};date:{note.timestamp}")

    def deleteNote(self, filename):
        target_id = input("Enter id of note: ")
        for note in self.notes:
            if str(note.id) == target_id:
                self.notes.remove(note)
                print("Note deleted!")
        Operations.saveNotes(self, filename)
    
    def editNote(self, filename):
        target_id = input("Enter id of note: ")
        for note in self.notes:
            if str(note.id) == target_id:
                note.title = input("Enter new title: ")
                note.text = input("Enter new text: ")
                note.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                Operations.saveNotes(self, filename)
                print("Note edited!")
    
    def saveNotes(self, filename):
        with open(filename, 'w', newline= '') as f:
            writer = csv.writer(f, delimiter= ';')
            # writer.writerow(['id','title', 'text', 'timestamp'])
            for note in self.notes:
                writer.writerow([note.id, note.title, note.text, note.timestamp])
        f.close
        print("Notes saved!")

    def ReadAll(self, filename, flag):
        try:
            with open(filename, 'r', newline= '') as f:
                reader = csv.reader(f, delimiter=';')
                # next(reader)
                for row in reader:
                    if not flag:
                        print(row)
                    if flag:
                        id = int(row[0])
                        title = row[1]
                        text = row[2]
                        timestamp = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                        note = Note(id, title, text, timestamp)
                        self.notes.append(note)
        except StopIteration:
            print("Notes not found!")
        finally:
            f.close    

    def LoadId(self, filename):
        idHolder = set()
        with open(filename, 'r', newline= '') as r:
            reader = csv.reader(r, delimiter= ';')
            for row in reader:
                id = int(row[0])
                idHolder.add(id)
        return idHolder