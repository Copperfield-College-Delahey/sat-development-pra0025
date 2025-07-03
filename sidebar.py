
import customtkinter as ctk


class Dashboard(ctk.CTk):
    def __init__(self): # runs the parent class setup so the window works correctly.
        super().__init__()

        self.grid_columnconfigure(0,weight=0)
        self.grid_rowconfigure((0,1),weight=1)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(side='left',fill='y')

        self.button = ctk.CTkButton(self.frame,text='☰',width=50,font=("roboto",25),hover_color='#242424',fg_color='#2B2B2B',command=self.expand_side_bar)
        self.button.grid()


        

    def expand_side_bar(self):
        size = self.button.cget("width") # Retrieves the current width of the sidebar toggle button to check if the sidebar is expanded or collapsed
        

        if size == 70:
            self.button.configure(width=250)
        else:self.button.configure(width=70)

app = Dashboard()
app.mainloop()