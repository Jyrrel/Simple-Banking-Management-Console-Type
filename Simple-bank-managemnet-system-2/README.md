# Banking Management System
# Overview
The Banking Management System is a command-line application developed in Python that allows users to manage various banking operations, such as account creation, deposits, withdrawals, account updates, and more. The system ensures that users can securely interact with their accounts while maintaining minimum balance requirements for different types of accounts (savings and current).
The program uses the pickle module to store account data persistently in a binary file (bank.bin), allowing users to retrieve and modify accounts across different sessions.

## Some Preview
<div align="center">
  <img width="70%" src="https://github.com/Jyrrel/Simple-Banking-Management-Console-Type/blob/main/Simple-bank-managemnet-system-2/assets/Screenshot%202024-10-18%20193047.png"><br><br>
</div>

## Features
1.	Account Creation:
Users can create a savings or current account.

Minimum balance for savings: 5000.

Minimum balance for current: 2000.

Each account is assigned a unique account number.

2.	View All Accounts:
Displays a list of all created accounts with account number, name, type, and balance.

4.	Deposit:
Users can deposit money into an existing account by providing the account number.

5.	Withdraw:
Users can withdraw money from their accounts, ensuring minimum balance limits are respected.

6.	Update Account:
Users can update their account information, including name, account type, and balance.

7.	Search Account:
Users can search for an account by providing the account number and view the account details.

8.	Delete Account:
Users can delete an account from the system using the account number.

10.	Login System:


# How to Run the Code
To run this Python-based Banking Management System, follow the steps below:

## Step 1: Clone or Download the Repository
You can either clone the repository or download the zip file.
```bash
git clone https://github.com/Jyrrel/Simple-Banking-Management-Console-Type.git
```
## Step 2: Navigate to the Project Directory

```bash
cd banking-management-system
```
## Step 3: Install Required Python Modules
Ensure that Python 3.x is installed on your machine. Run:
```bash
python --version
```

## Step 4: Run the Python Script
```bash
python banking_system.py
```
## Step 5: Using the Application
Follow the on-screen instructions to perform various banking tasks.
