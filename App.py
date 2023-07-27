# Import required libraries
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.validation import add_regex_validation
from ttkbootstrap.tableview import Tableview

# Define a class HDF
class HDF(ttk.Frame):
    # Constructor method for the class
    def __init__(self, master_window):
        # Initialize the parent class constructor
        super().__init__(master_window, padding=(10, 10, 10, 10))

        # Create a label for the heading
        heading_label = ttk.Label(self, text="Health Declaration Form", font= ('Cascadia Code', 24))
        heading_label.pack(fill=tk.X, pady=10, padx= 25)
