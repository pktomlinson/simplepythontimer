
import time
import sys
import tkinter
from tkinter import *

class TimerGui:
        def __init__(self, master):
                self.counter = StringVar()
                self.counter.set("00:00:00")
                self.master = master
                #master.geometry("225x350")
                #master.grid_propagate(0)
                master.title("")
                self.countdown = Label(master, textvariable = self.counter)
                self.countdown.grid(row = 0, column = 0, columnspan = 2, sticky=W, padx = 5, pady = 5)
                self.countdown.config(font=("digital-7", 28))
                self.labelHrs = Label(master, text="Hours")
                self.hrs = Spinbox(master, from_ = 0, to = 23)
                self.labelHrs.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)
                self.hrs.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5)
                self.labelMns = Label(master, text="Minutes")
                self.mns = Spinbox(master, from_ = 0, to = 59)
                self.labelMns.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)
                self.mns.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 5)
                self.labelScs = Label(master, text="Seconds")
                self.scs = Spinbox(master, from_ = 0, to = 59)
                self.labelScs.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
                self.scs.grid(row = 6, column = 0, columnspan = 2, padx = 5, pady = 5)
                self.clockStart = Button(master, text="Start", command=self.startClock)
                self.clockReset = Button(master, text="Reset", command=self.clockReset)
                self.clockStart.grid(row = 7, column = 0, padx = 5, pady = 5)
                self.clockReset.grid(row = 7, column = 1, padx = 5, pady = 5)
                
        def startClock(self):
                #self.master.withdraw()
                self.c = ":"
                self.hour = int(self.hrs.get())
                self.min  = int(self.mns.get())
                self.sec  = int(self.scs.get())
                while self.hour > -1:
                        while self.min > -1:
                                while self.sec > 0:
                                        self.sec=self.sec-1
                                        time.sleep(1)
                                        self.sec1 = ('%02.f' % self.sec)  # format
                                        self.min1 = ('%02.f' % self.min)
                                        self.hour1 = ('%02.f' % self.hour)
                                        # self.countdown.after(1, self.updater())
                                        self.counter.set(str(self.hour1) + self.c + str(self.min1) + self.c + str(self.sec1))
                                        self.countdown.update()
                                self.min=self.min-1
                                self.sec=60
                        self.hour=self.hour-1
                        self.min=59
                else:
                        self.counter.set("Done!")
                        self.clockReset

        def clockReset(self):
                self.hour = 0
                self.min = 0
                self.sec = 0
                self.master.update()
                #self.master.deiconify()
        def dummy(self):
                pass
                
root = Tk()
timer_gui = TimerGui(root)
root.mainloop()

