# tests for the Account class
from bank import Account, BalanceError
import pytest

def test_default_account_balance_is_0():
    a = Account()
    assert a.balance == 0

def test_account_with_initial_balance():
    a = Account(10)
    assert a.balance == 10

def test_balance_after_deposit():
    a = Account(10)
    a.deposit(10)
    assert a.balance == 20

def test_balance_after_transfer():
    a = Account(10)
    a.transfer(5)
    assert a.balance == 5

def test_exception_insufficient_funds():
    a = Account(10)
    with pytest.raises(BalanceError):
        a.transfer(15)