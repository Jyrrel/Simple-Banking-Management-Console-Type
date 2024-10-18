import pickle
import os

# Predefined login credentials (can modify or extend this)
login_credentials = {'admin': 'admin123'}

class Customer:
    def __init__(self, A):
        self.name = input("Enter Name: ")
        self.type = input("Type of Account s/c?: ")
        self.amount = int(input("Enter Amount: "))
        while True:
            if self.type == 's':
                if self.amount < 5000:
                    print("Min 5000 required")
                    self.amount = int(input("Please Enter amount again: "))
                else:
                    break
            if self.type == 'c':
                if self.amount < 2000:
                    print("Min 2000 required")
                    self.amount = int(input("Please Enter amount again: "))
                else:
                    break
        self.accountNo = A
        print("Your Account No. is:", self.accountNo)

    def Display(self):
        print("{:<15} {:<15} {:<15} {:<15}".format(self.accountNo, self.name, self.type, self.amount))


def createAccount():
    try:
        file = open('bank.bin', 'rb')
        while True:
            t = pickle.load(file)
            A = t.accountNo
    except FileNotFoundError as e:
        A = 121000
    except EOFError as e:
        A = A + 1
        file.close()
    file = open('bank.bin', 'ab')
    s = Customer(A)
    pickle.dump(s, file)
    file.close()
    option()


def ViewAllAccount():
    try:
        file = open('bank.bin', 'rb')
        print("{:<15} {:<15} {:<15} {:<15}".format('Account No.', 'Name', 'Type', 'Amount'))
        while True:
            t = pickle.load(file)
            t.Display()
    except FileNotFoundError as e:
        print("\nThere Are No Records")
    except EOFError as e:
        file.close()
    option()


def Deposit():
    file = open('bank.bin', 'rb')
    file1 = open('tmp.bin', 'wb')
    x = int(input("Enter Bank Account: "))
    try:
        while True:
            t = pickle.load(file)
            if t.accountNo == x:
                cr = int(input("Enter Deposit Amount: "))
                t.amount = t.amount + cr
            pickle.dump(t, file1)
    except:
        pass
    finally:
        file.close()
        file1.close()
    os.remove('bank.bin')
    os.rename('tmp.bin', 'bank.bin')
    option()


def Withdraw():
    file = open('bank.bin', 'rb')
    file1 = open('tmp.bin', 'wb')
    x = int(input("Enter Bank Account: "))
    try:
        while True:
            t = pickle.load(file)
            if t.accountNo == x:
                dr = int(input("Enter Withdraw Amount: "))
                if t.type == 's':
                    while True:
                        if t.amount - dr < 5000:
                            print("Saving Account Balance can't be below 5000")
                            dr = int(input("Enter Withdraw Amount: "))
                        else:
                            t.amount = t.amount - dr
                            break
                if t.type == 'c':
                    while True:
                        if t.amount - dr < 2000:
                            print("Current Account Balance can't be below 2000")
                            dr = int(input("Enter Withdraw Amount: "))
                        else:
                            t.amount = t.amount - dr
                            break
            pickle.dump(t, file1)
    except:
        pass
    finally:
        file.close()
        file1.close()
    os.remove('bank.bin')
    os.rename('tmp.bin', 'bank.bin')
    option()


def Update():
    file = open('bank.bin', 'rb')
    file1 = open('tmp.bin', 'wb')
    x = int(input("Enter Bank Account: "))
    try:
        while True:
            t = pickle.load(file)
            if t.accountNo == x:
                print("\n1. Update Name\n2. Update Account Type\n3. Update Balance")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    t.name = input("Update Name: ")
                elif choice == 2:
                    t.type = input("Update Account Type s/c: ")
                elif choice == 3:
                    t.amount = int(input("Update Balance: "))
            pickle.dump(t, file1)
    except:
        pass
    finally:
        file.close()
        file1.close()
    os.remove('bank.bin')
    os.rename('tmp.bin', 'bank.bin')
    option()


def DeleteAccount():
    file = open('bank.bin', 'rb')
    file1 = open('tmp.bin', 'wb')
    x = int(input("Enter Bank Account to Delete: "))
    deleted = False
    try:
        while True:
            t = pickle.load(file)
            if t.accountNo != x:
                pickle.dump(t, file1)
            else:
                deleted = True
    except EOFError:
        pass
    finally:
        file.close()
        file1.close()
    os.remove('bank.bin')
    os.rename('tmp.bin', 'bank.bin')
    if deleted:
        print("Account Deleted Successfully")
    else:
        print("Account Not Found")
    option()


def Search():
    file = open('bank.bin', 'rb')
    x = int(input("Enter Bank Account: "))
    try:
        while True:
            t = pickle.load(file)
            if t.accountNo == x:
                print("\nName:", t.name)
                print("Account Type:", t.type)
                print("Amount:", t.amount)
                print("Account No.:", t.accountNo)
                break
    except:
        pass
    finally:
        file.close()
    option()


def login():
    print("Please log in:")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in login_credentials and login_credentials[username] == password:
        print("Login Successful!")
        option()  # Continue to the banking menu
    else:
        print("Invalid username or password!")
        main_menu()  # Go back to the main menu


def Exit():
    main_menu()  # Go back to the main menu instead of exiting


def option():
    print()
    print("What Do You Wanna Do\n1. Create Account\n2. View all Accounts\n3. Deposit\n4. Withdraw\n5. Update Account\n6. Search\n7. Delete Account\n8. Back to Main Menu")
    n = int(input())
    if n == 1:
        createAccount()
    elif n == 2:
        ViewAllAccount()
    elif n == 3:
        Deposit()
    elif n == 4:
        Withdraw()
    elif n == 5:
        Update()
    elif n == 6:
        Search()
    elif n == 7:
        DeleteAccount()
    elif n == 8:
        Exit()
    else:
        print("Invalid option")
        print("Try again")
        option()


def main_menu():
    print("\nBANKING MANAGEMENT SYSTEM")
    print("1. Banking Menu")
    print("2. Log In")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        option()
    elif choice == 2:
        login()
    elif choice == 3:
        print("Goodbye!")
        exit()  # Only exit the program in this option
    else:
        print("Invalid option!")
        main_menu()


# Start the program by displaying the main menu
main_menu()
