# Student-Information-System

## Project Description

The Student Information System is a Python application built using Tkinter and MySQL. It is designed to store and manage details regarding students' internships, extracurricular, and co-curricular activities, along with their basic personal information.

## Features

- **Student Details**: Store and manage basic student information such as name, age, gender, and contact details.
- **Internship Details**: Record information about students' internships, including company name, duration, and role.
- **Extracurricular Activities**: Track students' participation in extracurricular activities such as sports, arts, and clubs.
- **Co-curricular Activities**: Manage details of students' involvement in co-curricular activities like seminars, workshops, and courses.
- **Interactive GUI**: User-friendly interface developed with Tkinter.

## Requirements

To run this project, you need the following Python packages:

- `mysql-connector-python==9.0.0`
- `python-dotenv==1.0.1`

You can install these packages using the following command:

```sh
pip install mysql-connector-python==9.0.0 python-dotenv==1.0.1
```
## Setting up Environment Variables

- Create a .env file in the root directory of your project and add the following environment variables with your MySQL database credentials:

- DB_HOST=your_database_host
- DB_USER=your_database_user
- DB_PASSWORD=your_database_password
- DB_NAME=your_database_name

## Database Setup

- Ensure mysql is installed and a proper connection to a mysql instance is established before execution.