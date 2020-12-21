# import Graph
# import WebScrapper
import tkinter as tk
from tkinter import messagebox

run = True
try:
    import Graph
    import WebScrapper
    run = True
except ModuleNotFoundError as e:
    messagebox.showerror(" Module Not Found Error", f"Please make sure to install all the prerequisits before running the program!\nError raised: {e}")
    run = False

class Application(tk.Frame):
    def __init__(self, master=None):
        """
        This is the constructor of this application
        and it sets the default values
        """
        super().__init__(master)
        self.master = master
        self.create_widgets() #creates all the widgets
        self.display_widgets()  #Displays all the widgets
        self.node_checkBox.select() #sets the default 
        self.edge_checkBox.deselect()   #sets the default 
        self.bl_checkBox.select() #sets the default 
        self.nbrOfItr_entry.insert(0, 1) #sets the default 
        self.input_entry.insert(0, "https://infallible-varahamihira-e94f86.netlify.app/") #inputs to the entry input the url from the testing website just to show an example
        self.prev_input_val = "" #this is the variable for the input entry, this variable holds the privious value that was in the entry
        self.prev_iterations_val = "" #this is the variable for the input entry, this variable holds the privious value that was in the entry

    def create_graph(self):
        """
        This method creates the graph when the button input is clicked
        """
        self.ws = WebScrapper.WebScrapper() #instanciates the class Webscraper
        self.G = Graph.Graph() #instanciates the class Graph
        url = self.input_entry.get().replace(" ", "") #gets the url from the entry and if it contains whitespaces it removes them
        #checks if the input URL is valid 
        if self.ws.is_valid(url):
            self.ws.set_nbr_iterations(int(self.nbrOfItr_entry.get()))
            self.ws.setBrokenLink(self.blVar.get())
            self.ws.crawl(url)
            self.nodes = self.ws.getNodes()
            self.edges = self.ws.getEdges()
            self.ws.writeNodesEdgesToAFile()
            self.show_btn['state'] = tk.NORMAL
            self.nodeData_btn['state'] = tk.NORMAL
            self.edgeData_btn['state'] = tk.NORMAL
            if self.blVar.get() == True:
                self.brokenLink_btn['state'] = tk.NORMAL
            else:
                self.brokenLink_btn['state'] = tk.DISABLED
        else:
            messagebox.showerror("Invalid URL", "Please make sure that the URL is valid!")

    def show_graph(self):
        """
        This method will display the graph when the button "show graph" is clicked
        """
        #checks if the input URL is valid 
        self.G.drawGraph(self.nodes, self.edges, self.nodeVar.get(), self.edgeVar.get())
        self.G.showGraph()

    def open_nodeData(self):
        """
        This method will open a .txt file, containing all the nodes 
        of the graph, when the button "View the nodes data" is clicked
        """
        import os, sys, subprocess

        if sys.platform == "win32":
            os.startfile("data\\nodes.txt")
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "data/nodes.txt"])

    def open_edgeData(self):
        """"
        This method will open a .txt file, containing all the edges 
        of the graph, when the button "View the edges data" is clicked
        """
        import os, sys, subprocess

        if sys.platform == "win32":
            os.startfile("data\\edges.txt")
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "data/edges.txt"])

    def open_broken_linkData(self):
        """"
        This method will open a .txt file, containing all the edges 
        of the graph, when the button "View the edges data" is clicked
        """
        import os, sys, subprocess

        if sys.platform == "win32":
            os.startfile("data\\broken-links.txt")
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "data/broken-links.txt"])
    
    def disableBtn(self):
        self.show_btn['state'] = tk.DISABLED
        self.nodeData_btn['state'] = tk.DISABLED
        self.edgeData_btn['state'] = tk.DISABLED
        self.brokenLink_btn['state'] = tk.DISABLED
    
    def inputStateChanged(self, event):
        value=self.input_entry.get()
        self.prev_input_val = value
        self.disableBtn()
    
    def iterationsStateChanged(self, event):
        value=self.input_entry.get()
        self.prev_iterations_val = value
        self.disableBtn()

    def create_widgets(self):
        """
        This method creates all the widgets for the interface
        """
        #variables
        self.nodeVar = tk.StringVar()
        self.edgeVar = tk.StringVar()
        self.blVar = tk.BooleanVar()
        self.curr_input_val = tk.StringVar()
        self.curr_iterations_val = tk.StringVar()

        #settings frame
        self.settings_frame = tk.LabelFrame(root, text="Settings", bg='#0A7599')

        #creating the buttons
        self.input_btn = tk.Button(root, text="Input", padx=5, pady=2, font=("Consolas", 14), border=0, command=self.create_graph)
        self.show_btn = tk.Button(root, text="View the graph", padx=5, pady=2, state=tk.DISABLED,  font=("Consolas", 14), border=0, command=self.show_graph)
        self.nodeData_btn = tk.Button(root, text="View the nodes data", padx=5, pady=2, state=tk.DISABLED, font=("Consolas", 14), border=0, command=self.open_nodeData)
        self.edgeData_btn = tk.Button(root, text="View the edges data", padx=5, pady=2, state=tk.DISABLED, font=("Consolas", 14), border=0, command=self.open_edgeData)
        self.brokenLink_btn = tk.Button(root, text='View the broken-links data', padx=5, pady=2, state=tk.DISABLED, font=("Consolas", 14), border=0, command=self.open_broken_linkData)
        

        #creating the entrys
        self.input_entry = tk.Entry(root, textvariable=self.curr_input_val, font=("Consolas", 14))
        self.input_entry.bind("<KeyRelease>", self.inputStateChanged)   #this binds the entry to any key in the keyboard so that once the user modifies the buttons -> DISABLE
        self.nbrOfItr_entry = tk.Entry(self.settings_frame, text=1, font=("Consolas", 12), textvariable=self.curr_iterations_val, width=3)
        self.nbrOfItr_entry.bind("<KeyRelease>", self.iterationsStateChanged)   #this binds the entry to any key in the keyboard so that once the user modifies the buttons -> DISABLE
        
        #Creating th labels
        self.input_label = tk.Label(root, text="URL:", font=("Consolas", 14), bg='#0A7599')
        self.nbrOfItr_label = tk.Label(self.settings_frame, text="Number of pages to crawl:", font=("Consolas", 12), bg='#0A7599')

        #creating the chekboxes
        self.node_checkBox = tk.Checkbutton(self.settings_frame, text="Node color", variable=self.nodeVar, onvalue="On", offvalue="Off", font=("Consolas", 12 ), bg='#0A7599')
        self.edge_checkBox = tk.Checkbutton(self.settings_frame, text="Edge color", variable=self.edgeVar, onvalue="On", offvalue="Off", font=("Consolas", 12), bg='#0A7599')
        self.bl_checkBox = tk.Checkbutton(self.settings_frame, text="Broken-Link", variable=self.blVar, onvalue=True, offvalue=False, font=("Consolas", 12), bg='#0A7599', command=self.disableBtn)

    def display_widgets(self):
        """
        This method displays all the widgets on the interface
        """
        self.settings_frame.place(x=10, y=80, width=300, height=150)

        #buttons
        self.input_btn.place(x=580, y=30, height=30)
        self.show_btn.place(x=470, y=100, height=30)
        self.nodeData_btn.place(x=470, y=140, height=30)
        self.edgeData_btn.place(x=470, y=180, height=30)
        self.brokenLink_btn.place(x=470, y=220, height=30)
        

        #labels
        self.input_label.place(x=10, y=30)
        self.nbrOfItr_label.grid(column=0, row=0)#place(x=0, y=5)

        #entry
        self.input_entry.place(x=60, y=30, width=500)
        self.nbrOfItr_entry.grid(column=1, row=0)#place(x=235, y=8, width=40) #170, 5

        #chekbox
        self.node_checkBox.grid(column=0, row=1, sticky='W')#place(x=0, y=40)
        self.edge_checkBox.grid(column=0, row=2, sticky='W')#place(x=0, y=70)
        self.bl_checkBox.grid(column=0, row=3, sticky='W')#place(x=0, y=100)

if __name__ == '__main__': 
    if run:    
        root = tk.Tk()
        #set the window
        root.title('Link Structure Vizualizer')
        root.iconbitmap('images/icon.ico')
        root.geometry("760x260")
        root.configure(bg='#0A7599')

        # Gets the requested values of the height and widht.
        windowWidth = root.winfo_reqwidth()
        windowHeight = root.winfo_reqheight()
        
        # Gets both half the screen width/height and window width/height
        positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
        
        # Positions the window in the center of the screen.
        root.geometry("+{}+{}".format(positionRight, positionDown))

        #initialise the application
        app = Application(master=root)
        app.mainloop()
