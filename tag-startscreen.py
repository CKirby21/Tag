from tkinter import *
import tag

def quit_me():
    root.quit()
    root.destroy()

def start(entSpeed, entTime, entPlayer, entScreenWidth, entScreenHeight):
    quit_me()
    tag.Main(entSpeed, entTime, entPlayer, entScreenWidth, entScreenHeight)

if __name__ == '__main__':

    root = Tk()
    root.protocol("WM_DELETE_root", quit_me)
    root.title('Welcome')
    root.geometry('400x400')
    root.resizable(False,False)
    
    FONT = ("Times New Roman", 16, 'bold')
    lbl = Label(root, text="TAG", font = ("Times New Roman", 32, 'bold'))
    lbl.pack(side=TOP, pady=5)

    lbl = Label(root, text="Speed:", font = FONT)
    lbl.pack()

    entSpeed = Entry(root)
    entSpeed.insert(0, "3")
    entSpeed.pack()

    lbl = Label(root, text="Time (s):", font = FONT)
    lbl.pack()

    entTime = Entry(root)
    entTime.insert(0, "10")
    entTime.pack()

    lbl = Label(root, text="Player (px):", font = FONT)
    lbl.pack()

    entPlayer = Entry(root)
    entPlayer.insert(0, "20")
    entPlayer.pack()

    lbl = Label(root, text="Screen Width (px):", font = FONT)
    lbl.pack()

    entScreenWidth = Entry(root)
    entScreenWidth.insert(0, "400")
    entScreenWidth.pack()

    lbl = Label(root, text="Screen Height (px):", font = FONT)
    lbl.pack()

    entScreenHeight = Entry(root)
    entScreenHeight.insert(0, "400")
    entScreenHeight.pack()

    btn = Button(root, text="Start", font = FONT, command=lambda: start(entSpeed.get(), entTime.get(), entPlayer.get(), entScreenWidth.get(), entScreenHeight.get()))
    btn.pack(pady=10)
   
    root.mainloop()