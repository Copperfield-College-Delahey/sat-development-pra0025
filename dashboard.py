class Dashboard(Tk):
    def __init__(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # sidebar frame
        self.sidebar_frame = Frame(self, bg="#108cff", width=200, height=500)
        self.