import random
import string

password = {}
file_path = "password_data.txt"

while True:
    print("=========================== Welcome to the Password Management System =========================\n")
    print("1. To Add the password")
    print("2. To View the password")
    print("3. To Create the password")
    print("4. To Exit")

    choice = int(input("Enter your choice: \n"))

    if choice == 1:
        site = input("Enter the site: ")
        password = input("Enter the password: ")

        with open(file_path, 'a') as file:
            file.write(f"{site}:{password}\n")

    elif choice == 2:
        
        with open(file_path, 'r') as file:
            # data = file.read()
            for line in file:
                site, password = line.strip().split(":")
                print(site, password)
    elif choice == 3:
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        generated_pwd = "".join(random.choice(characters) for _ in range(8)) # Here for loop is used to generate the random character 8 times as I want the 8 character long password as at a time random module generate only one character
        print(generated_pwd)

        # print(data)

    elif choice == 4:
        print("Thanks for the visit")
        break
    else:
        print("Invalid input")
        break
