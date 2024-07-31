import mysql.connector
from dotenv import load_dotenv
import os

def create_table():
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

    create_database_query = "CREATE DATABASE IF NOT EXISTS project"

    # Define the CREATE TABLE statements with IF NOT EXISTS clause
    create_student_table = """
        CREATE TABLE IF NOT EXISTS STUDENT(
            ID varchar(50) Primary Key,
            Fname VARCHAR(50),
            Lname VARCHAR(50),
            College VARCHAR(50),
            Email VARCHAR(50),
            Ph_num varchar(15),
            Dept VARCHAR(10) CHECK (Dept IN ('CSE','IT','ECE','EEE','BME','Chem','Mech','Other')),
            Year_of_study varchar(5) CHECK (Year_of_study in ('1','2','3','4','PG'))
        )
    """

    create_internship_table = """
        CREATE TABLE IF NOT EXISTS INTERNSHIP(
            Name_of_company VARCHAR(50),
            Type_Intern VARCHAR(50),
            Role_intern VARCHAR(50),
            Start_Date char(50),
            End_Date char(50),
            Stipend_amt varchar(50),
            ID varchar(50) REFERENCES STUDENT(ID)
        )
    """

    create_extracurricular_table = """
        CREATE TABLE IF NOT EXISTS Extracurricular(
            Activity VARCHAR(50),
            Achieve_Date char(10),
            Organizer VARCHAR(50),
            Achievements VARCHAR(50),
            ID varchar(50) REFERENCES STUDENT(ID)
        )
    """

    create_cocurricular_table = """
        CREATE TABLE IF NOT EXISTS Cocurricular(
            Activity VARCHAR(50),
            Achieve_Date char(10),
            Organizer VARCHAR(50),
            Achievements VARCHAR(50),
            ID varchar(50) REFERENCES STUDENT(ID)
        )
    """
    mycursor.execute(create_database_query)
    mycursor.execute("Use Project")
    # Execute the CREATE TABLE statements
    mycursor.execute(create_student_table)
    mycursor.execute(create_internship_table)
    mycursor.execute(create_extracurricular_table)
    mycursor.execute(create_cocurricular_table)

    # Commit the changes

    mydb.commit()
