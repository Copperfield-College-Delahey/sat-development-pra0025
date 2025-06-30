import customtkinter as ctk
from customtkinter import *

root = ctk.CTk()

# Appearance
ctk.set_appearance_mode("Light") # Sets to light mode
ctk.set_default_color_theme("blue") 

# App setup
app = ctk.CTk()
app.title("Smart Sort")
app.geometry("1000x600")



# Layout 
app.grid_columnconfigure(0, weight=1) # Left Column
app.grid_columnconfigure(1, weight=4) # Right Column
app.grid_rowconfigure(0, weight=1)

# Sidebar
sidebar = ctk.CTkFrame(app, border_width=3)
sidebar.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5) # puts sidebar on the left side



# Main dashboard area




def start():
    pass
    
# Start Button
start_button = ctk.CTkButton(root, text="Start Organisation", command=start)
start_button.pack(pady=80)




app.mainloop()
