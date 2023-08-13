import os
from Controller import Operations
from Note import Note
class View:
    def start(filename):
        print("Welcome to Test 'Notes'!!!")
        unique_id = set()
        op = Operations()

        if os.path.isfile(filename):
            op.ReadAll(filename, True)
            unique_id = op.LoadId(filename)
            print("File exist!")
            
        else:
            try:
                with open(filename, 'a') as f:
                    f.close
            except Exception:
                    print("Error")
            finally:
                f.close

        while(True):
            print("---------------------------------------------------")
            choice = input("Choose from below: \n1)show my notes\n2)Make new note\n3)Save notes.\n4)Find note with index\n5)Show notes by date\n6)Edit note\n7)Delete\n8)Exit\n")
            match choice:
                case "1":
                    op.ReadAll(filename, False)
                case "2":
                    id = input("Enter note id: ")
                    if int(id) in unique_id:
                        print("This id already used!")
                    elif id not in unique_id:
                        unique_id.add(id)
                        newNote = Note.noteCreator(id)
                        op.makeNote(newNote)
                case "3":
                    op.saveNotes(filename)
                case "4":
                    op.findNote()
                case "5":
                    op.findByDate()
                case "6":
                    op.editNote(filename)
                case "7":
                    op.deleteNote(filename)
                case "8":
                    break

        
