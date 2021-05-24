import UI

def run():
    root = UI.tk.Tk()
    root.title("Fastest Land Routes through Japan from the Tokugawa Period to Modern Day")
    root.geometry('720x720')

    app = UI.App(master=root)
    app.mainloop()

run()