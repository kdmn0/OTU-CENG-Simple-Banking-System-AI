"""
Main - Console-based Banking System UI
Kişi sorumluluğu: Kullanıcı arayüzü ve interaksiyon
"""
from bank import Bank
import os
import sys


class BankingUI:
    """Banka sistemi için konsol kullanıcı arayüzü"""
    
    def __init__(self):
        self.bank = Bank("Turkish Banking System")
        self.current_user_account = None
    
    def clear_screen(self):
        """Ekranı temizle"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        """Ana menüyü göster"""
        print("\n" + "="*50)
        print("   BANKING SYSTEM - MAIN MENU")
        print("="*50)
        print("1. Create New Account")
        print("2. Login to Account")
        print("3. List All Accounts")
        print("4. Admin View (All Accounts Info)")
        print("5. Exit")
        print("="*50)
    
    def display_account_menu(self):
        """Hesap menüsünü göster"""
        if self.current_user_account is None:
            return
        
        account = self.bank.get_account(self.current_user_account)
        print("\n" + "="*50)
        print(f"   ACCOUNT MENU - {account.get_holder_name()}")
        print("="*50)
        print(f"Account #: {account.get_account_number()}")
        print(f"Balance: {account.get_balance()}₺")
        print("-"*50)
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Transfer Money")
        print("4. View Transaction History")
        print("5. Logout")
        print("="*50)
    
    def create_account(self):
        """Yeni hesap oluştur"""
        print("\n--- CREATE NEW ACCOUNT ---")
        holder_name = input("Enter holder name: ").strip()
        if not holder_name:
            print("❌ Invalid name!")
            return
        
        try:
            initial_balance = float(input("Enter initial balance (default 0): ") or 0)
            if initial_balance < 0:
                print("❌ Balance cannot be negative!")
                return
        except ValueError:
            print("❌ Invalid amount!")
            return
        
        account_number = self.bank.create_account(holder_name, initial_balance)
        if account_number:
            print(f"✓ Account created! Account #: {account_number}")
        else:
            print("❌ Failed to create account!")
    
    def login_account(self):
        """Hesaba giriş yap"""
        print("\n--- LOGIN ---")
        try:
            account_number = int(input("Enter account number: "))
            if self.bank.account_exists(account_number):
                self.current_user_account = account_number
                account = self.bank.get_account(account_number)
                print(f"✓ Welcome {account.get_holder_name()}!")
                return True
            else:
                print("❌ Account not found!")
                return False
        except ValueError:
            print("❌ Invalid account number!")
            return False
    
    def list_all_accounts(self):
        """Tüm hesapları listele"""
        print("\n--- ALL ACCOUNTS ---")
        accounts = self.bank.list_all_accounts()
        if not accounts:
            print("No accounts in the system.")
            return
        
        for account in accounts:
            print(account)
    
    def admin_view(self):
        """Admin görünümü - detaylı bilgiler"""
        print("\n--- ADMIN VIEW ---")
        print(self.bank)
        print("\nAccount Details:")
        accounts = self.bank.list_all_accounts()
        for i, account in enumerate(accounts, 1):
            print(f"\n{i}. {account}")
            transactions = account.get_transaction_history()
            if transactions:
                print("   Recent Transactions:")
                for tx in transactions[-3:]:  # Son 3 işlem
                    print(f"   - {tx}")
    
    def deposit_money(self):
        """Para yatır"""
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("❌ Amount must be positive!")
                return
            
            if self.bank.deposit(self.current_user_account, amount):
                account = self.bank.get_account(self.current_user_account)
                print(f"✓ Deposited {amount}₺")
                print(f"new balance: {account.get_balance()}₺")
            else:
                print("❌ Deposit failed!")
        except ValueError:
            print("❌ Invalid amount!")
    
    def withdraw_money(self):
        """Para çek"""
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("❌ Amount must be positive!")
                return
            
            if self.bank.withdraw(self.current_user_account, amount):
                account = self.bank.get_account(self.current_user_account)
                print(f"✓ Withdrawn {amount}₺")
                print(f"New balance: {account.get_balance()}₺")
            else:
                print("❌ Insufficient balance or invalid amount!")
        except ValueError:
            print("❌ Invalid amount!")
    
    def transfer_money(self):
        """Para transferi yap"""
        print("\n--- TRANSFER MONEY ---")
        try:
            to_account = int(input("Enter recipient account number: "))
            if not self.bank.account_exists(to_account):
                print("❌ Recipient account not found!")
                return
            
            amount = float(input("Enter amount to transfer: "))
            if amount <= 0:
                print("❌ Amount must be positive!")
                return
            
            if self.bank.transfer(self.current_user_account, to_account, amount):
                print(f"✓ Transferred {amount}₺ successfully!")
                from_account = self.bank.get_account(self.current_user_account)
                print(f"Your new balance: {from_account.get_balance()}₺")
            else:
                print("❌ Transfer failed! Check balance and account.")
        except ValueError:
            print("❌ Invalid input!")
    
    def view_transaction_history(self):
        """İşlem geçmişini göster"""
        print("\n--- TRANSACTION HISTORY ---")
        transactions = self.bank.get_transaction_history(self.current_user_account)
        
        if not transactions:
            print("No transactions yet.")
            return
        
        for tx in transactions:
            print(tx)
    
    def run(self):
        """Uygulamayı çalıştır"""
        while True:
            if self.current_user_account is None:
                self.clear_screen()
                self.display_menu()
                choice = input("Enter choice: ").strip()
                
                if choice == '1':
                    self.create_account()
                elif choice == '2':
                    self.login_account()
                elif choice == '3':
                    self.list_all_accounts()
                elif choice == '4':
                    self.admin_view()
                elif choice == '5':
                    print("Goodbye!")
                    break
                else:
                    print("❌ Invalid choice!")
                
                input("\nPress Enter to continue...")
            
            else:
                self.clear_screen()
                self.display_account_menu()
                choice = input("Enter choice: ").strip()
                
                if choice == '1':
                    self.deposit_money()
                elif choice == '2':
                    self.withdraw_money()
                elif choice == '3':
                    self.transfer_money()
                elif choice == '4':
                    self.view_transaction_history()
                elif choice == '5':
                    print("Logged out!")
                    self.current_user_account = None
                else:
                    print("❌ Invalid choice!")
                
                if self.current_user_account is not None:
                    input("\nPress Enter to continue...")


if __name__ == "__main__":
    ui = BankingUI()
    ui.run()
