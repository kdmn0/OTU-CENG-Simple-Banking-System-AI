# Banking System Project - 3 Person Team Assignment Guide

## Project: CENG110 - Simple Banking System (Project 6)

---

## Team Assignment Distribution

### 👤 Person 1: ADT Design & Data Structures Expert - Yiğit
**Responsibility Level**: 30%

#### **Main Tasks**:
1. **Transaction.py Module** (Week 1)
   - Design `Transaction` class
   - Implement `TransactionStack` class using Stack (LIFO) data structure
   - Add push(), pop(), peek(), is_empty() methods
   - Ensure O(1) operations for stack basics
   - Write docstrings with Big-O complexity

2. **Account.py Module** (Week 1-2)
   - Design `Account` ADT with private attributes
   - Use name mangling (\_\_attribute) for encapsulation
   - Implement getter methods (non-mutating)
   - Implement core operations:
     - `deposit(amount)` - O(1)
     - `withdraw(amount)` - O(1)
     - `transfer_out(amount)` - O(1)
     - `transfer_in(amount)` - O(1)
   - Integrate TransactionStack for history
   - Add input validation

#### **Deliverables**:
- ✓ src/transaction.py (complete & tested)
- ✓ src/account.py (complete & tested)
- ✓ Basic unit tests for single account operations

#### **Key Concepts**:
- Abstract Data Types (ADT)
- Encapsulation & Data Hiding
- Stack implementation (LIFO)
- Time Complexity Analysis

---

### 👤 Person 2: Bank Management System Developer - Yusuf
**Responsibility Level**: 35%

#### **Main Tasks**:
1. **Bank.py Module** (Week 2-3)
   - Design `Bank` ADT as account collection manager
   - Use dictionary for O(1) account lookup by account number
   - Implement account lifecycle:
     - `create_account(name, balance)` - O(1)
     - `get_account(account_number)` - O(1)
     - `account_exists(account_number)` - O(1)
   - Implement banking operations:
     - `deposit(account_num, amount)` - O(1)
     - `withdraw(account_num, amount)` - O(1)
     - `transfer(from_acc, to_acc, amount)` - O(1)
     - `get_account_balance(account_num)` - O(1)
     - `get_transaction_history(account_num)` - O(n)
   - Implement reporting functions:
     - `list_all_accounts()` - O(n)
     - `get_total_balance()` - O(n)
     - `search_accounts_by_holder_name(name)` - O(n)
   - Add comprehensive error handling

2. **System Coordination** (Week 3)
   - Ensure consistency between Account and Bank operations
   - Validate all inputs before operations
   - Maintain data integrity across operations
   - Handle edge cases (negative amounts, non-existent accounts, etc.)

#### **Deliverables**:
- ✓ src/bank.py (complete & tested)
- ✓ Integration tests for multi-account operations
- ✓ Error handling validation

#### **Key Concepts**:
- Collection management (dictionary as internal structure)
- O(1) lookup operations
- Multi-object coordination
- Transaction consistency

---

### 👤 Person 3: UI, Testing & Documentation - Ebu
**Responsibility Level**: 35%

#### **Main Tasks**:
1. **Console UI Implementation** (Week 1-2)
   - Create `BankingUI` class in src/main.py
   - Main menu interface
   - Account login system
   - Account menu (deposit, withdraw, transfer, history)
   - Admin view (bank statistics)
   - User-friendly error messages
   - Input validation at UI level

2. **Comprehensive Test Suite** (Week 2-3)
   - Write minimum 5 test cases in tests/test_banking.py:
     - ✓ **Test 1: Normal Case** - Account creation with valid inputs
     - ✓ **Test 2: Edge Case** - Empty system (no accounts)
     - ✓ **Test 3: Invalid Input** - Negative amounts rejected
     - ✓ **Test 4: Edge Case** - Insufficient balance
     - ✓ **Test 5: Complex Scenario** - Multiple operations
     - ✓ **Test 6: BONUS** - Transaction history (Stack LIFO)
     - ✓ **Test 7: BONUS** - Big-O Complexity Analysis
   
   - Test categories:
     - Normal cases (happy path)
     - Edge cases (empty structure, boundary values)
     - Invalid input cases
     - Complex scenarios (multiple operations)
     - Big-O analysis documentation

3. **Documentation & Report** (Week 3)
   - Create README.md with:
     - Project overview
     - Team structure & responsibilities
     - Feature list
     - Algorithm complexity table
     - Execution instructions
   - Prepare 3-5 page project report including:
     - ADT design explanation
     - Data structure justification (why Stack?)
     - Big-O analysis with proofs
     - Test case documentation
     - Code organization explanation

#### **Deliverables**:
- ✓ src/main.py (complete console UI)
- ✓ tests/test_banking.py (7+ test cases)
- ✓ README.md (project documentation)
- ✓ Project Report (3-5 pages)
- ✓ ASSIGNMENT_NOTES.md (This file)

#### **Key Concepts**:
- Console UI design
- Test case design (normal, edge, invalid, complex)
- Big-O complexity analysis
- Technical documentation

---

## Timeline (3 Weeks)

### **Week 1**:
- **Person 1**: Implement transaction.py and basic account.py
- **Person 2**: Wait for Account module completion, then start bank.py design
- **Person 3**: Design test cases structure, prepare UI mockups

### **Week 2**:
- **Person 1**: Complete account.py and unit tests → Review
- **Person 2**: Implement bank.py, integration testing
- **Person 3**: Implement main UI, write test cases

### **Week 3**:
- **Person 1**: Code review, optimization, documentation
- **Person 2**: Testing & bug fixes, final validation
- **Person 3**: Final testing, documentation, prepare report

---

## Code Structure Reference

```
BankingSystem/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── transaction.py       # ← Person 1
│   ├── account.py           # ← Person 1
│   ├── bank.py              # ← Person 2
│   └── main.py              # ← Person 3 (UI)
├── tests/
│   └── test_banking.py      # ← Person 3 (Tests)
├── README.md                # ← Person 3 (Doc)
├── ASSIGNMENT_NOTES.md      # ← Team (This file)
└── PROJECT_REPORT.md        # ← Person 3 (Report)
```

---

## Grading Rubric (100 Points)

| Criterion | Points | Person(s) |
|-----------|--------|-----------|
| ADT Design & Encapsulation | 25 | Person 1, 2 |
| Correct Functionality | 25 | Person 2, 3 |
| Algorithmic Analysis (Big-O) | 20 | Person 1, 3 |
| Modularity & Code Organization | 15 | All |
| Testing Quality (5+ test cases) | 10 | Person 3 |
| Documentation Quality | 5 | Person 3 |

---

## Collaboration Guidelines

### ✅ DO's:
- Commit code frequently to git
- Write clear docstrings for all functions
- Comment complex logic
- Test your own module before integration
- Use Python naming conventions (snake_case for functions)
- Follow the provided architecture

### ❌ DON'Ts:
- Don't modify other person's ADT classes
- Don't skip error handling
- Don't use global variables
- Don't hardcode values
- Don't skip tests

---

## Integration Checklist

Before final submission:

- [ ] Person 1: transaction.py and account.py are complete
- [ ] Person 2: bank.py is complete and integrated
- [ ] Person 3: All tests pass (minimum 5, with 7 implemented)
- [ ] All code has docstrings
- [ ] Big-O analysis documented
- [ ] README.md is complete
- [ ] Project report is written (3-5 pages)
- [ ] UI works without errors
- [ ] All test cases pass

---

## Communication Points

1. **After Week 1**: Person 1 shows completed ADT modules to Person 2
2. **Mid-Week 2**: Integrate bank.py with ADTs, test together
3. **End of Week 2**: Person 3 presents test suite, validate all operations
4. **Week 3**: Final review, documentation, report writing

---

## Success Criteria

✓ All 5 mandatory operations work correctly  
✓ Stack data structure properly implemented  
✓ All operations have correct Big-O complexity  
✓ Minimum 5 test cases pass  
✓ Code is modular and well-organized  
✓ Documentation is complete  
✓ Project report explains all design decisions  

---

**Project Created**: March 30, 2026  
**Expected Completion**: Week 3  
**Contact**: Team Lead / Instructor
