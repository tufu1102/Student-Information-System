from Table_Creation import create_table
from Button_Sql import *
import tkinter as tk
from tkinter import ttk, messagebox


def open_student_window():
    global root

    # Destroy the current widgets in the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Update the main window for student
    root.title("Student Window")

    # Welcome message
    student_welcome_label = tk.Label(root, text="Welcome, Student!", font=("Helvetica", 16))
    student_welcome_label.pack(pady=20)

    # ID Entry
    id_label = tk.Label(root, text="Enter your ID:")
    id_label.pack()

    global id_entry
    id_entry = tk.Entry(root, insertwidth = 4)
    id_entry.pack(pady=10)

    # Submit and Back buttons
    submit_button = tk.Button(root, text="Submit", command = submit_student)
    submit_button.pack(side=tk.LEFT, padx=10)

    back_button = tk.Button(root, text="Back", command=back_to_main)
    back_button.pack(side=tk.RIGHT, padx=10)

def open_teacher_window():
    global root

    # Destroy the current widgets in the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Update the main window for teacher
    root.title("Teacher Window")

    # Welcome message
    teacher_welcome_label = tk.Label(root, text="Welcome, Teacher!", font=("Helvetica", 16))
    teacher_welcome_label.pack(pady=20)

    # ID Entry
    id_label = tk.Label(root, text = "Enter your ID:")
    id_label.pack()

    global id_entry
    id_entry = tk.Entry(root, insertwidth = 4)
    id_entry.pack(pady=10)

    # Submit and Back buttons
    submit_button = tk.Button(root, text="Submit", command = submit_teacher)
    submit_button.pack(side=tk.LEFT, padx=10)

    back_button = tk.Button(root, text="Back", command=back_to_main)
    back_button.pack(side=tk.RIGHT, padx=10)

def submit_student():
    if check_id(id_entry):
        open_student_qualification_window()
    else:
        messagebox.showinfo("Error", "ID does not exist.")
        open_student_details_window()

def submit_teacher():
    global root, id_entry

    # Get the entered ID from the entry field
    entered_id = id_entry.get()

    # Check if the ID is correct
    if entered_id == "31225002":
        # ID is correct, open the qualification selection window
        open_teacher_requirement_window()
    else:
        messagebox.showerror("Error", "Incorrect ID. You may not be a teacher.")
        create_main_window()
        

def open_student_qualification_window():
    global root

    # Destroy the current widgets in the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Create a new window for qualification selection
    root.title("Qualification Selection")

    # Label for qualification selection
    qualification_label = tk.Label(root, text="Choose as per your qualification", font=("Helvetica", 16))
    qualification_label.pack(pady=20)

    # Buttons for Internship, Extra-Curricular, and Co-Curricular
    internship_button = tk.Button(root, text="Internship", command = open_internship_submit)
    internship_button.pack(pady=10)

    extracurricular_button = tk.Button(root, text="Extra-Curricular", command = open_extracurricular_submit)
    extracurricular_button.pack(pady=10)

    cocurricular_button = tk.Button(root, text="Co-Curricular", command = open_cocurricular_submit)
    cocurricular_button.pack(pady=10)

def open_student_details_window():
    global root, first_name_entry, last_name_entry, college_name_entry, student_id_entry, student_email_entry, phone_number_entry, department_var, year_var

    for widget in root.winfo_children():
        widget.destroy()

    root.title("Student Details")

    # Labels and Entry fields for student details
    first_name_label = tk.Label(root, text="First Name:")
    first_name_label.pack()

    first_name_entry = tk.Entry(root)
    first_name_entry.pack(pady=5)

    last_name_label = tk.Label(root, text="Last Name:")
    last_name_label.pack()

    last_name_entry = tk.Entry(root)
    last_name_entry.pack(pady=5)

    college_name_label = tk.Label(root, text="College Name:")
    college_name_label.pack()

    college_name_entry = tk.Entry(root)
    college_name_entry.pack(pady=5)

    student_id_label = tk.Label(root, text="Student ID:")
    student_id_label.pack()

    student_id_entry = tk.Entry(root)
    student_id_entry.pack(pady=5)

    student_email_label = tk.Label(root, text="Student Email:")
    student_email_label.pack()

    student_email_entry = tk.Entry(root)
    student_email_entry.pack(pady=5)

    phone_number_label = tk.Label(root, text="Phone Number:")
    phone_number_label.pack()

    phone_number_entry = tk.Entry(root)
    phone_number_entry.pack(pady=5)

    department_label = tk.Label(root, text="Department:")
    department_label.pack()

    # Dropdown for department
    department_options = ["CSE", "IT", "ECE", "EEE", "BME", "CHEM", "MECH"]
    department_var = tk.StringVar()
    department_dropdown = ttk.Combobox(root, textvariable=department_var, values=department_options)
    department_dropdown.pack(pady=5)

    year_label = tk.Label(root, text="Year of Study:")
    year_label.pack()

    # Dropdown for year of study
    year_options = [1, 2, 3, 4, "PG"]
    year_var = tk.StringVar()
    year_dropdown = ttk.Combobox(root, textvariable=year_var, values=year_options)
    year_dropdown.pack(pady=5)

    # Submit and Back buttons
    submit_button = tk.Button(root, text="Submit", command=submit_student_details)
    submit_button.pack(side=tk.LEFT, padx=10)

    back_button = tk.Button(root, text="Back", command = open_student_window)
    back_button.pack(side=tk.RIGHT, padx=10)

def submit_student_details():
    # Get values from entry fields
    id_value = student_id_entry.get()
    first_name_value = first_name_entry.get()
    last_name_value = last_name_entry.get()
    college_value = college_name_entry.get()
    email_value = student_email_entry.get()
    phone_number_value = phone_number_entry.get()
    department_value = department_var.get()
    year_of_study_value = year_var.get()

    # Call the function to insert student details
    insert_student_details(id_value, first_name_value, last_name_value, college_value,
                            email_value, phone_number_value, department_value, year_of_study_value)

    # Open the qualification window
    open_student_qualification_window()

def open_internship_submit():
    global root, id_entry, company_entry, type_var, role_entry, start_date_entry, end_date_entry, stipend_entry

    # Destroy the current widgets in the qualification window
    for widget in root.winfo_children():
        widget.destroy()

    # Create a new window for Internship details
    root.title("Internship Details")

    # Labels and Entry fields for Internship details
    company_label = tk.Label(root, text="Name of the Company:")
    company_label.pack()

    company_entry = tk.Entry(root)
    company_entry.pack(pady=5)

    type_label = tk.Label(root, text="Type of Internship:")
    type_label.pack()

    # Dropdown for type of internship
    internship_types = ["Physical", "Online", "Hybrid"]
    type_var = tk.StringVar()
    type_dropdown = ttk.Combobox(root, textvariable=type_var, values=internship_types)
    type_dropdown.pack(pady=5)

    id_label = tk.Label(root, text="ID:")
    id_label.pack()

    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)

    role_label = tk.Label(root, text="Role:")
    role_label.pack()

    role_entry = tk.Entry(root)
    role_entry.pack(pady=5)

    start_date_label = tk.Label(root, text="Start Date:")
    start_date_label.pack()

    start_date_entry = tk.Entry(root)
    start_date_entry.pack(pady=5)

    end_date_label = tk.Label(root, text="End Date:")
    end_date_label.pack()

    end_date_entry = tk.Entry(root)
    end_date_entry.pack(pady=5)

    stipend_label = tk.Label(root, text="Stipend Amount:")
    stipend_label.pack()

    stipend_entry = tk.Entry(root)
    stipend_entry.pack(pady=5)

    # Submit and Back buttons
    submit_button = tk.Button(root, text="Submit", command = submit_internship_details)
    submit_button.pack(side=tk.LEFT, padx=10)

    back_button = tk.Button(root, text="Back", command=open_student_qualification_window)
    back_button.pack(side=tk.RIGHT, padx=10)


def open_extracurricular_submit():
    global root, id_entry, type_var1, organizer_entry, date_entry, type_var2

    # Destroy the current widgets in the qualification window
    for widget in root.winfo_children():
        widget.destroy()

    # Create a new window for Extracurricular details
    root.title("Extracurricular Details")

    id_label = tk.Label(root, text="ID:")
    id_label.pack()

    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)

    # Labels and Entry fields for Extracurricular details
    activity_label = tk.Label(root, text="Activity:")
    activity_label.pack()

    activity_types = ['Sports','Music and Dance','Drama and Theatre','Student Council','Volunteering','Scouting and guiding','Robotics Club','Online course','Fundraising','Other']
    type_var1 = tk.StringVar()
    type_dropdown = ttk.Combobox(root, textvariable=type_var1, values=activity_types)
    type_dropdown.pack(pady=5)

    organizer_label = tk.Label(root, text="Organizer:")
    organizer_label.pack()

    organizer_entry = tk.Entry(root)
    organizer_entry.pack(pady=5)

    date_label = tk.Label(root, text="Date:")
    date_label.pack()

    date_entry = tk.Entry(root)
    date_entry.pack(pady=5)

    achv_label = tk.Label(root, text="Achievement:")
    achv_label.pack()

    achievement_types = ["1st","2nd","3rd","Participation"]
    type_var2 = tk.StringVar()
    type_dropdown = ttk.Combobox(root, textvariable=type_var2, values=achievement_types)
    type_dropdown.pack(pady=5)


    # Submit and Back buttons
    submit_button = tk.Button(root, text="Submit", command = submit_extracurricular_details)
    submit_button.pack(side=tk.LEFT, padx=10)

    back_button = tk.Button(root, text="Back", command=open_student_qualification_window)
    back_button.pack(side=tk.RIGHT, padx=10)

def open_cocurricular_submit():
    global root, id_entry, type_var1, organizer_entry, date_entry, type_var2


    # Destroy the current widgets in the qualification window
    for widget in root.winfo_children():
        widget.destroy()

    # Create a new window for Cocurricular details
    root.title("Cocurricular Details")

    id_label = tk.Label(root, text="ID:")
    id_label.pack()

    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)

    # Labels and Entry fields for Cocurricular details
    activity_label = tk.Label(root, text="Activity:")
    activity_label.pack()

    activity_types =['Debate','Quizes','Fairs','Olympiads','Exhibitions','workshops','Field Trips','Language Clubs']
    type_var1 = tk.StringVar()
    type_dropdown = ttk.Combobox(root, textvariable=type_var1, values=activity_types)
    type_dropdown.pack(pady=5)

    organizer_label = tk.Label(root, text="Organizer:")
    organizer_label.pack()

    organizer_entry = tk.Entry(root)
    organizer_entry.pack(pady=5)

    date_label = tk.Label(root, text="Date:")
    date_label.pack()

    date_entry = tk.Entry(root)
    date_entry.pack(pady=5)

    achv_label = tk.Label(root, text="Achievement")
    achv_label.pack()

    achievement_types = ["1st","2nd","3rd","Participation"]
    type_var2 = tk.StringVar()
    type_dropdown = ttk.Combobox(root, textvariable=type_var2, values=achievement_types)
    type_dropdown.pack(pady=5)


    # Submit and Back buttons
    submit_button = tk.Button(root, text="Submit", command = submit_cocurricular_details)
    submit_button.pack(side=tk.LEFT, padx=10)

    back_button = tk.Button(root, text="Back", command=open_student_qualification_window)
    back_button.pack(side=tk.RIGHT, padx=10)

def submit_internship_details():
    global root, company_entry, type_var, id_entry, role_entry, start_date_entry, end_date_entry, stipend_entry

    # Get the entered values
    company = company_entry.get()
    internship_type = type_var.get()
    student_id = id_entry.get()
    role = role_entry.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    stipend_amount = stipend_entry.get()
    stipend_amount = int(stipend_amount)

    # Check if all fields are filled
    if not company or not internship_type or not student_id or not role or not start_date or not end_date or not stipend_amount:
        messagebox.showerror("Error", "All fields must be filled.")
        return

    # Call the function from Button_Sql to insert internship details
    insert_internship_details(company, internship_type, student_id, role, start_date, end_date,stipend_amount)
    (company, internship_type, role, start_date, end_date, stipend_amount, student_id)
    # Optionally, you can add a message box to indicate successful submission
    messagebox.showinfo("Success", "Internship details submitted successfully.")

    # Go back to the student qualification window
    open_student_qualification_window()

def submit_extracurricular_details():

    # Get values from entry fields and dropdowns
    id_value = id_entry.get()
    activity_value = type_var1.get()
    organizer_value = organizer_entry.get()
    date_value = date_entry.get()
    achievement_value = type_var2.get()

    # Check if all required fields are filled
    if not id_value or not activity_value or not organizer_value or not date_value or not achievement_value:
        messagebox.showerror("Error", "All fields must be filled.")
        return

    # Create a tuple of details
    details = (activity_value, date_value, organizer_value, achievement_value, id_value )

    # Insert extracurricular details
    if insert_extracurricular_details(details):
        messagebox.showinfo("Success", "Extracurricular details submitted successfully.")
    else:
        messagebox.showerror("Error", "Failed to submit extracurricular details.")

def submit_cocurricular_details():
    # Get values from entry fields and dropdowns
    id_value = id_entry.get()
    activity_value = type_var1.get()
    organizer_value = organizer_entry.get()
    date_value = date_entry.get()
    achievement_value = type_var2.get()

    # Check if all required fields are filled
    if not id_value or not activity_value or not organizer_value or not date_value or not achievement_value:
        messagebox.showerror("Error", "All fields must be filled.")
        return

    # Create a tuple of details
    details = (activity_value, date_value, organizer_value, achievement_value, id_value )


    # Insert cocurricular details
    if insert_cocurricular_details(details):
        messagebox.showinfo("Success", "Cocurricular details submitted successfully.")
    else:
        messagebox.showerror("Error", "Failed to submit cocurricular details.")

def open_teacher_requirement_window():
    global root

    # Destroy the current widgets in the main window
    for widget in root.winfo_children():
        widget.destroy()

    # Create a new window for qualification selection
    root.title("Requirement Selection")

    # Label for qualification selection
    qualification_label = tk.Label(root, text="Choose as per your requirement", font=("Helvetica", 16))
    qualification_label.pack(pady=20)

    # Buttons for Internship, Extra-Curricular, and Co-Curricular
    internship_button = tk.Button(root, text="Internship", command = open_internship_search)
    internship_button.pack(pady=10)

    extracurricular_button = tk.Button(root, text="Extra-Curricular", command = open_extracurricular_search)
    extracurricular_button.pack(pady=10)

    cocurricular_button = tk.Button(root, text="Co-Curricular", command = open_cocurricular_search)
    cocurricular_button.pack(pady=10)

def open_internship_search():
    global root, id_entry, company_entry, type_var, role_entry, start_date_entry, end_date_entry, stipend_entry, organizer_entry

    # Destroy the current widgets in the qualification window
    for widget in root.winfo_children():
        widget.destroy()

    # Create a new window for Internship details
    root.title("Internship Details")

    # Labels and Entry fields for Internship details
    company_label = tk.Label(root, text="Name of the Company:")
    company_label.pack()

    company_entry = tk.Entry(root)
    company_entry.pack(pady=5)

    type_label = tk.Label(root, text="Type of Internship:")
    type_label.pack()

    # Dropdown for type of internship
    internship_types = ["Physical", "Online", "Hybrid"]
    type_var = tk.StringVar()
    type_dropdown = ttk.Combobox(root, textvariable=type_var, values=internship_types)
    type_dropdown.pack(pady=5)

    id_label = tk.Label(root, text="ID:")
    id_label.pack()

    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)

    role_label = tk.Label(root, text="Role:")
    role_label.pack()

    role_entry = tk.Entry(root)
    role_entry.pack(pady=5)

    start_date_label = tk.Label(root, text="Start Date:")
    start_date_label.pack()

    start_date_entry = tk.Entry(root)
    start_date_entry.pack(pady=5)

    end_date_label = tk.Label(root, text="End Date:")
    end_date_label.pack()

    end_date_entry = tk.Entry(root)
    end_date_entry.pack(pady=5)

    stipend_label = tk.Label(root, text="Stipend Amount:")
    stipend_label.pack()

    stipend_entry = tk.Entry(root)
    stipend_entry.pack(pady=5)

    # Submit and Back buttons
    search_button = tk.Button(root, text="Search", command = search_internship_details)
    search_button.pack(padx=10)

    delete_button = tk.Button(root, text="Delete", command=delete_internship_records)
    delete_button.pack(padx=10)

    back_button = tk.Button(root, text="Back", command=open_teacher_requirement_window)
    back_button.pack(padx=10)


def open_extracurricular_search():
    global root, id_entry, type_var1, organizer_entry, date_entry, type_var2

    # Destroy the current widgets in the qualification window
    for widget in root.winfo_children():
        widget.destroy()

    # Create a new window for Extracurricular details
    root.title("Extracurricular Details")

    id_label = tk.Label(root, text="ID:")
    id_label.pack()

    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)

    # Labels and Entry fields for Extracurricular details
    activity_label = tk.Label(root, text="Activity:")
    activity_label.pack()

    activity_types = ['Sports','Music and Dance','Drama and Theatre','Student Council','Volunteering','Scouting and guiding','Robotics Club','Online course','Fundraising','Other']
    type_var1 = tk.StringVar()
    type_dropdown = ttk.Combobox(root, textvariable=type_var1, values=activity_types)
    type_dropdown.pack(pady=5)

    organizer_label = tk.Label(root, text="Organizer:")
    organizer_label.pack()

    organizer_entry = tk.Entry(root)
    organizer_entry.pack(pady=5)

    date_label = tk.Label(root, text="Date:")
    date_label.pack()

    date_entry = tk.Entry(root)
    date_entry.pack(pady=5)

    achv_label = tk.Label(root, text="Achievement:")
    achv_label.pack()

    achievement_types = ["1st","2nd","3rd","Participation"]
    type_var2 = tk.StringVar()
    type_dropdown = ttk.Combobox(root, textvariable=type_var2, values=achievement_types)
    type_dropdown.pack(pady=5)


    # Search and Back buttons
    search_button = tk.Button(root, text="Search", command = search_internship_details)
    search_button.pack(padx=10)

    delete_button = tk.Button(root, text="Delete", command=delete_internship_records)
    delete_button.pack(padx=10)

    back_button = tk.Button(root, text="Back", command=open_teacher_requirement_window)
    back_button.pack(padx=10)

def open_cocurricular_search():
    global root, id_entry, type_var1, organizer_entry, date_entry, type_var2


    # Destroy the current widgets in the qualification window
    for widget in root.winfo_children():
        widget.destroy()

    # Create a new window for Cocurricular details
    root.title("Cocurricular Details")

    id_label = tk.Label(root, text="ID:")
    id_label.pack()

    id_entry = tk.Entry(root)
    id_entry.pack(pady=5)

    # Labels and Entry fields for Cocurricular details
    activity_label = tk.Label(root, text="Activity:")
    activity_label.pack()

    activity_types =['Debate','Quizes','Fairs','Olympiads','Exhibitions','workshops','Field Trips','Language Clubs']
    type_var1 = tk.StringVar()
    type_dropdown = ttk.Combobox(root, textvariable=type_var1, values=activity_types)
    type_dropdown.pack(pady=5)

    organizer_label = tk.Label(root, text="Organizer:")
    organizer_label.pack()

    organizer_entry = tk.Entry(root)
    organizer_entry.pack(pady=5)

    date_label = tk.Label(root, text="Date:")
    date_label.pack()

    date_entry = tk.Entry(root)
    date_entry.pack(pady=5)

    achv_label = tk.Label(root, text="Achievement")
    achv_label.pack()

    achievement_types = ["1st","2nd","3rd","Participation"]
    type_var2 = tk.StringVar()
    type_dropdown = ttk.Combobox(root, textvariable=type_var2, values=achievement_types)
    type_dropdown.pack(pady=5)


    # Search and Back buttons
    search_button = tk.Button(root, text="Search", command = search_internship_details)
    search_button.pack(padx=10)

    delete_button = tk.Button(root, text="Delete", command=delete_internship_records)
    delete_button.pack(padx=10)

    back_button = tk.Button(root, text="Back", command=open_teacher_requirement_window)
    back_button.pack(padx=10)


def search_internship_details():
    global root, id_entry, type_var, organizer_entry, date_entry, type_var

    # Get values from entry fields and dropdowns
    company_value = company_entry.get()
    type_value = type_var.get()
    id_value = id_entry.get()
    role_value = role_entry.get()
    start_date_value = start_date_entry.get()
    end_date_value = end_date_entry.get()
    stipend_value = stipend_entry.get()

    # Create a dictionary of search criteria
    search_criteria = {
        'Name_of_company': company_value,
        'Type_Intern': type_value,
        'ID': id_value,
        'Role_intern': role_value,
        'Start_Date': start_date_value,
        'End_Date': end_date_value,
        'Stipend_amt': stipend_value
    }

    # Search for internship records
    search_result = search_internship_records(search_criteria)

    if search_result:
        # Display the search results in a new window
        display_search_results(search_result)
    else:
        # Display a message if no matching records are found
        messagebox.showinfo("Search Results", "No matching records found.")


def search_extracurricular_details():
    global root, id_entry, type_var, organizer_entry, date_entry, type_var


    # Get values from entry fields and dropdowns
    id_value = id_entry.get()
    activity_value = type_var1.get()
    organizer_value = organizer_entry.get()
    date_value = date_entry.get()
    achievement_value = type_var2.get()

    # Create a dictionary of search criteria
    search_criteria = {
        'ID': id_value,
        'Activity': activity_value,
        'Organizer': organizer_value,
        'Achieve_Date': date_value,
        'Achievements': achievement_value
    }

    # Search for extracurricular records
    search_result = search_extracurricular_records(search_criteria)

    if search_result:
        # Display the search results in a new window
        display_search_results(search_result)
    else:
        # Display a message if no matching records are found
        messagebox.showinfo("Search Results", "No matching records found.")

def search_cocurricular_details():
    global root, id_entry, type_var, organizer_entry, date_entry, type_var

    # Get values from entry fields and dropdowns
    id_value = id_entry.get()
    activity_value = type_var1.get()
    organizer_value = organizer_entry.get()
    date_value = date_entry.get()
    achievement_value = type_var2.get()

    # Create a dictionary of search criteria
    search_criteria = {
        'ID': id_value,
        'Activity': activity_value,
        'Organizer': organizer_value,
        'Achieve_Date': date_value,
        'Achievements': achievement_value
    }

    # Search for cocurricular records
    search_result = search_cocurricular_records(search_criteria)

    if search_result:
        # Display the search results in a new window
        display_search_results(search_result)
    else:
        # Display a message if no matching records are found
        messagebox.showinfo("Search Results", "No matching records found.")

def delete_internship_records():
    # Get values from entry fields and dropdowns
    company_value = company_entry.get()
    type_value = type_var.get()
    id_value = id_entry.get()
    role_value = role_entry.get()
    start_date_value = start_date_entry.get()
    end_date_value = end_date_entry.get()
    stipend_value = stipend_entry.get()

    # Create a dictionary of delete criteria
    delete_criteria = {
        'Name_of_company': company_value,
        'Type_Intern': type_value,
        'ID': id_value,
        'Role_intern': role_value,
        'Start_Date': start_date_value,
        'End_Date': end_date_value,
        'Stipend_amt': stipend_value
    }

    # Construct the DELETE query based on the delete criteria
    where_clause = ' AND '.join([f'{key} = "{value}"' for key, value in delete_criteria.items() if value])

    # Construct the DELETE query
    delete_query = f"DELETE FROM INTERNSHIP {'WHERE ' + where_clause if where_clause else ''}"

    try:
        # Execute the DELETE query
        mycursor.execute(delete_query)
        mydb.commit()

        # Display a success message
        messagebox.showinfo("Success", "Records deleted successfully.")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        mydb.rollback()
        messagebox.showerror("Error", "Failed to delete records.")

def delete_extracurricular_records():
    # Get values from entry fields and dropdowns
    id_value = id_entry.get()
    activity_value = type_var1.get()
    organizer_value = organizer_entry.get()
    date_value = date_entry.get()
    achievement_value = type_var2.get()

    # Create a dictionary of delete criteria
    delete_criteria = {
        'ID': id_value,
        'Activity': activity_value,
        'Organizer': organizer_value,
        'Achieve_Date': date_value,
        'Achievements': achievement_value
    }

    # Construct the DELETE query based on the delete criteria
    where_clause = ' AND '.join([f'{key} = "{value}"' for key, value in delete_criteria.items() if value])

    # Construct the DELETE query
    delete_query = f"DELETE FROM Extracurricular {'WHERE ' + where_clause if where_clause else ''}"


    try:
        # Execute the DELETE query
        mycursor.execute(delete_query)
        mydb.commit()

        # Display a success message
        messagebox.showinfo("Success", "Records deleted successfully.")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        mydb.rollback()
        messagebox.showerror("Error", "Failed to delete records.")

def delete_cocurricular_records():
    # Get values from entry fields and dropdowns
    id_value = id_entry.get()
    activity_value = type_var1.get()
    organizer_value = organizer_entry.get()
    date_value = date_entry.get()
    achievement_value = type_var2.get()

    # Create a dictionary of delete criteria
    delete_criteria = {
        'ID': id_value,
        'Activity': activity_value,
        'Organizer': organizer_value,
        'Achieve_Date': date_value,
        'Achievements': achievement_value
    }

    # Construct the DELETE query based on the delete criteria
    where_clause = ' AND '.join([f'{key} = "{value}"' for key, value in delete_criteria.items() if value])

    # Construct the DELETE query
    delete_query = f"DELETE FROM Cocurricular {'WHERE ' + where_clause if where_clause else ''}"

    try:
        # Execute the DELETE query
        mycursor.execute(delete_query)
        mydb.commit()

        # Display a success message
        messagebox.showinfo("Success", "Records deleted successfully.")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        mydb.rollback()
        messagebox.showerror("Error", "Failed to delete records.")



def display_search_results(result):
    # Create a new window for displaying search results
    result_window = tk.Toplevel(root)
    result_window.title("Search Results")

    # Create a Treeview widget
    tree = ttk.Treeview(result_window)

    # Add columns to the Treeview using column names from the database table
    columns = [desc[0] for desc in mycursor.description]
    tree["columns"] = tuple(columns)

    # Configure column headings
    for col in columns:
        tree.column(col, anchor="center", width=100)
        tree.heading(col, text=col, anchor="center")

    # Add data to the Treeview
    for row in result:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill=tk.BOTH)



def back_to_main():
    global root

    # Recreate the main window
    create_main_window()

def create_main_window():
    global root

    try:
        for widget in root.winfo_children():
            widget.destroy()
    except NameError:
        root = tk.Tk()

    
    root.title("Student Information Management System")
    root.geometry("800x600")

    # Welcome message
    welcome_label = tk.Label(root, text="Welcome to Student Information Management System", font=("Helvetica", 16))
    welcome_label.pack(pady=20)

    # Buttons for Student and Teacher
    button_student = tk.Button(root, text="Student", command=open_student_window)
    button_student.pack(pady=10)

    button_teacher = tk.Button(root, text="Teacher", command=open_teacher_window)
    button_teacher.pack(pady=10)

    # Label for role selection
    label_role = tk.Label(root, text="Choose your role")
    label_role.pack()

    # Start the main event loop
    root.mainloop()

#Creation of Database
create_table()

# Initial creation of the main window
create_main_window()

