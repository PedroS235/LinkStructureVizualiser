import graph
import webScrapper
import tkinter as tk


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

    def create_graph(self):
        """
        This method creates the graph when the button input is clicked
        """
        self.ws = webScrapper.WebScrapper()
        self.G = graph.Graph()
        url = self.input_entry.get()
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
            tk.messagebox.showerror("Invalid URL", "Please make sure that the URL is valid!")
        print("yes")
    def show_graph(self):
        """
        This method will display the graph when the button "show graph" is clicked
        """
        if self.prev_nbr_of_itr != self.nbrOfItr_entry.get():
            self.create_graph()
        self.G.drawGraph(self.nodes, self.edges, self.nodeVar.get(), self.edgeVar.get())
        self.G.showGraph()

    def open_nodeData(self):
        """
        This method will open a .txt file, containing all the nodes 
        of the graph, when the button "View the nodes data" is clicked
        """
        from os import startfile
        startfile("nodes.txt")

    def open_edgeData(self):
        """"
        This method will open a .txt file, containing all the edges 
        of the graph, when the button "View the edges data" is clicked
        """
        from os import startfile
        startfile("edges.txt")

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
        self.input_btn = tk.Button(root, text="Input", padx=5, pady=2, font=("Consolas", 14), border=0, bg='#04A2D6', activebackground='#02EAFD', fg='#ffffff', activeforeground='#ffffff', command=self.create_graph)
        self.show_btn = tk.Button(root, text="View the graph", padx=5, pady=2, state=tk.DISABLED,  font=("Consolas", 14), border=0, bg='#04A2D6', activebackground='#02EAFD', fg='#ffffff', activeforeground='#ffffff', command=self.show_graph)
        self.nodeData_btn = tk.Button(root, text="View the nodes data", padx=5, pady=2, state=tk.DISABLED, font=("Consolas", 14), border=0, bg='#04A2D6', activebackground='#02EAFD', fg='#ffffff', activeforeground='#ffffff', command=self.open_nodeData)
        self.edgeData_btn = tk.Button(root, text="View the edges data", padx=5, pady=2, state=tk.DISABLED, font=("Consolas", 14), border=0, bg='#04A2D6', activebackground='#02EAFD', fg='#ffffff', activeforeground='#ffffff', command=self.open_edgeData)
        self.instructions_btn = tk.Button(root, text="Instructions", padx=5, pady=2, font=("Consolas", 14), border=0, bg='#04A2D6', activebackground='#02EAFD', fg='#ffffff', activeforeground='#ffffff')
        
        #creating the entrys
        self.input_entry = tk.Entry(root, font=("Consolas", 14))
        self.nbrOfItr_entry = tk.Entry(self.settings_frame, text=1, font=("Consolas", 12))
        
        #Creating th labels
        self.input_label = tk.Label(root, text="URL:", font=("Consolas", 14), bg='#0A7599')
        self.nbrOfItr_label = tk.Label(self.settings_frame, text="Number of iterations:", font=("Consolas", 12), bg='#0A7599')

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
        self.nbrOfItr_entry.place(x=200, y=5, width=40)

        #chekbox
        self.node_checkBox.place(x=0, y=40)
        self.edge_checkBox.place(x=0, y=70)
        self.bl_checkBox.place(x=0, y=100)

root = tk.Tk()
root.title('Link Structure Vizualizer')
root.iconbitmap('images/icon.ico')
root.geometry("700x250")
root.configure(bg='#0A7599')
app = Application(master=root)
app.mainloop()
