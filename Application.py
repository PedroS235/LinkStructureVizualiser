import Graph
import WebScrapper
import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        """
        This is the constructor of this application
        and it sets the default values
        """
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.display_widgets()
        self.node_checkBox.select()
        self.edge_checkBox.deselect()
        self.bl_checkBox.deselect()
        self.nbrOfItr_entry.insert(0, 1)
        self.input_entry.insert(0, "https://infallible-varahamihira-e94f86.netlify.app/")

    def create_graph(self):
        """
        This method creates the graph when the button input is clicked
        """
        self.ws = WebScrapper.WebScrapper()
        self.G = Graph.Graph()
        url = self.input_entry.get().replace(" ", "")
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
            self.prev_nbr_of_itr = self.nbrOfItr_entry.get()
        else:
            messagebox.showerror("Invalid URL", "Please make sure that the URL is valid!")

    def show_graph(self):
        """
        This method will display the graph when the button "show graph" is clicked
        """
        url = self.input_entry.get()
        #checks if the input URL is valid 
        if self.ws.is_valid(url):
            if self.prev_nbr_of_itr != self.nbrOfItr_entry.get():
                self.create_graph()
            self.G.drawGraph(self.nodes, self.edges, self.nodeVar.get(), self.edgeVar.get())
            self.G.showGraph()
        else:
            messagebox.showerror("Invalid URL", "Please make sure that the URL is valid!")

    def open_nodeData(self):
        """
        This method will open a .txt file, containing all the nodes 
        of the graph, when the button "View the nodes data" is clicked
        """
        import os, sys, subprocess

        if sys.platform == "win32":
            os.startfile("nodes.txt")
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "nodes.txt"])

    def open_edgeData(self):
        """"
        This method will open a .txt file, containing all the edges 
        of the graph, when the button "View the edges data" is clicked
        """
        import os, sys, subprocess

        if sys.platform == "win32":
            os.startfile("edges.txt")
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "edges.txt"])

    def disableBtn(self):
        self.show_btn['state'] = tk.DISABLED
        self.nodeData_btn['state'] = tk.DISABLED
        self.edgeData_btn['state'] = tk.DISABLED

    def create_widgets(self):
        """
        This method creates all the widgets for the interface
        """
        #variables
        self.nodeVar = tk.StringVar()
        self.edgeVar = tk.StringVar()
        self.blVar = tk.BooleanVar()

        #settings frame
        self.settings_frame = tk.LabelFrame(root, text="Settings", bg='#0A7599')

        #creating the buttons
        #, bg='#04A2D6', activebackground='#02EAFD', fg='#ffffff', activeforeground='#ffffff',
        self.input_btn = tk.Button(root, text="Input", padx=5, pady=2, font=("Consolas", 14), border=0, command=self.create_graph)
        self.show_btn = tk.Button(root, text="View the graph", padx=5, pady=2, state=tk.DISABLED,  font=("Consolas", 14), border=0, command=self.show_graph)
        self.nodeData_btn = tk.Button(root, text="View the nodes data", padx=5, pady=2, state=tk.DISABLED, font=("Consolas", 14), border=0, command=self.open_nodeData)
        self.edgeData_btn = tk.Button(root, text="View the edges data", padx=5, pady=2, state=tk.DISABLED, font=("Consolas", 14), border=0, command=self.open_edgeData)
        self.instructions_btn = tk.Button(root, text="Instructions", padx=5, pady=2, font=("Consolas", 14), border=0)
        
        #creating the entrys
        self.input_entry = tk.Entry(root, font=("Consolas", 14))
        self.nbrOfItr_entry = tk.Entry(self.settings_frame, text=1, font=("Consolas", 12))
        
        #Creating th labels
        self.input_label = tk.Label(root, text="URL:", font=("Consolas", 14), bg='#0A7599')
        self.nbrOfItr_label = tk.Label(self.settings_frame, text="Number of pages to crawl:", font=("Consolas", 12), bg='#0A7599')

        #creating the chekboxes
        self.node_checkBox = tk.Checkbutton(self.settings_frame, text="Node color", variable=self.nodeVar, onvalue="On", offvalue="Off", font=("Consolas", 12 ), bg='#0A7599', command=self.disableBtn)
        self.edge_checkBox = tk.Checkbutton(self.settings_frame, text="Edge color", variable=self.edgeVar, onvalue="On", offvalue="Off", font=("Consolas", 12), bg='#0A7599', command=self.disableBtn)
        self.bl_checkBox = tk.Checkbutton(self.settings_frame, text="Broken-Link", variable=self.blVar, onvalue=True, offvalue=False, font=("Consolas", 12), bg='#0A7599', command=self.disableBtn)

    def display_widgets(self):
        """
        This method displays all the widgets on the interface
        """
        self.settings_frame.place(x=10, y=80, width=300, height=150)

        #buttons
        self.input_btn.place(x=470, y=30, height=30)
        self.show_btn.place(x=470, y=100, height=30)
        self.nodeData_btn.place(x=470, y=140, height=30)
        self.edgeData_btn.place(x=470, y=180, height=30)
        #self.instructions_btnplace(x=10, y=50)

        #labels
        self.input_label.place(x=10, y=30)
        self.nbrOfItr_label.place(x=0, y=5)

        #entry
        self.input_entry.place(x=60, y=30, width=400)
        self.nbrOfItr_entry.place(x=170, y=5, width=40)

        #chekbox
        self.node_checkBox.place(x=0, y=40)
        self.edge_checkBox.place(x=0, y=70)
        self.bl_checkBox.place(x=0, y=100)
    

root = tk.Tk()
#set the window
root.title('Link Structure Vizualizer')
root.iconbitmap('images/icon.ico')
root.geometry("700x250")
root.configure(bg='#0A7599')

# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

#initialise the application
app = Application(master=root)
app.mainloop()
