# Create a class Continental. Make subclasses as AN, AM, SAM, SCT having its own functionalities and work
# Create another parent class paygroup and link both classes and use the functionalities

class Continental:
    def __init__(self, region):
        self.region = region

    def disp_region(self):
        return f"Region: {self.region}"
    
    def __str__(self):
        return f"Welcome to Conti. You are currently in {self.region}"

class AN(Continental):
    def __init__(self,region ="Asia, Bangalore",amount= 549889):
        super().__init__(region)
        self.amount = amount
    
    def increment(self):
        self.amount += self.amount ** 0.5
    
    def disp_info(self):
        self.increment()
        return f"Welcome to AN {self.region}. Your salary after hike of 50% is {self.amount}"

class AM(Continental):
    def __init__(self,region = "JKI", amount = 100000):
        super().__init(region)
        self.amount = amount

    def increment(self):
        self.amount += self.amount**10

    def disp_info(self):
        self.increment()
        return f"Welcome to AM {self.region}. Your salary after hike of 50% is {self.amount}"
    
pers1 = AN()
print(pers1.disp_info())
