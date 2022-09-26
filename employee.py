"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from email.policy import default
from contract import Contract
from comission import Commission


class Employee:
    # Make a contract class
    def __init__(self, name, contract : Contract, commission=None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        total_pay = 0
        total_pay += self.contract.get_pay()
        if self.commission:
            total_pay += self.commission.get_pay()

        return total_pay

    def __str__(self):
        string = f"{self.name} works on a "
        if self.contract.is_contract_salary():
            string += f"monthly salary of {self.contract.get_pay()}" 
        else:
            string += f"contract of {self.contract.get_hours()} hours at {self.contract.get_base_pay()}/hour"
        if not self.commission:
            return string + f".  Their total pay is {self.get_pay()}."
        
        if self.commission.get_is_bonus():
            string += f" and receives a bonus commission of {self.commission.get_pay()}."
        else:
            string += f" and receives a commission for {self.commission.get_contracts_landed()} contract(s) at {self.commission.get_commission_rate()}/contract."
        return string + f"  Their total pay is {self.get_pay()}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Contract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Contract(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Contract(3000), Commission(False, 200, 4))
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Contract(25, 150), Commission(False, 220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Contract(2000), Commission(True, 1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Contract(30, 120), Commission(True, 600))