class passenger:
    def __init__(self,name):
        self.name = name

    def getname(self):
        return self.name

    def purchase_seat(self, busobj, sn):
        for seat in busobj.getseats():
            if seat.getsn() == sn and seat.getflag() == 1:
                seat.setoccupant(self)
                seat.setflag()
                busobj.setamount(busobj.getprice())

class bus:
    def __init__(self,ticket_price_per_seat):
        self.ticket_price_per_seat = ticket_price_per_seat
        self.booking_amount = 0
        self.seats = [seat(x) for x in range(1,25)]

    def getprice(self):
        return self.ticket_price_per_seat

    def setamount(self, amount):
        self.booking_amount += amount

    def getseats(self):
        return self.seats

    def display(self):
        [seat.display() for seat in self.seats]

        print('Total Bokking amount: ', self.booking_amount)

class seat:
    def __init__(self, seat_number, occupant = ""):
        self.seat_number = seat_number
        self.occupant = occupant
        self.flag = 1

    def getsn(self):
        return self.seat_number

    def getflag(self):
        return self.flag

    def setflag(self):
        self.flag = 0

    def setoccupant(self,passengerobj):
        self.occupant = passengerobj

    def display(self):
        if self.getflag() == 0:
            print('Seat number: ',self.seat_number, 'Occupant name: ', self.occupant.getname())

def main():
    busobj = bus(500)
    passengerobj1 = passenger('Daimi')
    passengerobj2 = passenger('Anonymous')
    print('Available seats: ')
    for i in busobj.getseats():
        if i.getflag() == 1:
            print(i.getsn(), end=" ")
    print()
    passengerobj1.purchase_seat(busobj, 15)
    passengerobj2.purchase_seat(busobj, 15)
    busobj.display()
    print()
    print('Available seats:')
    for i in busobj.getseats():
        if i.getflag() == 1:
            print(i.getsn(), end=" ")
main()
