# Contact-Contact-Tracing-App 
The Health Declaration Form (HDF) program is a simple Tkinter-based application designed to collect personal information and health-related data from users. The program presents a graphical user interface (GUI) that allows users to fill in their details and answer a series of health-related questions. The collected data is then displayed in a table format for easy reference and can be used for contact tracing and necessary health protocols as required by health authorities.

# Requirements
To run the HDF program, you need to have Python installed on your system. The program utilizes the following libraries, so you should make sure they are installed before running the application:

tkinter: The standard GUI library for Python.

ttkbootstrap: A theme-aware set of widgets and styles for tkinter.

ttkbootstrap.toast: A component for displaying toast notifications.

ttkbootstrap.validation: A component for adding regex validation to form entries.

ttkbootstrap.tableview: A component for displaying data in a table format.

You can install the required libraries using pip with the following command:

pip install ttkbootstrap

# How to Use
Run the HDF program by executing the script. The program window titled "COVID CONTACT TRACKER" will appear.
Fill in your personal information in the "Personal Information" section, including your name, date, age, gender, address, phone number, and email address.
Provide details about a contact person in the "Contact Person Details" section, including their name, contact number, email address, and relationship to you.
Answer the questionnaires in the "Questionnaires" section:

"1. Are you vaccinated for COVID-19?" Choose one of the options that represent your vaccination status.

"2. Have you been exposed to a confirmed case in the last 14 days?" Choose one of the options that represent your exposure status.

"3. Do you have any symptoms in the past 7 days?" Choose one of the options that represent your symptoms.

"4. Have you been in contact with a person that has COVID-19 symptoms?" Choose one of the options that represent your contact status.

"5. Have you been tested for COVID-19 in the last 14 days?" Choose one of the options that represent your COVID-19 test status.

Once you have filled in all the necessary information, click the "Submit" button. The data you entered will be printed to the console, and a toast notification will confirm that your submission was successful.

If you decide not to proceed or want to exit the program, click the "Cancel" button.

