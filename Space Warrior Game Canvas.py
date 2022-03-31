from tkinter import *
window = Tk()
window.geometry("850x650")
window.configure(bg="green")
title = window.title("Shadow Warriors")
# score = Label(window, text="SCORE :")
# score.grid(row=0, column=0)


c = Canvas(window, bg="black", height=800, width=600)
c = Canvas.create_text(c, text="Hello World")

c.pack()


window.mainloop()
