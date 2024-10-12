import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def organize_files_by_extension(path, progress_var, progress_bar):
    """Organize files in the given directory by their extensions."""
    try:
        files = os.listdir(path)
        total_files = len(files)
        if not files:
            messagebox.showinfo("Empty Directory", f"The directory '{path}' is empty.")
            return
        
        progress_step = 100 / total_files  # Calculate progress step for each file

        for index, file in enumerate(files):
            full_file_path = os.path.join(path, file)

            # Skip if it's a directory
            if os.path.isdir(full_file_path):
                continue

            filename, extension = os.path.splitext(file)
            extension = extension[1:].lower()  # Remove dot and convert to lowercase

            # If no extension, create a 'No_Extension' folder
            if not extension:
                extension = "No_Extension"

            # Check if the folder for the extension exists, otherwise create it
            destination_dir = os.path.join(path, extension)
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            # Move the file into the appropriate folder
            shutil.move(full_file_path, os.path.join(destination_dir, file))

            # Update progress bar
            progress_var.set((index + 1) * progress_step)
            progress_bar.update()

        messagebox.showinfo("Success", "Files have been successfully organized.")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_directory(progress_var, progress_bar):
    """Open a file dialog to select the directory for file organization."""
    path = filedialog.askdirectory(title="Select Folder to Organize")
    if path:
        organize_files_by_extension(path, progress_var, progress_bar)

def create_ui():
    """Create the GUI for the file organizer."""
    root = tk.Tk()
    root.title("File Organizer by Extension")
    root.geometry("400x250")
    root.configure(bg="#f0f4f7")  # Light background color
    
    # Set window icon (optional)
    # root.iconbitmap('path_to_icon.ico')  # Uncomment if you have an icon
    
    # Main label
    label = tk.Label(root, text="Organize Files by Extension", font=("Arial", 16, "bold"), bg="#f0f4f7", fg="#333")
    label.pack(pady=20)

    # Progress bar label
    progress_label = tk.Label(root, text="Progress", font=("Arial", 12), bg="#f0f4f7", fg="#333")
    progress_label.pack()

    # Progress bar
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", variable=progress_var)
    progress_bar.pack(pady=10)

    # Button to select folder and start organizing
    button = tk.Button(root, text="Select Folder and Organize", font=("Arial", 12), bg="#4CAF50", fg="white", 
                       activebackground="#45a049", padx=10, pady=5, command=lambda: select_directory(progress_var, progress_bar))
    button.pack(pady=20)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_ui()
