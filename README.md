# Banking Management System
# Overview
The Banking Management System is a command-line application developed in Python that allows users to manage various banking operations, such as account creation, deposits, withdrawals, account updates, and more. The system ensures that users can securely interact with their accounts while maintaining minimum balance requirements for different types of accounts (savings and current).
The program uses the pickle module to store account data persistently in a binary file (bank.bin), allowing users to retrieve and modify accounts across different sessions.

## Some Preview
<div align="center">
  <img width="70%" src="assets\Screenshot 2024-10-18 193047.png" alt="preview"><br><br>
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
