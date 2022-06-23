
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

def paceD():
    pDist = float(paceDistance.get())
    thour = timeHR.get()
    tMin = timeMin.get()
    tSec = timeSec.get()

    time = ((thour * 3600) + (tMin * 60) + tSec)
    pace = time/pDist
    print(divmod(pace,60))

def dConversion():
    selection_var.get()
    toBeConverted = float(distEntryConv.get())
    if selection_var.get() == KM:
        print(divmod(toBeConverted,0.621371))
    elif selection_var.get() == Miles:
        print(toBeConverted*0.621371)

#creates the window for the GUI
root = tk.Tk()
root.geometry("750x450")
root.resizable(False, False)
root.title("Daily Tracker")

#set style
rootStyle = ttk.Style(root)
rootStyle.theme_use("aqua")


dUnitLabel=ttk.Label(root, text="Pick the unit for your pace:")
dUnitLabel.place(x=20, y=70)
dMeasure = tk.StringVar()
dBox = ttk.Combobox(root, textvariable=dMeasure, width=5)
dBox["values"] = ("Miles","KM")
dBox.place(x=20,y=90)

timeHR = tk.IntVar()
timeMin = tk.IntVar()
timeSec = tk.IntVar()
paceTimeLabel=ttk.Label(root,text="Enter a total run time: ")
paceTimeLabel.place(x=20,y=110)
timeEntryHR = ttk.Entry(root, width=3, textvariable=timeHR)
timeEntryHR.place(x=20, y=130)
timeEntryMin = ttk.Entry(root, width=3, textvariable=timeMin)
timeEntryMin.place(x=70, y=130)
timeEntrySec = ttk.Entry(root, width=3, textvariable=timeSec)
timeEntrySec.place(x=120, y=130)

paceDistance = tk.IntVar()
paceDistanceLabel=ttk.Label(root,text="Enter a distance to determine the pace: ")
paceDistanceLabel.place(x=20,y=160)
distanceEntry = ttk.Entry(root, width=5, textvariable=paceDistance)
distanceEntry.place(x=20, y=180)


paceTimeHR = tk.IntVar()
paceTimeMin = tk.IntVar()
paceTimeSec = tk.IntVar()
paceTimeLabel=ttk.Label(root, text="Enter a pace time:")
paceTimeLabel.place(x=20, y=220)
paceEntryHR = ttk.Entry(root, width=3, textvariable=paceTimeHR)
paceEntryHR.place(x=20, y=240)
paceEntryMin = ttk.Entry(root, width=3, textvariable=paceTimeMin)
paceEntryMin.place(x=70, y=240)
paceEntrySec = ttk.Entry(root, width=3, textvariable=paceTimeSec)
paceEntrySec.place(x=120, y=240)

#distance conversion
distConvLabel = ttk.Label(root, text="Enter the distance to convert: ")
distConvLabel.place(x=400, y=70)
distConv = tk.StringVar()
distEntryConv = ttk.Entry(root, width=5, textvariable=distConv)
distEntryConv.place(x=400, y=90)

selection_var = tk.StringVar()
KM = ttk.Radiobutton(
    root,
    text = "To KM",
    variable=selection_var,
    value="KM")
Miles = ttk.Radiobutton(
    root,
    text = "To Miles",
    variable=selection_var,
    value="Miles")

KM.place(x=400, y=115)
Miles.place(x=400, y=135)
convert_button = ttk.Button(root, text="Convert", command=dConversion)
convert_button.place(x=400,y=165)

#calculate pace buttion
pace_button = ttk.Button(root, text="Calculate Pace", command=paceD)
pace_button.place(x=200,y=260)



#creates a button that quits program

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.place(x=625,y=400)

# save_data_button = ttk.Button(root, text="Save Data", command=save_data)
# save_data_button.place(x=375,y=350)

root.mainloop()
