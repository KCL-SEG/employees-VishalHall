"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from email.policy import default


class Employee:
    # Make a contract class
    def __init__(self, name, has_salary_contract, base_pay, gets_comission, gets_fixed_bonus, hours=0, comission_rate=0, contracts_landed = 1):
        self.name = name
        self.has_salary_contract = has_salary_contract
        self.gets_comission = gets_comission
        self.base_pay = base_pay
        self.hours = hours
        self.comission_rate = comission_rate
        self.contracts_landed = contracts_landed
        self.gets_fixed_bonus = gets_fixed_bonus

        self.summary = f"{self.name} works on a "
        self.total_pay = 1

    def get_pay(self):
        if self.has_salary_contract:
            self.total_pay = self.base_pay
            self.summary += f"monthly salary of {self.base_pay} "
        else:
            self.total_pay = self.base_pay * self.hours
            self.summary += f"contract of {self.hours} hours at {self.base_pay}/hour"
        if not self.gets_comission:
            return self.total_pay
        if self.gets_fixed_bonus:
            self.summary += f" and receives a bonus commission of {self.comission_rate}"
        else:
            self.summary += f" and receives a commission for {self.contracts_landed}(s) at {self.comission_rate}/contract"
        
        self.total_pay += self.contracts_landed * self.comission_rate
        return self.total_pay
        
        

    def __str__(self):
        self.get_pay()
        self.summary += f".  Their total pay is {self.total_pay}."
        return self.summary


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', True, 4000, False, False)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, 25, False, 100, False)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, 3000, True, False, contracts_landed=4, comission_rate=200)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', False, 25, True, 150, False, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 2000, True, True, comission_rate=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', False, 30, True, True, 120, 600)
print (str(ariel))