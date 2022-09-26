class Commission:
    def __init__(self, is_bonus, commission_rate, contracts_landed=0):
        self.is_bonus = is_bonus
        self.commission_rate = commission_rate
        self.contracts_landed = contracts_landed

    def get_pay(self):
        if self.is_bonus:
            return self.commission_rate
        return self.commission_rate * self.contracts_landed
    
    def get_contracts_landed(self):
        return self.contracts_landed

    def get_commission_rate(self):
        return self.commission_rate

    def get_is_bonus(self):
        return self.is_bonus
        
