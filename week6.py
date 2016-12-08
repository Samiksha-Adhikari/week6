# On start
print("Welcome to prudent Health Care")


import time

users = {
    "root": {
        "password": "gucci-mane",
        "group": "admin",
    }
}


#form
def writes(patient_id, first_name, last_name, address, gender, contact):
        fw = open('data2.txt', "a")
        fw.write("%1s%20s%20s%20s%20s%20s\n" % (patient_id, first_name, last_name, address, gender, contact))
        fw.close()
# approving form
def validate(form):
    if len(form) > 0:
        return False
    return True

def last():
    print("Options:\n1=register \n2=login\n3=physian\n4=payment \n5=exit")
    while True:
        option = input("> ")
        if option == "1":
            register()
        elif option == "2":
            login()
        elif option == "3":
            physian()
        elif option == "4":
            payment()
        elif option == "5":
            break
        else:
            print(option + " is not an option")
    print("-----------------------------------------po")
    # On exit
    print("Shutting down...")
    time.sleep(1)


# login authorization
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login successful")
            return True
    return False


# login
def login():
   pid=input("enter ur pid")
   users = open("data2.txt", 'r')

   for each_line in users:
       (patient_id, first_name, last_name, address, gender, contact) = each_line.split()

       if (patient_id == pid):
           print(patient_id, first_name, last_name, address, gender, contact)
   users.close()
   last()

def cash(name, by, recebill):
    fw = open('data1.txt', "a")
    fw.write("%1s%20s%20s\n" % (name, by, recebill))
    fw.close()

def credit(name,by,crebill):
    fw = open('data1.txt', "a")
    fw.write("%1s%20s%20s\n" % (name, by, crebill))
    fw.close()

# registration
def register():
    first_name = input("Enter your first_name")
    last_name = input("Enter your last name")
    patient_id = input("Enter patient_id")
    address = input("Enter your address")
    gender = input("Enter your gender ")
    contact = input("Enter your contact number")
    writes(patient_id, first_name, last_name, address, gender, contact)
    print("THANK YOU!!!")
    print("\nUser created!\n")
    last()


# User screen
def userscreen(username):
    print("1. Book an appointment")
    choice_str = input("Input your choice\n")
    number = int(choice_str)
    if number == 1:
        appointment()

    else:
        appointment()






def physian():
    print("Book an appointment")
    print("List of specialists")
    print("1. Doctor A")
    print("2. Doctor B")
    print("3. Doctor C")
    print("4. Doctor D")

    # This is for Doctor A
    select_doctor = input("Choose your doctor\n")

    if select_doctor == "1":

        print("Doctor A \n a. 08:00AM-09:00AM \n b.12:00AM-01:00PM \n c. 03:00PM-04:00PM")

        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 08:00AM-09:00AM")
        elif your_time == "b":
            print("b. 12:00AM-01:00PM")
        elif your_time == "c":
            print("c. 03:00PM-04:00PM")

        else:
            print("Not available")
        notification = input("notification goes to doctor for check up press y")
        if notification == "y":
            print("y. Check up done.")
            last()
        else:
            print("waiting list")
            last()
            # This is for Doctor B

    elif select_doctor == "2":

        print("Doctor B \n a. 09:30AM-10:30AM\n b. 01:30PM-02:30PM \n c. 03:30PM-04:30PM")

        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 09:30AM-10:30AM")
        elif your_time == "b":
            print("b. 01:30PM-02:30PM")
        elif your_time == "c":
            print("c. 03:30PM-04:30PM")
        else:
            print("Not available")
        notification = input("notification goes to doctor for check up press y")
        if notification == "y":
            print("y. Check up done.")
            last()
        else:
            print("waiting list")
            last()

            # This is for Doctor C

    elif select_doctor == "3":

        print("Doctor C \n a. 11:00AM-12:00AM \n b. 01:00PM-02:00PM \nc. 03:00PM-04:00PM")

        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 11:00AM-12:00AM")
        elif your_time == "b":
            print("b. 01:00PM-02:00PM")
        elif your_time == "c":
            print("c. 03:00PM-04:00PM")
        else:
            print("Not available")
        notification = input("notification goes to doctor for check up press y")
        if notification == "y":
            print("y. Check up done.")
            last()
        else:
            print("waiting list")
            last()

            # This is for Doctor D

    elif select_doctor == "4":

        print("Doctor D \n a. 07:30AM-08:30AM \n b. 10:30AM-11:30AM \n c. 04:30PM-05:30PM")
        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 07:30AM-08:30AM")
        elif your_time == "b":
            print("b. 10:30AM-11:30AM")
        elif your_time == "c":
            print("c. 04:30PM-05:30PM")
        else:
            print("Not available")
        notification = input("notification goes to doctor for check up Press y")
        if notification == "y":
            print("y. Check up done.")
            last()
        else:
            print("waiting list")
            last()

            # This is for payment process
def payment():
    print("For cash Enter C")
    print("For credit Enter L")
    payment = input("finish the payment")
    if payment == "C":
        print("payment done by cash")
        print("payment done by cash")
        name = input("Enter your name")
        by = input("write by cash")
        recebill = input("Please enter the receipt for the bill:-")
        print(recebill)
        cash(name, by, recebill)
        print("Thank you")
        last()

    elif payment == "L":
        print("payment done by credit")
        name = input("Enter your name")
        by = input("write by credit")
        crebill = input("Please enter the credit card number")

        print(crebill)
        credit(name,by,crebill)
        print("Thank you")
        last()
    else:
        print("not paid and go for payment")
        print("Thank You")
        last()


# ---When you open the program....
print("---------------------------------------")

print("Options:\n1=register \n2=login\n3=physian\n4=payment \n5=exit")
while True:
    option = input("> ")
    if option == "1":
        register()
    elif option == "2":
        login()
    elif option=="3":
        physian()
    elif option == "4":
         payment()
    elif option == "5":
        break
    else:
        print(option + " is not an option")
print("-----------------------------------------po")
# On exit
print("Shutting down...")
time.sleep(1)

