class Dashboard(Tk):
    def __init__(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        super().__init__()
        self.title("Dashboard")
        self.geometry("1000x600")
        
        self.sidebar_expand = True
        
        # sidebar frame
        self.sidebar_frame = Frame(self, bg="#108cff", width=200, height=500)
        self.sidebar_frame.grid(row=0, column=0, sticky="ns")
        
        # Main content frame
        self.content_frame = Frame(self, bg="ecf0f1")
        self.content_frame.grid(row=0, column=1, sticky="nsew")
        
        # Side bar toggle to expand
        self.toggle_button = Button(self.sidebar_frame, text="☰", bg="#034787", fg="white",
                                    cursor="hand2", font=("Arial", 16), releif="flat") # the symbol "☰" was gathered for an copy and paste website
        self.toggle_button.pack(pady-10, padx=10, fill="x",)
        
    
    if __name__ == "__main__":