# Simple Banking System with Database in Python

This project is a fully functional **Simple Banking System** built with **Python** and **Tkinter**. It provides users with an intuitive graphical interface to perform common banking operations, such as creating an account, depositing funds, withdrawing money, and viewing transaction history. The system is integrated with a basic file-based database to store user accounts and transaction data securely.

## Features

- **Create Account**: Users can create a new account by providing their personal details, such as name, phone number, email, and initial deposit amount. The system securely stores this information.
  
- **Deposit & Withdraw**: Users can deposit or withdraw money from their accounts, with real-time updates to their balance and transaction history.

- **View Account Information**: Users can view their account details and transaction history. The account data includes account number, name, email, phone number, account type, and current balance.

- **Delete Account**: Users can delete their account after verifying their password, with a secure confirmation dialog.

- **Transaction History**: A detailed list of all transactions made by the user, including deposits and withdrawals.

- **Password Protection**: Accounts are secured with a password that is required for account deletion, ensuring only authorized users can make sensitive changes.

- **Modern UI**: The user interface is built using **Tkinter**, styled with **ttk** for a modern look and feel.

- **File-based Storage**: All data (accounts and transactions) are stored in simple text-based files, ensuring easy management and retrieval of data.

## Technologies Used

- **Python** (for core functionality)
- **Tkinter** (for the graphical user interface)
- **ttk** (for modern styling)
- **File I/O** (for storing account and transaction data)

## Requirements

To run the project, ensure you have Python 3.x installed. You can download it from [here](https://www.python.org/downloads/).

### Install dependencies:

```bash
pip install tkinter
```

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Lusan-sapkota/Gui-based-banking-system
   ```

2. Run the `index.py` file to start the application.

   ```bash
   python index.py
   ```

3. The application will open in a new window where you can create accounts, perform banking operations, and view transaction history.

## Screenshots
**These are some glimps of system**

![Screenshot 2024-11-13 212320](https://github.com/user-attachments/assets/b77892af-c96a-4c91-9a91-bb17453e8f42)
![Screenshot 2024-11-13 212257](https://github.com/user-attachments/assets/9475a4f8-cd67-4147-96cb-470d1c12b0a2)
![Screenshot 2024-11-13 212440](https://github.com/user-attachments/assets/a8a43fef-35da-4618-b80e-335888973495)



## Future Improvements

- **Database Integration**: Replace file-based storage with a real database like SQLite for more robust data handling.
- **Advanced Security Features**: Implement encryption for storing passwords and sensitive information.
- **2FA**: Implement 2FA system using twillo API.
- **User Authentication**: Add a login system to allow multiple users to access their accounts securely.
- **Mobile Support (last improvement)**: Port the application to mobile platforms using frameworks like Kivy or ionic.
