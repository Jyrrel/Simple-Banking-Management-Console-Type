# Banking Management System
# Overview
The Banking Management System is a command-line application developed in Python that allows users to manage various banking operations, such as account creation, deposits, withdrawals, account updates, and more. The system ensures that users can securely interact with their accounts while maintaining minimum balance requirements for different types of accounts (savings and current).
The program uses the pickle module to store account data persistently in a binary file (bank.bin), allowing users to retrieve and modify accounts across different sessions.

## Some Preview
<div align="center">
  <img width="70%" src="https://github.com/Jyrrel/Simple-Banking-Management-Console-Type/blob/main/Simple-bank-managemnet-system-2/assets/Screenshot%202024-10-18%20193047.png"><br><br>
</div>
________________________________________
Features
1.	Account Creation:
o	Users can create a savings or current account.
o	Minimum balance for savings: 5000.
o	Minimum balance for current: 2000.
o	Each account is assigned a unique account number.
2.	View All Accounts:
o	Displays a list of all created accounts with account number, name, type, and balance.
3.	Deposit:
o	Users can deposit money into an existing account by providing the account number.
4.	Withdraw:
o	Users can withdraw money from their accounts, ensuring minimum balance limits are respected.
5.	Update Account:
o	Users can update their account information, including name, account type, and balance.
6.	Search Account:
o	Users can search for an account by providing the account number and view the account details.
7.	Delete Account:
o	Users can delete an account from the system using the account number.
8.	Login System:

How to Run the Code
To run this Python-based Banking Management System, follow the steps below:

Step 1: Clone or Download the Repository
You can either clone the repository or download the zip file.

bash
Copy code
git clone [https://github.com/your-repo/banking-management-system.git](https://github.com/Jyrrel/Simple-Banking-Management-Console-Type.git)
Step 2: Navigate to the Project Directory
bash
Copy code
cd banking-management-system
Step 3: Install Required Python Modules
Ensure that Python 3.x is installed on your machine. The program relies on the pickle module, which is part of the standard Python library, so no external packages are needed. However, you should make sure Python is properly installed by running:

bash
Copy code
python --version
Step 4: Run the Python Script
You can execute the Python script using the following command:

bash
Copy code
python banking_system.py
Step 5: Using the Application
After running the program, you will be prompted with the Main Menu to log in or access the banking operations. Simply follow the instructions on the screen to perform various banking tasks such as creating an account, depositing funds, withdrawing funds, updating account information, searching for accounts, and deleting accounts.

License
This project is open-source and can be modified or distributed freely.
