import UI

def run():
    root = UI.tk.Tk()
    root.title("Find Your Way in Japan, Past and Present!")
    root.geometry('720x720')

    app = UI.App(master=root)
    app.mainloop()

run()