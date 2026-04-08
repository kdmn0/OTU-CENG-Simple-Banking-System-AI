"""
Bank ADT - Tüm hesapları yönetme
Kişi sorumluluğu: Bank yapısı ve hesap yönetim operasyonları
"""
from account import Account


class Bank:
    """
    Banka sistemini temsil eden ADT sınıfı
    Tüm hesapları yönetir ve operasyonları koordine eder
    """
    
    def __init__(self, bank_name):
        self.__bank_name = bank_name
        self.__accounts = {}  # account_number -> Account
        self.__next_account_number = 1001
    
    # Getter methods
    def get_bank_name(self):
        """O(1) - Banka adını döndür"""
        return self.__bank_name
    
    def get_total_accounts(self):
        """O(1) - Toplam hesap sayısını döndür"""
        return len(self.__accounts)
    
    # Account operations
    def create_account(self, holder_name, initial_balance=0):
        """
        O(1) - Yeni hesap oluştur
        Args: holder_name (str), initial_balance (float)
        Returns: account_number (int) or None
        """
        if holder_name == "" or initial_balance < 0:
            return None
        
        account_number = self.__next_account_number
        self.__next_account_number += 1
        
        account = Account(account_number, holder_name, initial_balance)
        self.__accounts[account_number] = account
        return account_number
    
    def get_account(self, account_number):
        """
        O(1) - Hesap numarası ile hesabı getir
        Args: account_number (int)
        Returns: Account object or None
        """
        return self.__accounts.get(account_number)
    
    def account_exists(self, account_number):
        """
        O(1) - Hesap var mı?
        Args: account_number (int)
        Returns: bool
        """
        return account_number in self.__accounts
    
    def deposit(self, account_number, amount):
        """
        O(1) - Hesaba para yatır
        Args: account_number (int), amount (float)
        Returns: bool - başarı durumu
        """
        account = self.__accounts.get(account_number)
        if account is None or not account.is_active():
            return False
        return account.deposit(amount)
    
    def withdraw(self, account_number, amount):
        """
        O(1) - Hesaptan para çek
        Args: account_number (int), amount (float)
        Returns: bool - başarı durumu
        """
        account = self.__accounts.get(account_number)
        if account is None or not account.is_active():
            return False
        return account.withdraw(amount)
    
    def transfer(self, from_account_number, to_account_number, amount):
        """
        O(1) - Para transferi
        Args: from_account_number (int), to_account_number (int), amount (float)
        Returns: bool - başarı durumu
        """
        from_account = self.__accounts.get(from_account_number)
        to_account = self.__accounts.get(to_account_number)
        
        if from_account is None or to_account is None:
            return False
        if not from_account.is_active() or not to_account.is_active():
            return False
        
        # Transfer işlemi
        success = from_account.transfer_out(amount, to_account.get_holder_name())
        if success:
            to_account.transfer_in(amount, from_account.get_holder_name())
            return True
        return False
    
    def get_account_balance(self, account_number):
        """
        O(1) - Hesap bakiyesini getir
        Args: account_number (int)
        Returns: float or None
        """
        account = self.__accounts.get(account_number)
        if account is None:
            return None
        return account.get_balance()
    
    def get_transaction_history(self, account_number):
        """
        O(n) - Hesabın işlem geçmişini getir
        Args: account_number (int)
        Returns: list or None
        """
        account = self.__accounts.get(account_number)
        if account is None:
            return None
        return account.get_transaction_history()
    
    def list_all_accounts(self):
        """
        O(n) - Tüm hesapları listele
        Returns: list of Account objects
        """
        return list(self.__accounts.values())
    
    def get_total_balance(self):
        """
        O(n) - Bankanın toplam bakiyesini hesapla
        Returns: float
        """
        total = sum(account.get_balance() for account in self.__accounts.values())
        return total
    
    def search_accounts_by_holder_name(self, holder_name):
        """
        O(n) - Hesap sahibi adı ile hesap ara
        Args: holder_name (str)
        Returns: list of Account objects
        """
        results = []
        for account in self.__accounts.values():
            if holder_name.lower() in account.get_holder_name().lower():
                results.append(account)
        return results
    
    def __str__(self):
        """Banka bilgilerini string olarak döndür"""
        return (f"Bank: {self.__bank_name} | "
                f"Total Accounts: {len(self.__accounts)} | "
                f"Total Assets: {self.get_total_balance()}₺")
