from email.mime import base


class Contract:
    def __init__(self, base_pay, hours=0):
        self.base_pay = base_pay
        self.hours = hours
    
    def get_pay(self):
        if not self.hours:
            return self.base_pay
        return self.base_pay * self.hours

    def get_hours(self):
        return self.hours
    
    def get_base_pay(self):
        return self.base_pay

    def is_contract_salary(self):
        return self.hours == 0