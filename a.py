from tkinter import Entry, Tk
root = Tk()
def callback(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False
vcmd = (root.register(callback))

w = Entry(root, validate='all', validatecommand=(vcmd, '%P')) 
w.pack(padx=20, pady=20)

root.mainloop()