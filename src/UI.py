import tkinter as tk
import pathfinder as pf
import timestuff as ts
import roadgenerator as rg
import copy

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createRoads()
        self.periodno = ts.TOKUGAWA
        self.images = [tk.PhotoImage(file="fiveroads.gif"),tk.PhotoImage(file="ImperialRailways.gif"),tk.PhotoImage(file="shinkasen.gif")]
        self.periods = {"Tokugawa":0,"Meiji":1,"Modern":2}
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.startMenu = None
        self.createWidgets()

    def createRoads(self):
        #fiveRoads = rg.createRoadsFromFile("C:\\Users\\Jack\\3D Objects\\HIS70A\\src\\FiveRoads.txt")
        fiveRoads = rg.createRoadsFromFile("FiveRoads.txt")
        shinkansen = rg.createRoadsFromFile("Shinkansen.txt")
        imperial = rg.createRoadsFromFile("ImperialRailway.txt")
        self.roadtimes = [ts.buildGraphFromRoadLengths(fiveRoads, ts.TOKUGAWA), ts.buildGraphFromRoadLengths(imperial, ts.MEIJI), ts.buildGraphFromRoadLengths(shinkansen, ts.MODERN)]

    def createWidgets(self):
        #self.img = tk.PhotoImage(file="fiveroads.gif")
        self.img = self.images[0]
        self.map = tk.Label(self,image = self.img)
        self.map.pack(side = "top")

        self.periodsMenu = tk.Menubutton(self, text="Period",width=6,height=1,relief=tk.RAISED,direction='left')
        self.periodsMenu.menu = tk.Menu(self.periodsMenu, tearoff=0)
        self.periodsMenu['menu'] = self.periodsMenu.menu
        self.period = tk.StringVar()
        self.period.trace("w",self.changePeriod)
        self.periodsMenu.menu.add_radiobutton(label = "Tokugawa", variable=self.period)
        self.periodsMenu.menu.add_radiobutton(label = "Meiji", variable=self.period)
        self.periodsMenu.menu.add_radiobutton(label = "Modern", variable=self.period)
        self.periodsMenu.pack(side="left")
        self.pathtime = tk.Label(self)
        self.pathtime.pack(side='bottom')

        self.period.set("Tokugawa")

        self.rightWidgets()

    def changePeriod(self, *args):
        #print(self.period.get())
        if self.startMenu != None:
            self.deleteAllTowns()
        self.periodno = self.periods[self.period.get()]
        self.map.pack_forget()
        self.map = tk.Label(self,image=self.images[self.periodno])
        self.map.pack(side="top")
        if self.startMenu != None:
            for town in self.roadtimes[self.periodno]:
                self.startMenu.menu.add_radiobutton(label = town, variable=self.start)
                self.endMenu.menu.add_radiobutton(label = town, variable=self.end)
        self.days, self.hours, self.minutes = 0,0,0
        self.pathtime.config(text="Shortest time estimate for the " + self.period.get() + " Era is " + str(self.days) + " Days, " + str(self.hours) + " Hours, " + str(self.minutes) + " Minutes")

    def rightWidgets(self):
        self.getTime = tk.Button(self,width=12,height=1)
        self.getTime["text"] = "Find fastest time"
        self.getTime["command"] = self.search
        self.getTime.pack(side="bottom")

        self.startMenu = tk.Menubutton(self, text="Start Town",width=12,height=1,relief=tk.RAISED,direction='right')
        self.startMenu.menu = tk.Menu(self.startMenu, tearoff=0)
        self.startMenu['menu'] = self.startMenu.menu
        self.start = tk.StringVar()
        self.endMenu = tk.Menubutton(self, text="End Town",width=12,height=1,relief=tk.RAISED,direction='right')
        self.endMenu.menu = tk.Menu(self.endMenu, tearoff=0)
        self.endMenu['menu'] = self.endMenu.menu
        self.end = tk.StringVar()
        for town in self.roadtimes[self.periodno]:
            self.startMenu.menu.add_radiobutton(label = town, variable=self.start)
            self.endMenu.menu.add_radiobutton(label = town, variable=self.end)
        self.endMenu.pack(side="bottom")
        self.startMenu.pack(side="bottom")

    def search(self):
        roads = copy.deepcopy(self.roadtimes[self.periodno])
        path, time = pf.shortestPath(self.start.get(),self.end.get(),roads)
        self.days, self.hours, self.minutes = ts.minutesToMore(time)
        self.pathtime.config(text="Shortest time estimate for the " + self.period.get() + " Era is " + str(self.days) + " Days, " + str(self.hours) + " Hours, " + str(self.minutes) + " Minutes")

    def deleteAllTowns(self):
        for town in self.roadtimes[self.periodno]:
            self.startMenu.menu.delete(town)
            self.endMenu.menu.delete(town)