import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the environment variables
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Connect to the database using the environment variables
mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)
mycursor = mydb.cursor()

def check_id(id_entry):
    # Get the entered ID from the entry field
    entered_id = id_entry.get()

    mycursor.execute("SELECT ID FROM Student WHERE ID = %s", (entered_id,))
    result = mycursor.fetchone()

    if result:
        return True
    else:
        return False

    
def insert_student_details(id_value, first_name_value, last_name_value, college_value,
                            email_value, phone_number_value, department_value, year_of_study_value):
    try:
        # Construct the INSERT query
        insert_query = """
            INSERT INTO STUDENT (ID, Fname, Lname, College, Email, Ph_num, Dept, Year_of_study)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Student data to be inserted
        student_data = (id_value, first_name_value, last_name_value, college_value,
                        email_value, phone_number_value, department_value, year_of_study_value)

        # Fetch any remaining rows to clear the result set
        mycursor.fetchall()

        # Execute the INSERT query
        mycursor.execute(insert_query, student_data)

        # Commit the changes
        mydb.commit()

        # Display a success message or perform other actions
        print("Student details inserted successfully!")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        mydb.rollback()  # Rollback changes in case of an error

# Call this function in your main code with appropriate values


   

def insert_internship_details(company, internship_type, student_id, role, start_date, end_date, stipend_amount):
    global mydb, mycursor

    # Execute the INSERT query to add internship details to the database
    insert_query = """
        INSERT INTO INTERNSHIP (Name_of_company, Type_Intern, Role_intern, Start_Date, End_Date, Stipend_amt, ID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    internship_data = (company, internship_type, role, start_date, end_date, stipend_amount, student_id)

    try:
        mycursor.fetchall()
        mycursor.execute(insert_query, internship_data)
        mydb.commit()
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        mydb.rollback()


def insert_extracurricular_details(details):
        try:
            # Construct the INSERT query
            insert_query = """
                INSERT INTO Extracurricular (Activity, Achieve_Date, Organizer,  Achievements, ID)
                VALUES (%s, %s, %s, %s, %s)
            """
            mycursor.fetchall()
            # Execute the INSERT query
            mycursor.execute(insert_query, details)

            # Commit the changes
            mydb.commit()

            return True

        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return False
        
def insert_cocurricular_details(details):
    try:
        # Construct the INSERT query
        insert_query = """
            INSERT INTO Cocurricular (Activity, Achieve_Date, Organizer,  Achievements, ID)
            VALUES (%s, %s, %s, %s, %s)
        """
        mycursor.fetchall()
        # Execute the INSERT query
        mycursor.execute(insert_query, details)

        # Commit the changes
        mydb.commit()

        return True

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return False
    
def search_internship_records(search_criteria):
    try:
        # Construct the SELECT query based on the search criteria
        where_clause = ' AND '.join(f"{key} = '{value}'" for key, value in search_criteria.items() if value)
        select_query = f"""
            SELECT *
            FROM INTERNSHIP
            {"WHERE " + where_clause if where_clause else ""}
        """

        
        mycursor.execute(select_query)
        result = mycursor.fetchall()

        return result

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None
    
def search_extracurricular_records(search_criteria):
    try:
        # Construct the SELECT query based on the search criteria
        where_clause = ' AND '.join(f"{key} = '{value}'" for key, value in search_criteria.items() if value)
        select_query = f"""
            SELECT *
            FROM Extracurricular
            {"WHERE " + where_clause if where_clause else ""}
        """

        mycursor.execute(select_query)
        result = mycursor.fetchall()

        return result if result else None

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None
    
def search_cocurricular_records(search_criteria):
    try:
        # Construct the SELECT query based on the search criteria
        where_clause = ' AND '.join(f"{key} = '{value}'" for key, value in search_criteria.items() if value)
        select_query = f"""
            SELECT *
            FROM Cocurricular
            {"WHERE " + where_clause if where_clause else ""}
        """

        mycursor.execute(select_query)
        result = mycursor.fetchall()

        return result

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return None
