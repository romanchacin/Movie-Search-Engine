import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import Functions


root = tk.Tk()

root.title("MOVIES")
root.wm_geometry("750x660+0+0")
root.resizable(False, False)
root.config(bg="#1CC")
frame = tk.Frame(root, bg="#1CC")
frame.config(width=800, height=800)

frame.pack()

image1 = Image.open("FondoAzul.png")
image1 = image1.resize((300,400), Image.Resampling.LANCZOS)
imageSIZE = ImageTk.PhotoImage(image1, width=300, height=400)
labelIMG = tk.Label(frame, image=imageSIZE)
labelIMG.place(x=0,y=0)
labelIMG.grid(row=0, column=0, columnspan=3, rowspan=5, padx=20, pady=20)

labelNAME = tk.Label(frame, text="Name of the Movie: ")
labelNAME.grid(row=5,column=0,padx=5,pady=10,sticky="e")

entryNAME = tk.Entry(frame)
entryNAME.grid(row=5,column=1,padx=10,pady=10)

labelYEAR = tk.Label(frame, text="Year: ")
labelYEAR.grid(row=6,column=0,padx=5,pady=10,sticky="e")

entryYEAR = tk.Entry(frame)
entryYEAR.grid(row=6,column=1,padx=10,pady=10)

labelDATE = tk.Label(frame, text="Date: ")
labelDATE.grid(row=0,column=3,padx=5,pady=10,sticky="e")

entryDATE = tk.Entry(frame,state="readonly")
entryDATE.grid(row=0,column=4,padx=10,pady=10)

labelRunTime = tk.Label(frame, text="RunTime: ")
labelRunTime.grid(row=1,column=3,padx=5,pady=10,sticky="e")

entryRUNTIME = tk.Entry(frame,state="readonly")
entryRUNTIME.grid(row=1,column=4,padx=10,pady=10)

labelRating = tk.Label(frame, text="Rating: ")
labelRating.grid(row=2,column=3,padx=5,pady=10,sticky="e")

entryRATING = tk.Entry(frame,state="readonly")
entryRATING.grid(row=2,column=4,padx=10,pady=10)

labelPlot = tk.Label(frame, text="Plot: ")
labelPlot.grid(row=3,column=3,padx=5,pady=10,sticky="e")

scrollbar = tk.Scrollbar(frame, orient="vertical")

textPLOT = tk.Text(frame,state="disabled")
textPLOT.grid(row=3,column=4,padx=10,pady=10)
textPLOT.config(width=30,height=10,yscrollcommand=scrollbar.set)
scrollbar.config(command=textPLOT.yview)

scrollbar.grid(row=3,column=5,sticky="ns")

botonSEARCH = tk.Button(frame, text="SEARCH", bg="#4BF86D",command=lambda: Functions.SEARCH(labelIMG,entryNAME,entryYEAR,entryDATE,entryRUNTIME,textPLOT,entryRATING))
botonSEARCH.grid(row=7,column=0,padx=10,pady=10)

botonDELETE = tk.Button(frame, text="DELETE ALL", bg="#F8A74B",command= lambda: Functions.DELETE_ALL(labelIMG,entryNAME,entryYEAR,entryDATE,entryRUNTIME,textPLOT,entryRATING))
botonDELETE.grid(row=7,column=1,padx=10,pady=10)

message = """Enter the full name and release year of a movie. With the help of OMDb API, I will show you the exact release date, movie length, rating, and plot. Here are some examples:
1. Cars 2 (2011)
2. Onward (2020)
3. The Hunger Games (2012)
4. Titanic (1997)
5. Don't Look Up (2021)
"""

textEXAMPLE = tk.Text(frame)
textEXAMPLE.grid(row=5,column=3,columnspan=3, rowspan=3,padx=10,pady=10)
textEXAMPLE.config(width=40,height=10)
textEXAMPLE.insert(1.0,message)
textEXAMPLE.config(state="disabled")

root.mainloop()
