import pickle
import os

# Predefined login credentials for initial access
login_credentials = {'admin': 'admin123'}

class Customer:
    def __init__(self, A):
        # Ensure the name field is not empty
        self.name = input("Enter Name: ")
        while not self.name.strip():  # Ensure name is not blank
            print("Name cannot be blank.")
            self.name = input("Enter Name: ")

        self.type = input("Type of Account s/c?: ")
        self.amount = int(input("Enter Amount: "))
        self.pin = input("Set a 4-digit PIN for this account: ")
        while len(self.pin) != 4 or not self.pin.isdigit():
            print("PIN must be exactly 4 digits.")
            self.pin = input("Set a 4-digit PIN for this account: ")
        
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
    deposited = False
    try:
        while True:
            t = pickle.load(file)
            if t.accountNo == x:
                cr = int(input("Enter Deposit Amount: "))
                t.amount += cr
                deposited = True
                print(f"Successfully deposited {cr}. New Balance: {t.amount}")
                print("Thank you for depositing!")
            pickle.dump(t, file1)
    except EOFError:
        if not deposited:
            print("Account not found!")
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


def account_login():
    print("Account Login")
    account_no = int(input("Enter Account Number: "))
    pin = input("Enter 4-digit PIN: ")
    
    file = open('bank.bin', 'rb')
    try:
        while True:
            t = pickle.load(file)
            if t.accountNo == account_no and t.pin == pin:
                print("Login Successful!")
                option()  # Proceed to banking menu if login is successful
                return
    except EOFError:
        print("Invalid account number or PIN!")
    finally:
        file.close()
    main_menu()


def main_menu():
    print("\nBANKING MANAGEMENT SYSTEM")
    print("1. Create Account")
    print("2. Log In")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        createAccount()
    elif choice == 2:
        account_login()
    elif choice == 3:
        print("Goodbye!")
        exit()  # Only exit the program in this option
    else:
        print("Invalid option!")
        main_menu()


def option():
    print()
    print("What Do You Wanna Do\n1. View all Accounts\n2. Deposit\n3. Withdraw\n4. Update Account\n5. Search\n6. Delete Account\n7. Log Out")
    n = int(input())
    if n == 1:
        ViewAllAccount()
    elif n == 2:
        Deposit()
    elif n == 3:
        Withdraw()
    elif n == 4:
        Update()
    elif n == 5:
        Search()
    elif n == 6:
        DeleteAccount()
    elif n == 7:
        main_menu()
    else:
        print("Invalid option")
        print("Try again")
        option()


# Start the program by displaying the main menu
main_menu()
