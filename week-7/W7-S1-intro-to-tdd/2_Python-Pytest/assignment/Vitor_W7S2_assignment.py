# start writing code from here
import pytest

class BankAccount():
    def __init__(self):
        self.__balance = 0
        
    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("You can only deposit numerical amounts")
        elif amount <= 0:
            raise ValueError("You need to deposit something...")
        elif amount > 1_000_000:
            raise ValueError("Max deposit is a million at a time")
        self.__balance += amount
        return self.__balance
        
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("You can only withdraw numerical amounts")
        elif amount <= 0:
            raise ValueError("You need to withdraw something...")
        elif amount > 1_000_000:
            raise ValueError("Max withdraw is a million at a time")
        elif amount > self.__balance:
            raise ValueError("You don't have enough")
        self.__balance -= amount
        return self.__balance
    
    def get_balance(self):
        return self.__balance

    
@pytest.fixture
def small_account():
    account = BankAccount()
    account.deposit(100)
    yield account
    del account # deletes the bank account
    
@pytest.fixture
def large_account():
    account = BankAccount()
    account.deposit(1_000_000)
    # second deposit is needed as max deposit is a million and we'll test for trying to withdraw more than a million at a time as it would fail on different test
    account.deposit(1_000_000)
    yield account
    del account # deletes the bank account

# use the small_account fixture in our TestDeposit class (must be included in quotations marks so it's visible inside the class)
@pytest.mark.usefixtures("small_account")
class TestDeposit():
    
    @pytest.mark.parametrize("amount, balance", [
        (10, 110),
        (50, 150),
        (1_000_000, 1_000_100),
    ])
    # it's still a method so self and fixture are required
    def test_deposit(self, small_account, amount, balance):
        assert small_account.deposit(amount) == balance
    
    # test when exceptions are raised and parameters are involved should be done separately. See end of page in https://docs.pytest.org/en/stable/example/parametrize.html
    @pytest.mark.parametrize("amount, excep", [
        # invalid input, exception pairs
        ("a", pytest.raises(TypeError, match="You can only deposit numerical amounts")),
        (0, pytest.raises(ValueError, match="You need to deposit something...")),
        (-1, pytest.raises(ValueError, match="You need to deposit something...")),
        (1_000_001, pytest.raises(ValueError, match="Max deposit is a million at a time")),
    ])
    def test_deposit_exceptions(self, small_account, amount, excep):
        # a context manager is needed to handle the exceptions
        with excep as e:
            assert small_account.deposit(amount) == e



# both accounts are needed to text edge cases
@pytest.mark.usefixtures("large_account")
class TestWithdraw():
    
    @pytest.mark.parametrize("amount, balance", [
        (10, 1_999_990),
        (50, 1_999_950),
        (1_000_000, 1_000_000),
    ])
    # it's still a method so self and fixture are required
    def test_withdraw(self, large_account, amount, balance):
        assert large_account.withdraw(amount) == balance
    
    
    # test when exceptions are raised and parameters are involved should be done separately. See end of page in https://docs.pytest.org/en/stable/example/parametrize.html
    @pytest.mark.parametrize("amount, excep", [
        # invalid input, exception pairs
        ("a", pytest.raises(TypeError, match="You can only withdraw numerical amounts")),
        (0, pytest.raises(ValueError, match="You need to withdraw something...")),
        (-1, pytest.raises(ValueError, match="You need to withdraw something...")),
        (1_000_001, pytest.raises(ValueError, match="Max withdraw is a million at a time")),
    ])
    def test_withdraw_exceptions(self, large_account, amount, excep):
        # a context manager is needed to handle the exceptions
        with excep as e:
            assert large_account.withdraw(amount) == e

    # test withdraw more than balance exception so new paramenters
    @pytest.mark.parametrize("amount, excep", [
        # invalid input, exception pairs
        (200, pytest.raises(ValueError, match="You don't have enough")),
    ])
    
    def test_withdraw_exceptions_s_acc(self, small_account, amount, excep):
        # a context manager is needed to handle the exceptions
        with excep as e:
            assert small_account.withdraw(amount) == e

# test balance returning clean values
class TestGetBalance():
    def test_get_balance_s_acc(self, small_account, large_account):
        DEF_SMALL_BALANCE = 100
        DEF_LARGE_BALANCE = 2_000_000
        assert small_account.get_balance() == DEF_SMALL_BALANCE
        assert large_account.get_balance() == DEF_LARGE_BALANCE
