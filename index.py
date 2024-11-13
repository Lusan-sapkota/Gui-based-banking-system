import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.filedialog as filedialog
import pickle
import os
import pathlib
from datetime import datetime
import random
import re
from tkinter import simpledialog

class Account:
    def __init__(self, accNo, name, accType, deposit, phone=None, email=None, document_path=None, password=None):
        self.accNo = accNo
        self.name = name
        self.accType = accType
        self.deposit = deposit
        self.phone = phone
        self.email = email
        self.document_path = document_path
        self.password = password  # Store password

# File path
ACCOUNTS_FILE_PATH = "accounts.dat"

# Write a new account to the file
def writeAccountsFile(account):
    # Read existing accounts
    accounts = readAccountsFile()
    
    # Append the new account
    accounts.append(account)
    
    # Save the updated list back to the file
    saveAccountsFile(accounts)

# Read all accounts from the file
def readAccountsFile():
    if not os.path.exists(ACCOUNTS_FILE_PATH):  # Check if file exists
        return []  # Return an empty list if the file doesn't exist

    try:
        with open(ACCOUNTS_FILE_PATH, "rb") as infile:
            accounts = pickle.load(infile)
            return accounts
    except (EOFError, pickle.UnpicklingError):  # Handle both EOF and invalid pickle errors
        return []  # Return an empty list if the file is corrupted or empty

# Save the list of accounts to the file
def saveAccountsFile(accounts):
    with open(ACCOUNTS_FILE_PATH, "wb") as outfile:
        pickle.dump(accounts, outfile)

class ModernBankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Modern Bank Management System")
        self.geometry("1000x650")
        self.configure(bg="#1e1e2e")
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.setup_styles()

        self.main_frame = ttk.Frame(self, padding=20)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.show_home()

    def setup_styles(self):
        self.style.configure("TFrame", background="#1e1e2e")
        self.style.configure("TButton", background="#3e3e5e", foreground="#ffffff", font=("Arial", 12), padding=10)
        self.style.map("TButton", background=[("active", "#5e5e7e")])
        self.style.configure("TLabel", background="#1e1e2e", foreground="#ffffff", font=("Arial", 12))
        self.style.configure("TEntry", font=("Arial", 12), padding=5)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_frame()

        # Title Label
        ttk.Label(self.main_frame, text="Welcome to Modern Bank System", font=("Arial", 18, "bold")).pack(pady=30)

        # Frame for Buttons
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        # Configure Grid Layout for Equal Spacing
        for i in range(3):
            button_frame.columnconfigure(i, weight=1)

        # Button Configuration (Text, Command, Background Color)
        buttons = [
            ("Create Account", self.show_create_account, "#4CAF50"), # Green
            ("View Accounts", self.show_view_accounts, "#1b1b1b"),
            ("Deposit", self.show_deposit, "#1b1b1b"),                
            ("Withdraw", self.show_withdraw, "#1b1b1b"),              
            ("Transaction History", self.show_transactions, "#1b1b1b"),
            ("Exit", self.quit, "#F44336"),                          # Red
        ]

        # Create Buttons with Custom Colors
        for index, (text, command, color) in enumerate(buttons):
            row = index // 3
            col = index % 3
            button = tk.Button(
                button_frame, text=text, command=command,
                bg=color, fg="white", font=("Arial", 12, "bold"),
                activebackground="#D3D3D3", activeforeground="black"
            )
            button.grid(row=row, column=col, padx=20, pady=15, ipadx=20, ipady=10, sticky="nsew")

        # Ensure Rows Expand Equally
        for row in range((len(buttons) + 2) // 3):
            button_frame.rowconfigure(row, weight=1)


    def show_back_button(self):
        # Clear any existing back button
        for widget in self.main_frame.pack_slaves():
            if isinstance(widget, ttk.Button) and widget.cget("text") == "Back":
                widget.destroy()

        # Create a new back button with an arrow symbol and place it at the top left
        back_button = ttk.Button(self.main_frame, text="← Go Back", command=self.show_home)
        back_button.pack(anchor=tk.NW, padx=10, pady=10)


    def show_create_account(self):
        self.clear_frame()

        # Back Button at the top left
        back_button = ttk.Button(self.main_frame, text="← Back", command=self.show_home)
        back_button.pack(side=tk.LEFT, anchor="nw", padx=20, pady=10)

        # Title Label
        ttk.Label(self.main_frame, text="Create New Account", font=("Arial", 20, "bold")).pack(pady=20)

        # Frames for Layout
        form_frame = ttk.Frame(self.main_frame)
        form_frame.pack(side=tk.LEFT, padx=40, pady=10, fill=tk.BOTH, expand=True)

        instruction_frame = ttk.Frame(self.main_frame)
        instruction_frame.pack(side=tk.RIGHT, padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Generate Unique 5-digit Account Number
        def generate_account_number():
            accounts = readAccountsFile()
            existing_numbers = {account.accNo for account in accounts}
            while True:
                acc_no = random.randint(10000, 99999)
                if acc_no not in existing_numbers:
                    return acc_no

        # Automatically Generated Account Number
        account_number = generate_account_number()
        ttk.Label(form_frame, text=f"Account Number: {account_number}", font=("Arial", 12, "bold")).pack(pady=5)

        # Account Holder Name
        ttk.Label(form_frame, text="Account Holder Name").pack(pady=5)
        name_entry = ttk.Entry(form_frame)
        name_entry.pack(pady=10, fill=tk.X)

        # Phone Number
        ttk.Label(form_frame, text="Phone Number").pack(pady=5)
        phone_entry = ttk.Entry(form_frame)
        phone_entry.pack(pady=10, fill=tk.X)

        # Email
        ttk.Label(form_frame, text="Email").pack(pady=5)
        mail_entry = ttk.Entry(form_frame)
        mail_entry.pack(pady=10, fill=tk.X)

        # Password Field
        ttk.Label(form_frame, text="Password").pack(pady=5)
        password_entry = ttk.Entry(form_frame, show="*")  # Hide password input
        password_entry.pack(pady=10, fill=tk.X)

        # Account Type Dropdown
        acc_type_var = tk.StringVar(value="Saving")
        ttk.Label(form_frame, text="Account Type").pack(pady=5)
        acc_type_dropdown = ttk.Combobox(form_frame, textvariable=acc_type_var, values=["Saving", "Current"])
        acc_type_dropdown.pack(pady=10, fill=tk.X)

        # Initial Deposit
        ttk.Label(form_frame, text="Initial Deposit (>= 0)").pack(pady=5)
        deposit_entry = ttk.Entry(form_frame)
        deposit_entry.pack(pady=10, fill=tk.X)

        # Document Upload
        doc_path_var = tk.StringVar()

        def on_enter_name(event):
            phone_entry.focus_set()  # Focus on the phone entry

        def on_enter_phone(event):
            mail_entry.focus_set()  # Focus on the email entry

        def on_enter_email(event):
            password_entry.focus_set()  # Focus on the password entry

        def on_enter_password(event):
            deposit_entry.focus_set()  # Focus on the deposit entry

        def on_enter_deposit(event):
            save_account()  # Trigger save_account when enter is pressed

        # Add key bindings
        name_entry.bind("<Return>", on_enter_name)
        phone_entry.bind("<Return>", on_enter_phone)
        mail_entry.bind("<Return>", on_enter_email)
        password_entry.bind("<Return>", on_enter_password)
        deposit_entry.bind("<Return>", on_enter_deposit)

        def browse_document():
            file_path = filedialog.askopenfilename(
                title="Select Document",
                filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
            )
            if file_path:
                doc_path_var.set(file_path)
                doc_label.config(text=f"Selected: {file_path.split('/')[-1]}", foreground="green")

        ttk.Label(form_frame, text="Upload Document (PDF)").pack(pady=5)
        ttk.Button(form_frame, text="Browse", command=browse_document).pack(pady=5)
        doc_label = ttk.Label(form_frame, text="No document selected", foreground="gray")
        doc_label.pack(pady=5)

        # Save Account Function
        def save_account():
            try:
                name = name_entry.get()
                phone = phone_entry.get()
                mail = mail_entry.get()
                password = password_entry.get()
                acc_type = acc_type_var.get()
                deposit = int(deposit_entry.get()) if deposit_entry.get() else 0
                document_path = doc_path_var.get()

                if not name or not phone.isdigit() or len(phone) != 10:
                    raise ValueError("Invalid phone number.")
                if not document_path:
                    raise ValueError("Document not uploaded.")
                if not password:
                    raise ValueError("Password cannot be empty.")

                email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                if not re.match(email_pattern, mail):
                    raise ValueError("Invalid email address.")

                # Create new account with auto-generated account number
                new_account = Account(account_number, name, acc_type, deposit)
                new_account.phone = phone
                new_account.email = mail
                new_account.password = password  # Store password securely (consider hashing)
                new_account.document_path = document_path

                writeAccountsFile(new_account)

                messagebox.showinfo("Success", f"Account created successfully!\nAccount Number: {account_number}")
                self.show_home()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        # Save Button
        ttk.Button(form_frame, text="Save Account", command=save_account, width=20).pack(pady=15)

        # Instructions Panel
        instructions = (
            "Instructions:\n\n\n"
            "1. The account number is automatically generated and unique.\n\n"
            "2. Enter the account holder's full name.\n\n"
            "3. Enter a valid 10-digit phone number.\n\n"
            "4. Enter a valid email address (e.g., example@gmail.com).\n\n"
            "5. Enter a valid Password which will be later used as a security measure while deleting the account.\n\n"
            "6. Select the account type (Saving or Current).\n\n"
            "7. Enter an initial deposit amount (0 or more).\n\n"
            "8. Upload a document (PDF format preferred) for verification.\n\n"
            "9. Click 'Save Account' to create the account."
        )

        ttk.Label(instruction_frame, text=instructions, justify=tk.LEFT, wraplength=300, font=("Arial", 12)).pack(pady=10)


    def show_view_accounts(self):
        self.clear_frame()
        accounts = readAccountsFile()
        if not accounts:
            messagebox.showinfo("Info", "No accounts found.")
            self.show_home()
            return

        tree = ttk.Treeview(self.main_frame, columns=("AccNo", "Name", "Phone", "Gmail", "Type", "Deposit", "Document"), show="headings")
        tree.heading("AccNo", text="Account No")
        tree.heading("Name", text="Name")
        tree.heading("Phone", text="Phone")
        tree.heading("Gmail", text="Gmail")
        tree.heading("Type", text="Type")
        tree.heading("Deposit", text="Deposit")
        tree.heading("Document", text="Document")

        for account in accounts:
            doc_name = account.document_path.split('/')[-1] if hasattr(account, 'document_path') else "N/A"
            tree.insert("", tk.END, values=(account.accNo, account.name, getattr(account, 'phone', 'N/A'), account.accType, account.email, account.deposit, doc_name))

        tree.pack(expand=True, fill=tk.BOTH, pady=10)

        # This function will be triggered when Enter is pressed
        def delete_on_enter(event):
            selected_item = tree.selection()  # Get the selected item in the treeview
            if selected_item:
                account = tree.item(selected_item[0])['values']  # Get the values of the selected account
                # Create an account object or pass the account data as needed
                selected_account = Account(*account)  # Assuming you have an Account class, adjust as needed
                self.show_delete_confirmation(selected_account)  # Pass the account to the delete confirmation

        tree.bind("<Return>", delete_on_enter)

        # Creating a frame for the "Delete" and "Back" buttons at the bottom
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(side=tk.BOTTOM, pady=20, fill=tk.X)

        back_button = ttk.Button(button_frame, text="← Back", command=self.show_home)
        back_button.pack(side=tk.LEFT, padx=20)

        # Pass the account to the delete confirmation
        delete_button = ttk.Button(button_frame, text="Delete Account", command=lambda: self.show_delete_confirmation(account))
        delete_button.pack(side=tk.RIGHT, padx=20)

    def show_delete_confirmation(self, account):
        # Create a new window to ask for the password
        password_window = tk.Toplevel(self.main_frame)
        password_window.title("Enter Password")

        # Set modern styling
        password_window.geometry("500x250")  # Set the size for a neat look
        password_window.config(padx=20, pady=20)  # Add padding around the window

        # Title Label
        ttk.Label(password_window, text="Please enter your password to delete the account", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=15)

        # Password Entry
        ttk.Label(password_window, text="Password:", font=("Arial", 12)).grid(row=1, column=0, pady=5, sticky="e")
        password_entry = ttk.Entry(password_window, show="*", width=25, font=("Arial", 12))
        password_entry.grid(row=1, column=1, pady=10)

        def verify_password():
            entered_password = password_entry.get()
            if entered_password == account.password:  # Use the password from the selected account
                # Delete account logic
                accounts = readAccountsFile()
                accounts = [acc for acc in accounts if acc.accNo != account.accNo]  # Remove account
                saveAccountsFile(accounts)
                messagebox.showinfo("Success", "Account deleted successfully!")
                password_window.destroy()
                self.show_view_accounts()  # Refresh the account list
            else:
                messagebox.showerror("Error", "Incorrect password.")
                password_window.destroy()

        # Buttons to confirm or cancel the deletion
        confirm_button = ttk.Button(password_window, text="Delete Account", command=verify_password, width=15)
        cancel_button = ttk.Button(password_window, text="Cancel", command=password_window.destroy, width=15)

        def on_enter(event):
            confirm_button.invoke()  # Trigger the button's command (verify_password)

        # Bind the Enter key to the button press
        password_window.bind("<Return>", on_enter)

        # Place buttons in the last row, across two columns for proper spacing
        confirm_button.grid(row=3, column=0, padx=10, pady=10)
        cancel_button.grid(row=3, column=1, padx=10, pady=10)

        # Focus the password entry field so the user can type immediately
        password_entry.focus()


    def show_transactions(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Transaction History", font=("Arial", 16)).pack(pady=20)

        acc_no_entry = ttk.Entry(self.main_frame)
        acc_no_entry.pack(pady=10, fill=tk.X)
        ttk.Label(self.main_frame, text="Enter Account Number").pack(pady=5)

        def display_history():
            try:
                acc_no = int(acc_no_entry.get())
                accounts = readAccountsFile()

                for account in accounts:
                    if account.accNo == acc_no:
                        if not account.transactions:
                            messagebox.showinfo("Info", "No transactions found for this account.")
                            return

                        history_frame = ttk.Frame(self.main_frame)
                        history_frame.pack(expand=True, fill=tk.BOTH)

                        scrollbar = ttk.Scrollbar(history_frame)
                        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

                        listbox = tk.Listbox(history_frame, yscrollcommand=scrollbar.set, width=80, height=15)
                        for transaction in account.transactions:
                            listbox.insert(tk.END, transaction)
                        listbox.pack(side=tk.LEFT, fill=tk.BOTH)

                        scrollbar.config(command=listbox.yview)
                        return

                messagebox.showerror("Error", "Account not found.")
            except ValueError:
                messagebox.showerror("Error", "Invalid account number.")

        ttk.Button(self.main_frame, text="Show History", command=display_history, width=20).pack(pady=15)
        self.show_back_button()

    def show_deposit(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Deposit Money", font=("Arial", 16)).pack(pady=20)

        acc_no_entry = ttk.Entry(self.main_frame)
        acc_no_entry.pack(pady=10, fill=tk.X)
        ttk.Label(self.main_frame, text="Account Number").pack(pady=5)

        amount_entry = ttk.Entry(self.main_frame)
        amount_entry.pack(pady=10, fill=tk.X)
        ttk.Label(self.main_frame, text="Amount to Deposit").pack(pady=5)

        def accno_deposit_on_enter(event):
            amount_entry.focus_set()

        def amt_deposit_on_enter(event):
            deposit()  # Trigger deposit when Enter key is pressed

        acc_no_entry.bind("<Return>", accno_deposit_on_enter)
        amount_entry.bind("<Return>", amt_deposit_on_enter)

        def deposit():
            try:
                acc_no = int(acc_no_entry.get())
                amount = int(amount_entry.get())
                accounts = readAccountsFile()

                for account in accounts:
                    if account.accNo == acc_no:
                        account.deposit += amount
                        account.transactions.append(f"Deposited: {amount} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                        saveAccountsFile(accounts)
                        messagebox.showinfo("Success", "Amount deposited successfully!")
                        return
                messagebox.showerror("Error", "Account not found.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input.")

        ttk.Button(self.main_frame, text="Deposit", command=deposit, width=20).pack(pady=15)
        self.show_back_button()

    def show_withdraw(self):
        self.clear_frame()
        ttk.Label(self.main_frame, text="Withdraw Money", font=("Arial", 16)).pack(pady=20)

        acc_no_entry = ttk.Entry(self.main_frame)
        acc_no_entry.pack(pady=10, fill=tk.X)
        ttk.Label(self.main_frame, text="Account Number").pack(pady=5)

        amount_entry = ttk.Entry(self.main_frame)
        amount_entry.pack(pady=10, fill=tk.X)
        ttk.Label(self.main_frame, text="Amount to Withdraw").pack(pady=5)

        def acc_withdraw_on_enter(event):
            amount_entry.focus_set()

        def amt_withdraw_on_enter(event):
            withdraw()

        acc_no_entry.bind("<Return>", acc_withdraw_on_enter)
        amount_entry.bind("<Return>", amt_withdraw_on_enter)

        def withdraw():
            try:
                acc_no = int(acc_no_entry.get())
                amount = int(amount_entry.get())
                accounts = readAccountsFile()

                for account in accounts:
                    if account.accNo == acc_no:
                        if account.deposit < amount:
                            messagebox.showerror("Error", "Insufficient balance.")
                            return
                        account.deposit -= amount
                        account.transactions.append(f"Withdrew: {amount} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                        saveAccountsFile(accounts)
                        messagebox.showinfo("Success", "Amount withdrawn successfully!")
                        return
                messagebox.showerror("Error", "Account not found.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input.")

        ttk.Button(self.main_frame, text="Withdraw", command=withdraw, width=20).pack(pady=15)
        self.show_back_button()

if __name__ == "__main__":
    app = ModernBankApp()
    app.mainloop()
