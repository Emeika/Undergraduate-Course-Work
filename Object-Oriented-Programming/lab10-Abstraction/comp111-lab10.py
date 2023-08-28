class Package:
    def __init__(self, sname, saddress, scity, sstate, szipcode, rname, raddress, rcity, rstate, rzipcode, weight, cost_per_ounce):
        self.sname = sname
        self.saddress = saddress
        self.scity = scity
        self.sstate = sstate
        self.szipcode = szipcode
        self.rname = rname
        self.raddress = raddress
        self.rcity = rcity
        self.rstate = rstate
        self.rzipcode = rzipcode
        self.weight = abs(weight)
        self.cost_per_ounce = abs(cost_per_ounce)

    def calculateCost(self):
        return(float(self.weight*self.cost_per_ounce))

class TwoDayPackage(Package):
    total = 0
    def __init__(self,sname, saddress, scity, sstate, szipcode, rname, raddress, rcity, rstate, rzipcode, weight, cost_per_ounce, flat_fee):
        super().__init__(sname, saddress, scity, sstate, szipcode, rname, raddress, rcity, rstate, rzipcode, weight, cost_per_ounce)
        self.flat_fee = flat_fee

    def calculateCost(self):
        TwoDayPackage.total = float(super().calculateCost()+self.flat_fee)
        print('Two Day Package total cost: ',round(TwoDayPackage.total,3))

class OvernightPackage(Package):
    total = 0
    def __init__(self,sname, saddress, scity, sstate, szipcode, rname, raddress, rcity, rstate, rzipcode, weight, cost_per_ounce, fee):
        super().__init__(sname, saddress, scity, sstate, szipcode, rname, raddress, rcity, rstate, rzipcode, weight,cost_per_ounce)
        self.fee = fee
    def calculateCost(self):
        OvernightPackage.total = float(super().calculateCost()+self.fee)
        print('Overnight Package total cost', round(OvernightPackage.total, 3))

def main():
    hehe = 'Y'
    while (hehe == 'Y'):
        choice = input('Enter the type of delivery: (Two Day Package/Overnight Package)?')
        choice = choice.lower()
        if choice ==  'two day package':
            twodayobj = TwoDayPackage('Daim','Ar complex','fantasy world','mental',69696, 'devil','gulberg','lahore','pk',8888,887,6.7,6.789)
            twodayobj.calculateCost()
        elif choice == 'overnight package':
            overnightobj = OvernightPackage('hafsah','shalimar','lahore','punjab',8888 , 'kiran','shadman','karachi','pks',7777,56.765,7.65,0.8)
            overnightobj.calculateCost()
        hehe = input('Create another package? (Y or N): ').upper()
main()







