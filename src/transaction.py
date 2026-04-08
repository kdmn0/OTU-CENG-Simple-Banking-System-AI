"""
Transaction ADT - Stack implementasyonu ile işlem geçmişi yönetimi
Kişi sorumluluğu: Bu modülü en az bakım gerektiren veri yapısı
"""
from datetime import datetime


class Transaction:
    """Bir işlem kaydını temsil eden sınıf"""
    def __init__(self, transaction_type, amount, balance_after, description=""):
        self.timestamp = datetime.now()
        self.type = transaction_type  # 'Deposit', 'Withdraw', 'Transfer'
        self.amount = amount
        self.balance_after = balance_after
        self.description = description
    
    def __str__(self):
        return (f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] "
                f"{self.type}: {self.amount}₺ | "
                f"Balance: {self.balance_after}₺ | {self.description}")


class TransactionStack:
    """
    Stack (LIFO) veri yapısı - işlem geçmişi için
    ADT: Tüm internal gösterim gizlidir (encapsulation)
    """
    def __init__(self):
        self._items = []  # Internal representation - gizli
    
    def push(self, transaction):
        """O(1) - Yeni işlemi stack'e ekle"""
        self._items.append(transaction)
    
    def pop(self):
        """O(1) - Son işlemi çıkar"""
        if not self.is_empty():
            return self._items.pop()
        return None
    
    def peek(self):
        """O(1) - Son işlemi göster (çıkarmadan)"""
        if not self.is_empty():
            return self._items[-1]
        return None
    
    def is_empty(self):
        """O(1) - Stack boş mu?"""
        return len(self._items) == 0
    
    def size(self):
        """O(1) - Stack boyutu"""
        return len(self._items)
    
    def get_all_transactions(self):
        """O(n) - Tüm işlemleri ters sırada döndür (en yeniden en eski)"""
        return list(reversed(self._items))
    
    def clear(self):
        """O(1) - Stack'i temizle"""
        self._items.clear()
