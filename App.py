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

# Initialize instance variables
        self.pack(fill=tk.BOTH, expand=tk.YES)
        self.name = ttk.StringVar(value="")
        self.date = ttk.StringVar(value="")
        self.age = ttk.StringVar(value="")
        self.gender = ttk.StringVar(value="")
        self.address = ttk.StringVar(value="")
        self.phone_number = ttk.StringVar(value="")
        self.email_address = ttk.StringVar(value="")
        self.vaccination_status = ttk.StringVar(value="")
        self.symptoms = ttk.StringVar(value="")
        self.exposure_status = ttk.StringVar(value="")
        self.contact_status = ttk.StringVar(value="")
        self.covid_test_status = ttk.StringVar(value="")

        self.contact_name = ttk.StringVar(value="")
        self.contact_number = ttk.StringVar(value="")
        self.contact_email = ttk.StringVar(value="")
        self.relationship = ttk.StringVar(value="")

        self.data = []
        self.colors = ttk.Style(theme='solar').colors

        # Create a Canvas to enable scrolling
        canvas = tk.Canvas(self, highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=tk.YES)

        # Attach a scrollbar to the canvas
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to work with the scrollbar
        canvas.config(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        
        # Create a frame inside the canvas to hold all the content
        content_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

