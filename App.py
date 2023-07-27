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

    # Function to create form entry with label and entry field
    def create_form_entry(self, frame, label, variable):
        form_field_container = ttk.Frame(frame)
        form_field_container.pack(fill=tk.X, expand=True, pady=5)

        form_field_label = ttk.Label(master=form_field_container, text=label, width=25)
        form_field_label.pack(side=tk.LEFT, padx=5)

        form_input = ttk.Entry(master=form_field_container, textvariable=variable)
        form_input.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        add_regex_validation(form_input, r'^[a-zA-Z0-9_]*$')

        return form_input
    
    # Function to create radiobuttons for vaccination status and exposure status
    def create_radiobuttons(self, frame):
        vaccine_container = ttk.Frame(frame)
        vaccine_container.pack(fill=tk.X, expand=True, pady=5)

        vaccine_label = ttk.Label(master=vaccine_container, text="1. Are you vaccinated for COVID-19?", width=50)
        vaccine_label.pack(side=tk.LEFT, padx=5)

        vaccination_options = ["Not Yet", "1st Dose", "2nd Dose", "1st Booster", "2nd Booster"]
        for option in vaccination_options:
            ttk.Radiobutton(vaccine_container, text=option, variable=self.vaccination_status, value=option).pack(side=tk.LEFT)

        exposure_container = ttk.Frame(frame)
        exposure_container.pack(fill=tk.X, expand=True, pady=5)

        exposure_label = ttk.Label(master=exposure_container, text="2. Have you been exposed to a confirmed case in the last 14 days?", width=70)
        exposure_label.pack(side=tk.LEFT, padx=5)

        exposure_options = ["Yes", "No", "Not Sure"]
        for option in exposure_options:
            ttk.Radiobutton(exposure_container, text=option, variable=self.exposure_status, value=option).pack(side=tk.LEFT)

    # Function to create combobox for symptoms selection
    def create_symptoms_combobox(self, frame):
        symptoms_container = ttk.Frame(frame)
        symptoms_container.pack(fill=tk.X, expand=True, pady=5)

        symptoms_label = ttk.Label(master=symptoms_container, text="3. Do you have any symptoms in the past 7 days?", width=60)
        symptoms_label.pack(side=tk.LEFT, padx=5)

        symptoms_options = ["Fever", "Headache", "Colds", "Muscle Pain", "Sore Throat", "Cough", "Diarrhea",
                            "Difficulty of Breathing", "Loss of Taste", "None of the above"]
        symptoms_combobox = ttk.Combobox(symptoms_container, textvariable=self.symptoms, values=symptoms_options)
        symptoms_combobox.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

    # Function to add radiobuttons for contact status
    def create_contact_radiobutton(self, frame):  
        contact_container = ttk.Frame(frame)
        contact_container.pack(fill=tk.X, expand=True, pady=5)

        contact_label = ttk.Label(master=contact_container, text="4. Have you been in contact with a person that has COVID-19 symptoms?", width=70)
        contact_label.pack(side=tk.LEFT, padx=5)

        contact_options = ["Yes", "No"]
        for option in contact_options:
            ttk.Radiobutton(contact_container, text=option, variable=self.contact_status, value=option).pack(side=tk.LEFT)

    # Function to create the button box with Submit and Cancel buttons
    def create_buttonbox(self, frame):
        button_container = ttk.Frame(frame)
        button_container.pack(fill=tk.X, expand=True, pady=(30, 20))
        
        # Set the font size for the buttons
        button_style = ttk.Style()
        button_style.configure('custom.TButton', font=('Arial', 18))  

    # Create cancel button
        cancel_btn = ttk.Button(master=button_container, text="Cancel", command=self.on_cancel, style='danger.custom.TButton', width=12)
        cancel_btn.pack(side=tk.RIGHT, padx=20)

        # Create submit button
        submit_btn = ttk.Button(master=button_container, text="Submit", command=self.on_submit, style='success.custom.TButton', width=12)
        submit_btn.pack(side=tk.RIGHT, padx=5)

    # Function to create the table
    def create_table(self):
        coldata = [{"text": "Name"}, {"text": "Date"}, {"text": "Age"}, {"text": "Gender"},
                   {"text": "Address"}, {"text": "Phone Number"},
                   {"text": "Email Address"}, {"text": "Vaccination Status"}, {"text": "Symptoms"},
                   {"text": "Exposure Status"}, {"text": "Contact with COVID-19 Symptoms"}, {"text": "COVID-19 Test Status"}]
        table = Tableview(master=self, coldata=coldata, rowdata=self.data, paginated=True, searchable=True,
                          bootstyle='primary', stripecolor=(self.colors.light, None))
        table.pack(fill=tk.BOTH, expand=tk.YES, padx=10, pady=0)
        return table

    # Event handler for submit button
    def on_submit(self):
        name = self.name.get()
        date = self.date.get()
        age = self.age.get()
        gender = self.gender.get()
        address = self.address.get()
        phone_number = self.phone_number.get()
        email_address = self.email_address.get()
  	    # Get the contact status value
        vaccination_status = self.vaccination_status.get()
	    # Get the contact status value
        symptoms = self.symptoms.get()
	    # Get the exposure status value
        exposure_status = self.exposure_status.get()
        # Get the contact status value
        contact_status = self.contact_status.get()  
        # Get the COVID-19 test status value
        covid_test_status = self.covid_test_status.get()  

        print("Name:", name)
        print("Date:", date)
        print("Age:", age)
        print("Gender:", gender)
        print("Address:", address)
        print("Phone Number:", phone_number)
        print("Email Address:", email_address)
        print("Vaccination Status:", vaccination_status)
        print("Symptoms:", symptoms)
        print("Exposure Status:", exposure_status)
        print("Contact with COVID-19 Symptoms:", contact_status)
        print("COVID-19 Test Status:", covid_test_status)

        contact_name = self.contact_name.get()
        contact_number = self.contact_number.get()
        contact_email = self.contact_email.get()
        relationship = self.relationship.get()

        print("Name:", contact_name)
        print("Contact Number:", contact_number)
        print("Email Address:", contact_email)
        print("Relationship to the contact person:", relationship)
   
        toast = ToastNotification(title="Submission successful!", message="Your data has been successfully submitted.", duration=3000)
        toast.show_toast()

        self.data.append((name, date, age, gender, address, phone_number, email_address, vaccination_status, symptoms, exposure_status, contact_status, covid_test_status))
        self.table.destroy()
        self.table = self.create_table()
