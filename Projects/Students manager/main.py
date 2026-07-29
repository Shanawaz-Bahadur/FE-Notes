import json
import os 

file_path = "students_details.json"
roll_no = 0

try:
    while True:
        print("=========================== Welcome to the Student management system =========================\n")
        print("1. To Add the students")
        print("2. To View the students")
        print("3. To Delete students")
        print("4. To Exit")

        user_input = int(input("Enter you option\n"))
        if user_input == 1:
            student_detail = {}

            stud_name = input("Enter the student name: \n")
            stud_address = input("Enter the student Address: \n")
            stud_age = input("Enter the student Age: \n")
            stud_std = input("Enter the student Standard: \n")
            roll_no += 1

            student_detail["name"] = stud_name
            student_detail["stud_address"] = stud_address
            student_detail["stud_age"] = stud_age
            student_detail["stud_std"] = stud_std
            student_detail["roll_no"] = roll_no

            print(f"{stud_name} successfully added !\n")
            print(student_detail)

            # 1. Initialize the file with an empty list if it does not exist
            if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
                with open(file_path, 'w') as file:
                    json.dump([], file)

            # Reading the current data in the file to append the next student.
            with open(file_path, 'r') as file:
                current_list = json.load(file)
            
            current_list.append(student_detail)

            # Updating the new student in the file
            with open(file_path, 'w') as file:
                json.dump(current_list, file, indent=4)
            
        elif user_input == 2:
            with open(file_path, 'r') as file:
                file_data = json.load(file)

            print("This is the list of students: \n", file_data, type(file_data))
            print("Name of the students: ",[ obj['name'] for obj in file_data])

        elif user_input == 3:
            del_roll_no = int(input("Enter the roll no. to be removed: "))

            with open(file_path, 'r') as file:
                data = json.load(file)

            print(data)
            
            for obj in data:
                if obj['roll_no'] == del_roll_no:
                    data.remove(obj)
                    break

            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)

        elif user_input == 4:
            print("Thank you for a  visit")
            break

        else:
            print("Invalid Input...")
            break

except Exception as e:
    print(f"{type(e).__name__}: {e}")