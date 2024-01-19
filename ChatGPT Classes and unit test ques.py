import math

# Question 1
class Rectangle:
    """A rectangle with width w and height h"""
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    

    def area(self):
        """Returns area of Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of Rectangle"""
        return (self.width + self.height) * 2
    
    def is_square(self):
        """Determines if square"""
        if self.width == self.height:
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return f"Rectangle with width {(self.width):.2f} and height {(self.height):.2f}"
    

assert isinstance(Rectangle(9, 3.8).area(), float), "Test1 failed!"
assert Rectangle.is_square, "Test2 failed!"
assert math.isclose(Rectangle(2, 3.3).perimeter(), 10.5, abs_tol=0.1), "Test3 failed!"



# Question 2
class BankAccount:
    def __init__(self, account_holder_name, balance) -> None:
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return f"Balance for {self.account_holder_name} is {(self.balance):.2f}"


try:
    customer1 = BankAccount("Grace", 0.00)
    try:
        customer1 = BankAccount.withdraw(9000.00)
    except:
        print("Not enough money")
except:
    print(customer1.get_balance())


