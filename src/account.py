"""
Account ADT - Bireysel hesap yönetimi
Kişi sorumluluğu: Account tasarımını ve temel işlemlerini yönetme
"""
from transaction import Transaction, TransactionStack


class Account:
    """
    Banka hesabını temsil eden ADT sınıfı
    Internal gösterim tamamen gizlenmiştir (encapsulation)
    """
    
    def __init__(self, account_number, holder_name, initial_balance=0):
        # Private attributes - dış erişim yasaklanmıştır
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = initial_balance
        self.__transaction_history = TransactionStack()
        self.__is_active = True
        
        # İlk bakiye işlemi
        if initial_balance > 0:
            tx = Transaction("Initial Deposit", initial_balance, self.__balance,
                           f"Account opened with {initial_balance}₺")
            self.__transaction_history.push(tx)
    
    # Getter methods (sadece okumalık erişim)
    def get_account_number(self):
        """O(1) - Hesap numarası döndür"""
        return self.__account_number
    
    def get_holder_name(self):
        """O(1) - Hesap sahibinin adı döndür"""
        return self.__holder_name
    
    def get_balance(self):
        """O(1) - Mevcut bakiye döndür"""
        return self.__balance
    
    def is_active(self):
        """O(1) - Hesap aktif mi?"""
        return self.__is_active
    
    # Core operations
    def deposit(self, amount):
        """
        O(1) - Para yatırma işlemi
        Args: amount (float) - yatırılacak tutar
        Returns: bool - başarı durumu
        """
        if amount <= 0:
            return False
        
        self.__balance += amount
        tx = Transaction("Deposit", amount, self.__balance, "Money deposited")
        self.__transaction_history.push(tx)
        return True
    
    def withdraw(self, amount):
        """
        O(1) - Para çekme işlemi
        Args: amount (float) - çekilecek tutar
        Returns: bool - başarı durumu
        """
        if amount <= 0:
            return False
        if amount > self.__balance:
            return False  # Yetersiz bakiye
        
        self.__balance -= amount
        tx = Transaction("Withdraw", amount, self.__balance, "Money withdrawn")
        self.__transaction_history.push(tx)
        return True
    
    def transfer_out(self, amount, recipient_name):
        """
        O(1) - Para gönderme işlemi
        Args: amount (float), recipient_name (str)
        Returns: bool - başarı durumu
        """
        if amount <= 0 or amount > self.__balance:
            return False
        
        self.__balance -= amount
        description = f"Transfer sent to {recipient_name}"
        tx = Transaction("Transfer Out", amount, self.__balance, description)
        self.__transaction_history.push(tx)
        return True
    
    def transfer_in(self, amount, sender_name):
        """
        O(1) - Para alma işlemi
        Args: amount (float), sender_name (str)
        Returns: bool - başarı durumu
        """
        if amount <= 0:
            return False
        
        self.__balance += amount
        description = f"Transfer received from {sender_name}"
        tx = Transaction("Transfer In", amount, self.__balance, description)
        self.__transaction_history.push(tx)
        return True
    
    def get_transaction_history(self):
        """O(n) - Tüm işlem geçmişini döndür"""
        return self.__transaction_history.get_all_transactions()
    
    def get_last_transaction(self):
        """O(1) - Son işlemi döndür"""
        return self.__transaction_history.peek()
    
    def __str__(self):
        """Hesap bilgilerini string olarak döndür"""
        status = "Active" if self.__is_active else "Inactive"
        return (f"Account #{self.__account_number} | "
                f"Holder: {self.__holder_name} | "
                f"Balance: {self.__balance}₺ | "
                f"Status: {status}")
