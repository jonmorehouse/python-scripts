from Tkinter import *

root = Tk()

button = Button(root, text="hello", command=quit)
button.pack()

minutes = Label(root, text="Minutes:")
minutes.pack(side=LEFT)

scale = Scale(root, from_=1, to=45, orient=HORIZONTAL, length=300)
scale.pack()

button = Button(root, text="Start timing", command=quit)
button.pack(side="left")

root.mainloop()

def function test():
	print("hello ")