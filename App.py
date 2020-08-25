import tkinter as tk
from tkinter import messagebox as mbox
from mp3_wav_convert import Converter
import os


root = tk.Tk()
root.title("mp3 wav Converter")

def process():
	file = r'%s' % entry2.get()
	directory = r'%s' % entry1.get()
	if len(file) == 0 or len(directory) == 0:
		mbox.showerror(title="Empty", message="One or both entry fields are empty")
	else:
		try:
			os.listdir(directory)
		except FileNotFoundError:
			mbox.showerror(title="File Not Found", message="Can't find the file/directory")
		else:
			engine = Converter(directory, file)
			if ".mp3" in file:
				engine.mp3_to_wav()
				mbox.showinfo(title="Success!", message="File Successfully Converted")
			elif ".wav" in file:
				engine.wav_to_mp3()
				mbox.showinfo(title="Success!", message="File Successfully Converted")

pane = tk.Canvas(root, height="200", width="400", bg="light gray")
pane.pack()

Directory = tk.Label(pane, text="Enter Directory", font=("calibri", 15), bg="light gray")
Directory.place(relx=0.1, rely=0.1)

entry1 = tk.Entry(pane, font=("calibri", 15))
entry1.place(relx=0.1, rely=0.25)

File = tk.Label(pane, text="Enter Filename", font=("calibri", 15), bg="light gray")
File.place(relx=0.1, rely=0.4)

entry2 = tk.Entry(pane, font=("calibri", 15))
entry2.place(relx=0.1, rely=0.55)

button = tk.Button(pane, text="Convert", font=("calibri", 15), command=process)
button.place(relx=0.1, rely=0.75)

root.mainloop()

