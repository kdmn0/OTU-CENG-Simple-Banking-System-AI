# Simple Banking System - CENG110 Project 6

## Project Overview (Prepared by AI)
Modular Python-based console banking system with ADT design for transaction management.

## Team Structure (3 People - Minimum Requirements)

### Person 1: ADT Design & Data Structures
- **File**: `src/transaction.py`, `src/account.py`
- **Responsibilities**:
  - Design Account ADT (private attributes, encapsulation)
  - Implement TransactionStack using Stack (LIFO)
  - Handle basic account operations (deposit, withdraw)
  - Ensure data integrity & validation

### Person 2: Bank Management System
- **File**: `src/bank.py`
- **Responsibilities**:
  - Design Bank ADT (account collection management)
  - Implement bank-level operations (create account, transfer)
  - Handle account lookup and searches
  - Coordinate multi-account operations

### Person 3: UI & Testing
- **File**: `src/main.py`, `tests/test_banking.py`
- **Responsibilities**:
  - Console-based user interface
  - Write test cases (minimum 5)
  - Documentation & reporting
  - Big-O analysis testing

---

## Project Structure

```
BankingSystem/
├── src/
│   ├── transaction.py    # Transaction ADT & Stack data structure
│   ├── account.py        # Account ADT
│   ├── bank.py           # Bank ADT
│   └── main.py           # Console UI
└── tests/
    └── test_banking.py   # Test suite (6+ test cases)
```

---

## Key Features

### 1. Abstract Data Types (ADTs)
- **Account ADT**: Manages individual accounts with encapsulation
- **Bank ADT**: Manages multiple accounts and operations
- **TransactionStack ADT**: Stack-based transaction history (LIFO)

### 2. Mandatory Operations
✓ Create account  
✓ Deposit money  
✓ Withdraw money  
✓ Transfer money between accounts  
✓ Transaction history  

### 3. Data Structure: Stack
- Used for **Transaction History** (Stack - LIFO)
- Most recent transaction on top
- O(1) push/pop operations

---

## Algorithm Complexity Analysis (Big-O)

| Operation | Complexity | Reason |
|-----------|-----------|--------|
| Create Account | O(1) | Hash table insertion |
| Deposit | O(1) | Balance update + stack push |
| Withdraw | O(1) | Balance update + stack push |
| Transfer | O(1) | Two updates + stack operations |
| Get Balance | O(1) | Direct dictionary lookup |
| Get Last Transaction | O(1) | Stack peek (top element) |
| Get Transaction History | O(n) | Stack traversal (n=transaction count) |
| List All Accounts | O(n) | Dictionary iteration (n=account count) |
| Get Total Balance | O(n) | Sum operation over all accounts |
| Search by Holder Name | O(n) | Linear search through accounts |

---

## Running the Application

### 1. Run Main Program
```bash
python src/main.py
```

### 2. Run Test Suite
```bash
python tests/test_banking.py
```

---

## Test Cases (Minimum 5 Required)

### Test 1: Normal Case - Account Creation
- Create account with positive balance
- Verify account number assignment
- Verify holder name and balance

### Test 2: Edge Case - Empty System
- Empty bank system has 0 accounts
- Total balance is 0
- Non-existent account returns None

### Test 3: Invalid Input - Negative Amount
- Reject negative deposits
- Verify balance unchanged
- System state remains valid

### Test 4: Edge Case - Insufficient Balance
- Reject withdrawal exceeding balance
- Balance remains unchanged
- No transaction recorded

### Test 5: Complex Scenario - Multiple Operations
- Create multiple accounts
- Perform deposit, transfer, withdrawal
- Verify all balances correct
- Check total bank balance

### Test 6: Transaction History (Stack - LIFO)
- Record all transactions
- Retrieve in LIFO order
- Verify last transaction

### Test 7: Big-O Analysis
- Document time complexity for all operations
- Explain reasoning for each

---

## Features Implemented

### Encapsulation
- Private attributes (\_\_attribute)
- Getter methods for safe access
- No direct manipulation of internal data

### Data Validation
- Check positive amounts
- Verify account existence
- Validate sufficient balance
- Prevent duplicate operations

### User Interface
- Menu-driven console interface
- Account login system
- Transaction viewing
- Admin view (view all accounts)

### Error Handling
- Invalid input validation
- Account existence checks
- Balance verification
- Graceful error messages

---

## Grading Rubric (100 Points)

- **ADT Design & Encapsulation** (25%): Proper abstraction and private attributes
- **Correct Functionality** (25%): All operations work correctly
- **Algorithmic Analysis** (20%): Big-O complexity documented
- **Modularity & Code Organization** (15%): Clean, organized code structure
- **Testing Quality** (10%): Comprehensive test cases
- **Documentation** (5%): Code comments and README

---

## Instructions for Execution

1. **Ensure Python 3.x is installed**
2. **Navigate to project directory**
3. **Run main program**: `python src/main.py`
4. **Run tests**: `python tests/test_banking.py`

---

## Notes for Team

- Each person should commit their own module
- All files must have clear docstrings
- Follow Python naming conventions
- Comment all complex logic
- Test frequently during development

Good luck with your project! 🚀
