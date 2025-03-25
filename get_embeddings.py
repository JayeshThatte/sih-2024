# importing tkinter and tkinter.ttk
# and all their functions and classes
from tkinter import * 
from tkinter.ttk import *
import face_recognition
import json

datas = {}
# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile
  
root = Tk()
root.geometry('200x100')
  
# This function will be used to open
# file in read mode and only Python files
# will be opened
def open_file():
    file = askopenfile(mode ='r')
    photo = face_recognition.load_image_file(file.name)
    encoding = face_recognition.face_encodings(photo,model="large",num_jitters=1)
    if len(encoding):
        print(f"{file.name} recognised")
        encoding = encoding[0]
        with open(f"user.json","w") as f:
            datas["data"] = encoding.tolist()
            json.dump(datas,f)
    else:
        print(f"{file.name} not found")

  
btn = Button(root, text ='Open', command = lambda:open_file())
btn.pack(side = TOP, pady = 10)
  
mainloop()


# run the application
root.mainloop()