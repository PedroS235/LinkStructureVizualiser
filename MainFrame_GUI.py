import graph
import webScrapper
from tkinter import *
from tkinter import messagebox
#============================
#=START OF DEFINING THE ROOT=
#============================
#instanciate the window
root = Tk()

#==========================
#=END OF DEFINING THE ROOT=
#==========================

#================================
#=START OF VARIABLES DECLARATION=
#================================
nodeVar = StringVar()
edgeVar = StringVar()
#==============================
#=END OF VARIABLES DECLARATION=
#==============================

def createGraph():
    global ws
    global g
    url = input_entry.get()
    ws = webScrapper.WebScrapper()
    if ws.is_valid(url):
        ws.crawl(url)
    else: messagebox.showwarning("Warning", "Please enter a valid URL!")
    nodes = ws.getNodes()
    edges = ws.getEdges()
    g = graph.Graph(nodes, edges)

#===================================
#=START OF CREATING THE COMPONETNTS=
#===================================

#Creating a frame
settings_frame = LabelFrame(root, text="Settings")

#creating the buttons
input_btn = Button(root, text="Input", padx=5, pady=2, command=createGraph, font=("Consolas", 14), border=1, bg="#13A8F3", fg="#FfFFFF")
show_btn = Button(root, text="View the graph", padx=5, pady=2, state=DISABLED, font=("Consolas", 14), border=1, bg="#13A8F3", fg="#FfFFFF")
nodeData_btn = Button(root, text="View the nodes data", padx=5, pady=2, state=DISABLED, font=("Consolas", 14), border=1, bg="#13A8F3", fg="#fFFFFF")
edgeData_btn = Button(root, text="View the edges data", padx=5, pady=2, state=DISABLED, font=("Consolas", 14), border=1, bg="#13A8F3", fg="#fFFFFF")
instructions_btn = Button(root, text="Instructions", padx=5, pady=2, font=("Consolas", 14), border=0)

#creating the entrys
input_entry = Entry(root, text="https://www....", font=("Consolas", 14))
nbrOfItr_entry = Entry(settings_frame, text=1, font=("Consolas", 14))

#Creating the labels
input_label = Label(root, text="URL:", font=("Consolas", 14))
nbrOfItr_label = Label(settings_frame, text="Number of iterations:", font=("Consolas", 14))

#Creating the Check boxes
node_checkBox = Checkbutton(settings_frame, text="Node color", variable=nodeVar, onvalue="On", offvalue="Off", font=("Consolas", 14))
edge_checkBox = Checkbutton(settings_frame, text="Edge color", variable=edgeVar, onvalue="On", offvalue="Off", font=("Consolas", 14))
#==================================
#=END OF CREATING THE COMPONETNTS=
#==================================

#==================================
#=START OF SHOWING THE COMPONETNTS=
#==================================

#showing the components in the settings frame
#Frame
settings_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

#entrys
nbrOfItr_entry.grid(row=0, column=1)

#labels
nbrOfItr_label.grid(row=0, column=0)

#showing the components in the root
#buttons
input_btn.grid(row=1, column=2)
show_btn.grid(row=2, column=2)
nodeData_btn.grid(row=3, column=2)
edgeData_btn.grid(row=4, column=2)
instructions_btn.grid(row=0, column=0)

#entrys
input_entry.grid(row=1, column=1, ipadx=100)
nbrOfItr_entry.grid(row=0, column=1, ipadx=10)

#labels
input_label.grid(row=1, column=0)
nbrOfItr_label.grid(row=0, column=0)

#Check boxes
node_checkBox.grid(row=1, column=0)
edge_checkBox.grid(row=2, column=0)
#================================
#=END OF SHOWING THE COMPONETNTS=
#================================
def INIT():
    #setting root
    root.title("Link Structure Vizualizer")
    root.iconbitmap("images/icon.ico")
    #root.configure(bg="#20ACF1")
    #root.geometry("650x300")
    #setting settings_frame
    #settings_frame.configure(bg="#20ACF1")
    node_checkBox.select()
    edge_checkBox.deselect()

INIT()
#main loop of the window
root.mainloop()