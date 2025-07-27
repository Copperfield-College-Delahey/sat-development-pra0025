import customtkinter as ctk
from customtkinter import *



# Appearance
ctk.set_appearance_mode("Light") # Sets to light mode
ctk.set_default_color_theme("blue") # sets the theme to blue


# File extension mappings
file_types = {
    # All image file extensions go into the "Images" folder
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    # All documents file extensions go into the "Documents" folder
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    # All audio file extensions go into the "Audio" folder
    "Audio": [".mp3", ".wav", ".aac"],
    # All video file extensions go into the "Videos" folder
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    # All archives file extensions go into the "Archives" folder
    "Archives": [".zip", ".rar", ".7z"],
    # All programs file extensions go into the "Program" folder
    "Programs": [".exe", ".msi", ".bat"],
    # All scripts file extensions go into the "Scripts" folder
    "Scripts": [".py", ".js", ".html", ".css"],
    "Others": []
}

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

        self.button = ctk.CTkButton(self.frame,text='☰',row=0,column=0,width=50,font=("roboto",25),hover_color='#242424',fg_color='#2B2B2B',command=self.expand_side_bar)
        self.button.grid()


        

    def expand_side_bar(self):
        size = self.button.cget("width") # Retrieves the current width of the sidebar toggle button to check if the sidebar is expanded or collapsed
        
        
    def run_organiser(self):
        pass
    
    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.path_entry.delete(0, "end")
            self.path_entry.insert(0, folder_path)
            






# Main dashboard area
main = ctk.CTkFrame(app, border_width=3)
main.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=5, pady=5) # main dashboard placed on he right and bigger than the sidebar

# Configure main's grid to push content to the bottom
main.grid_rowconfigure(0, weight=1)  # Top space expands
main.grid_rowconfigure(1, weight=0)  # Button row

def start():
    folder = selected_folder.get() # saves the selected folder path into variable called folder
    if folder == "No folder selected" or not os.path.exists(folder): # Checks if no folder was picked or if the folder path doesn't exist
        return
    
# Start Button
start_button = ctk.CTkButton(app, text="Start Organisation", command=start) # button for starting the system
start_button.grid(row=1, column=1, sticky="s", pady=10, padx=10)



# Running the app
if __name__ == "__main__":
    app.mainloop()
