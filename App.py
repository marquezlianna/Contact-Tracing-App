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

        # Personal Information Section
        personal_info_frame = ttk.LabelFrame(content_frame, text="Personal Information")
        personal_info_frame.pack(fill=tk.X, padx=10, pady=5)

        instruction_text = "Please enter your Personal Information:"
        instruction = ttk.Label(personal_info_frame, text=instruction_text)
        instruction.pack(fill=tk.X, pady=10)

        self.create_form_entry(personal_info_frame, "Name:", self.name)
        self.create_form_entry(personal_info_frame, "Date:", self.date)
        self.create_form_entry(personal_info_frame, "Age:", self.age)
        self.create_form_entry(personal_info_frame, "Gender:", self.gender)
        self.create_form_entry(personal_info_frame, "Address:", self.address)
        self.create_form_entry(personal_info_frame, "Phone Number:", self.phone_number)
        self.create_form_entry(personal_info_frame, "Email Address:", self.email_address)

        # Contact Person Details Section
        contact_info_frame = ttk.LabelFrame(content_frame, text="Contact Person Details")
        contact_info_frame.pack(fill=tk.X, padx=10, pady=5)

        instruction_text = "Please enter the Contact Person Details:"
        instruction = ttk.Label(contact_info_frame, text=instruction_text)
        instruction.pack(fill=tk.X, pady=10)

        self.create_form_entry(contact_info_frame, "Name:", self.contact_name)
        self.create_form_entry(contact_info_frame, "Contact Number:", self.contact_number)
        self.create_form_entry(contact_info_frame, "Email Address:", self.contact_email)
        self.create_form_entry(contact_info_frame, "Relationship to the contact person:", self.relationship)

        # Questionnaires Section
        questionnaires_frame = ttk.LabelFrame(content_frame, text="Questionnaires")
        questionnaires_frame.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=5)

        self.create_radiobuttons(questionnaires_frame)
        self.create_symptoms_combobox(questionnaires_frame)
        self.create_contact_radiobutton(questionnaires_frame)
        self.create_covid_test_radiobutton(questionnaires_frame)

        # Privacy Consent Section
        privacy_consent_frame = ttk.LabelFrame(content_frame, text="Privacy Consent", padding=10, borderwidth=1, relief="solid")
        privacy_consent_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        consent_message = ("Your privacy is of utmost importance to us. By submitting this COVID-19 form you acknowledge and agree that the provided data will be used for contact tracing and necessary health protocols as required by health authorities. Rest assured, your information will be handled in accordance with applicable data protection laws.")

        consent_label = ttk.Label(privacy_consent_frame, text=consent_message, wraplength=700, font=('Times New Roman', 12), justify=tk.LEFT)
        consent_label.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

        self.create_buttonbox(content_frame)

        self.table = self.create_table()
