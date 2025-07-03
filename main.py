import customtkinter as ctk
from customtkinter import *



# Appearance
ctk.set_appearance_mode("Light") # Sets to light mode
ctk.set_default_color_theme("blue") # sets the theme to blue

# App setup
app = ctk.CTk()
app.title("Smart Sort") # app title
app.geometry("1000x600") # dimensions of window



# Layout 
app.grid_columnconfigure(0, weight=2) # Left Column
app.grid_columnconfigure(1, weight=4) # Right Column
app.grid_rowconfigure(0, weight=1)

# Sidebar
sidebar = ctk.CTkFrame(app, border_width=3)
sidebar.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=5, pady=5) # puts sidebar on the left side


# Dashboard Menu
class Dashboard(ctk.CTk):
    def __init__(self): # runs the parent class setup so the window works correctly.
        super().__init__()

        self.grid_columnconfigure(0,weight=0)
        self.grid_rowconfigure((0,0),weight=1)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(side='left',fill='y')

        self.button = ctk.CTkButton(self.frame,text='☰',width=50,font=("roboto",25),hover_color='#242424',fg_color='#2B2B2B',command=self.expand_side_bar)
        self.button.grid()


        

    def expand_side_bar(self):
        size = self.button.cget("width") # Retrieves the current width of the sidebar toggle button to check if the sidebar is expanded or collapsed
        

        if size == 70:
            self.button.configure(width=250)
        else:self.button.configure(width=70)






# Main dashboard area
main = ctk.CTkFrame(app, border_width=3)
main.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=5, pady=5) # main dashboard placed on he right and bigger than the sidebar

# Configure main's grid to push content to the bottom
main.grid_rowconfigure(0, weight=1)  # Top space expands
main.grid_rowconfigure(1, weight=0)  # Button row

def start():
    pass
    
# Start Button
start_button = ctk.CTkButton(app, text="Start Organisation", command=start) # button for starting the system
start_button.grid(row=1, column=1, sticky="s", pady=10, padx=10)




app.mainloop()
