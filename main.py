import customtkinter as ctk
from customtkinter import *
import os # to interact with folders and files
import shutil # To move files to specific folder


# Appearance
ctk.set_appearance_mode("Light") # Sets to light mode
ctk.set_default_color_theme("blue") # sets the theme to blue


# Defining file categories
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi", ".bat"],
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
app.grid_columnconfigure(2, weight=4)
app.grid_columnconfigure(3, weight=4)

app.grid_rowconfigure(0, weight=1)



# Box for tracking variables
def create_stat_box(parent, title, variable):
    box = ctk.CTkFrame(parent, width=200, height=100, corner_radius=10)
    box.pack(side="left", padx=15)
    ctk.CTkLabel(box, textvariable=variable, font=("Arial", 20)).pack(pady=5)
    ctk.CTkLabel(box, text=title).pack()
    return box

create_stat_box(app, "Total Files Organised", total_organised)
create_stat_box(app, "New Files", new_files)
create_stat_box(app, "Storage Space", storage_space)


# Tracking Variables
selected_folder = StringVar(value="No folder selected")
total_organised = StringVar(value="0")
new_files = StringVar(value="0")
storage_space = StringVar(value="0 GB")
file_type_display = StringVar(value="")
last_run = StringVar(value="Never")


# Sidebar
sidebar = ctk.CTkFrame(app)
sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=5, pady=5)
ctk.CTkLabel(sidebar, text="Smart Sort", font=("Arial", 20)).pack(pady=20)
for btn in ["Dashboard", "Organised Files", "Unsorted Files", "Settings", "Help"]:
    ctk.CTkButton(sidebar, text=btn).pack(pady=5, padx=10, fill="x")

# Dashboard Menu
class Dashboard(ctk.CTk):
    def __init__(self): # runs the parent class setup so the window works correctly.
        super().__init__()

        self.grid_columnconfigure(0,weight=0)
        self.grid_rowconfigure((0,0),weight=1)

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(side='left',fill='y')




        


    # Gives the total free storage on desktop
    def get_storage_summary():
        total, used, free = shutil.disk_usage(os.path.expanduser("~"))
        total_gb = round(total / (1024**3), 2)
        free_gb = round(free / (1024**3), 2)
        return f"{free_gb} GB Free / {total_gb} GB Total"
        
        

    
    def organise_files():
        # --Reading Files--
        folder = filedialog.askdirectory() # allows user to pick which file to organise
        print(folder)
        folderlist = os.listdir(folder)
        print(folderlist)
        
        def organise_files():
            folder = selected_folder.get()
            if folder == "No folder selected" or not os.path.exists(folder):
                    return
 
            moved_count = 0 # Counts how many files were moved
            file_types_found = set()  # Keeps track of which file type folders were used

            for filename in os.listdir(folder): # Go through each item in the selected folder
                filepath = os.path.join(folder, filename)
                if os.path.isfile(filepath): # Only continue if the item is a file
                    ext = os.path.splitext(filename)[1].lower()

                    for folder_name, extensions in file_types.items():
                        if ext in extensions:
                            dest_folder = os.path.join(folder, folder_name)
                            os.makedirs(dest_folder, exist_ok=True)
                            shutil.move(filepath, os.path.join(dest_folder, filename))
                            moved_count += 1 # increases the moved count
                            file_types_found.add(folder_name) # Records that a folder type was used
                            break
                        
                        
        # Prompt indicating process is complete
        messagebox.showinfo("Success", "Files have been organised!")
    
        


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
        

    # Choose file to organise and start button
    choose_button = ctk.CTkButton(app, text="Start Organisation", command=organise_files) 
    choose_button.grid(row=1, column=2, sticky="s", pady=10, padx=10)


    # Updating display



# Running the app
if __name__ == "__main__":
    app.mainloop()
