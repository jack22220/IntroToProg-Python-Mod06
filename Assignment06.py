# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JJohanneson,11/19/2023
# ------------------------------------------------------------------------------------------ #
import json

class FileProcessor:

    @staticmethod
    def input_menu_choice():
        choice = input("What would you like to do: ")
        return choice

    @staticmethod
    def input_student_data(data: list):
        try:
            temp: dict
            first_name = input("Enter the student's first name: ")
            if not first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            last_name = input("Enter the student's last name: ")

            if not last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            temp = {"FirstName": first_name,
                            "LastName": last_name,
                            "CourseName": course_name}
            data.append(temp)

        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.",e)
        print(f"You have registered {first_name} {last_name} for {course_name}.")
        return data

    @staticmethod
    def read_data_from_file(file_name: str, data: list):
        try:
            file = open(file_name, "r")
            data = json.load(file)
            file.close()

        except Exception as e:
            IO.output_error_messages("Error: There was a problem with reading the file.\n"
                                     "Please check that the file exists and that it is in a json format.", e)

        finally:
            if file.closed == False:
                file.close()

    @staticmethod
    def write_data_to_file(file_name: str, data: list):
        try:
            file = open(file_name, "w")
            json.dump(data, file)
            file.close()

            print('The following students were enrolled ')
            for student in data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')



        except Exception as e:
            if not file.closed:
                file.close()

            IO.output_error_messages("Error: There was a problem with writing to the file.\n"
                                     "Please check that the file is not open by another program.", e)





class IO:

    @staticmethod
    def output_menu(menu: str):
        print(menu)

    @staticmethod
    def output_error_messages(message: str, e: Exception = None):
        print(message)
        if e is not None:
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
    @staticmethod
    def output_student_courses(data: list):
        print("-" * 50)
        for student in data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)

FileProcessor.read_data_from_file(FILE_NAME,students)  # Extract the data from the file

# Present and Process the data
while True:
    IO.output_menu(MENU)  # Present the menu of choices
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        FileProcessor.input_student_data(students)  # prompt data input and append as a dictionary to students
        continue

    # Present the current data
    elif menu_choice == "2":

        IO.output_student_courses(students)  # display students entered and their courses
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME,students)  # save student data to file
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
