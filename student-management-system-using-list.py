# Student's information system ( through list)

# LIST - where student information will be store :D
names = []
srcode = []
ages = []
majors = []
emails = []
address = []

#METHODS

def add():
    print("\nADDING STUDENT INFROMATION")
    name = input("\nENTER STUDENT NAME: ")
    sr = input("ENTER STUDENT SR-Code: ")

    if sr in srcode:
        print("\nTHERE IS ALREADY A STUDENT WHO IS REGISTERED WITH THAT SR CODE. \nPLEASE TRY ANOTHER ONE.")
        add()

    else:
        age = input("ENTER STUDENT AGE: ")
        major = input("ENTER STUDENT MAJOR: ")
        email = input("ENTER STUDENT E-MAIL ID: ")
        location = input("ENTER STUDENT ADDRESS: ")
        names.append(name)
        srcode.append(sr)
        ages.append(age)
        majors.append(major)
        address.append(location)
        emails.append(email)

    print("\nADDED SUCCESSFULLY!")

def view():
    print("\nDISPLAYING STUDENT INFORMATION")
    for i in range(len(srcode)):
      num = i+1
      print("\nSTUDENT NO:",num)
      print("NAME:",names[i])
      print("SR-Code:",srcode[i])
      print("AGE:", ages[i])
      print("MAJOR:", majors[i])
      print("E-MAIL ID:", emails[i])
      print("STUDENT ADDRESS:", address[i])



def delete():
    code = input("\nENTER THE STUDENT SR-Code THAT YOU WANT TO DELETE INFORMATION: ")
    if code in srcode:
        index = srcode.index(code)
        names.pop(index)
        srcode.pop(index)
        ages.pop(index)
        majors.pop(index)
        emails.pop(index)
        address.pop(index)

        print("\nSTUDENT'S INFORMATION SUCCESSFULLY DELETED!")
    else:
        print("\nTHERE ARE NO STUDENT WITH THE SAME SR-Code IN THE RECORDS!")

def edit():
    code = input("\nENTER THE STUDENT SR-Code THAT YOU WANT TO UPDATE INFORMATION: ")
    if code in srcode:
        index = srcode.index(code)
        print("\nUPDATING STUDENT INFORMATION"+"\n\nKINDLY ENTER THE UPDATED STUDENT INFORMATION DETAILS!")
        names[index] = input("NAME: ")
        srcode[index] = input("SR-Code: ")
        ages[index] = input("AGE: ")
        majors[index] = input("MAJOR: ")
        emails[index] = input("EMAIL: ")
        address[index] = input("LOCATION: ")


        print("\nUPDATED INFORMATION")
        print("NAME:",names[index])
        print("SR-Code:", srcode[index])
        print("AGE:", ages[index])
        print("MAJOR:", majors[index])
        print("EMAIL:", emails[index])
        print("LOCATION:", address[index])

        print("\nSTUDENT'S INFORMATION SUCCESSFULLY UPDATED!")
    else:
        print("\nTHERE ARE NO STUDENT WITH THE SAME SR-Code IN THE RECORDS!")

def menu():
    exit = "5"


    # MENU CHOICES

    while True:
        choice = input("\nPRESS FROM THE FOLLOWING OPTION: \n\nPRESS 1 : TO ADD STUDENT INFROMATION"
                       "\nPRESS 2 : TO DELETE STUDENT INFROMATION \nPRESS 3 : TO UPDATE STUDENT INFORMATION  \nPRESS 4 : TO DISPLAY STUDENT INFORMATION"
                       "\nPRESS 5 : TO EXIT SYSTEM\n")

        if choice == '1':
            add()

        elif choice == '2':
            delete()

        elif choice == '3':
            edit()

        elif choice == '4':
            view()

        elif choice == exit:
            print("THANK YOU")
            break

        else:
            print("INVALID INPUT. PLEASE TRY AGAIN.")

menu()

