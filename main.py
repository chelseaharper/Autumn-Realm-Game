import characterbuilder
from cProfile import label
from tkinter import *
from tkinter import messagebox

if __name__ == "__main__":
    window = Tk()
    window.wm_title("Autumn's Realm Text-based RPG")
    window.geometry("800x800")

    base_pane = PanedWindow(bd=4, relief="raised")
    base_pane.configure(bg="#766A6A")
    base_pane.pack(fill=BOTH, expand=1)

    back_frame = Frame(base_pane, bg="#766A6A")
    menu_frame = Frame(back_frame, bg="#B2A5B5", width=200, height=300, padx=10, pady=20)
    base_pane.add(back_frame)
    menu_frame.place(x=300, y=175)

    #Main Menu Commands
    def newgame():
        #messagebox.showinfo("New Game", "This feature is not yet implemented.")
        new_window = Toplevel(window)
        new_window.title("Create Character")
        new_window.geometry("300x200")
        new_window.configure(bg="#DDDDDD")

        spacer1 = Label(new_window,bg="#DDDDDD", text="")
        spacer1.grid(row=0, column=0)
        spacer2 = Label(new_window,bg="#DDDDDD", text="")
        spacer2.grid(row=0, column=1)
        character_name = Label(new_window,bg="#DDDDDD", text="Character Name")
        character_name.grid(row=2, column=2)
        character_text = StringVar()
        character_entry = Entry(new_window, textvariable=character_text)
        character_entry.grid(row=1, column=2)

        def create():
            pass
        
        exit = Button(new_window, text="Cancel", width=8, command=new_window.destroy)
        exit.grid(row=3, column=2, padx=5)
        submit = Button(new_window, text="Next", width=12, command=create)
        submit.grid(row=3, column=1, padx=5)

    def loadgame():
        messagebox.showinfo("Load Game", "This feature is not yet implemented.")

    def quitgame():
        quit_ok = messagebox.askyesno("Quit Game", "Are you sure you would like to quit?")
        if quit_ok == 1:
            window.destroy()

    #Creating the Main Menu
    new = Button(menu_frame, text="New Game", width=12, command=newgame)
    new.grid(row=1, column=1, padx=5, pady=5, sticky=EW)
    load = Button(menu_frame, text="Load Game", width=12, command=loadgame)
    load.grid(row=2, column=1, padx=5, pady=5, sticky=EW)
    endgame = Button(menu_frame, text="Quit Game", width=12, command=quitgame)
    endgame.grid(row=3, column=1, padx=5, pady=5, sticky=EW)

    

    window.mainloop()