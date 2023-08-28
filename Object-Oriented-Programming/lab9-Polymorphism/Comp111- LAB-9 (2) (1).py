# Hafsah Shahbaz
# 251684784
# lab9

class payment: #Abstract class
    def __init__(self,amount):
        self.amount = amount

    def paymentdetails(self, creditcard_obj):
        return self.amount

class cashpayment(payment):  # inherited from payment
    def __init__(self,amount):
        super().__init__(amount)

    def paymentdetails(self,creditcard_obj):
        print('The payment in cash is',super().paymentdetails(creditcard_obj)) #displaying that the payment is in cash
        print()
        # super().paymentdetails() calls the paymentdetails method from base class

class cardpayment(payment):
    def __init__(self,amount): # inherited from payment
        super().__init__(amount)

    def paymentdetails(self,creditcard_obj):
        print('The payment in card is', super().paymentdetails(creditcard_obj)) #overides method in payment
        creditcard_obj.display()
        print()

class creditcard:
    def __init__(self,name,expirydate,cardnum):
        self.name = name
        self.expirydate = expirydate
        self.cardnum = cardnum

    def display(self):
        print('The Card details are: ')
        print('Name: ' ,self.name,'Expirydate: ' ,self.expirydate,'Cardnum: ' ,self.cardnum)


def main():
    paylit = []
    objlist = []
    creditcard_obj = None

    for i in range(4):
        choice = input("Card payment or Cash payment? ")
        c = choice.lower()
        if c == 'cash':
            payment_obj = cashpayment(input('Enter amount: '))
            objlist.append(payment_obj)
            paylit.append(creditcard_obj)

        elif c == 'card':
            payment_obj = cardpayment(input('Enter amount: '))
            names = input('Enter name: ')
            expiry = input('Enter expiry date: ')
            ccnum = input('Enter card number: ')
            creditcard_obj = creditcard(names,expiry,ccnum)
            objlist.append(payment_obj)
            paylit.append(creditcard_obj)
        print()
    x = 0
    for i in objlist:
        i.paymentdetails(paylit[x])
        x +=1
main()