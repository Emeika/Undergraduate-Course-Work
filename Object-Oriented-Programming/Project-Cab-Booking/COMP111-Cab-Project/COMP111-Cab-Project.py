class Person:
    def __init__(self, username, password, contact):
        self.username = username
        self.password = password
        self.contact = contact

    def profile_display(self):
        print('Username:', self.username)
        print('Contact:', self.contact)


class Customer(Person):  # Inheritance with person
    def __init__(self, username, password, contact, car_booking_obj):
        super().__init__(username, password, contact)
        # CarBooking class is aggregated
        self.car_booking_obj = car_booking_obj

    def profile_display(self):
        # Overrides method in Person
        super().profile_display()

    def booking_display(self, payment_obj):  # Payment class Associated with Carbooking class through customer
        self.car_booking_obj.display(payment_obj)
        print()

    def trip_history(self):
        infile = open(self.username + '.txt', 'r')
        for line in infile:
            line = line.strip('\n').split(',')
            print()
            if line[10] == 'Cancelled':
                print('Cancelled Booking Details:')
                print('Date and time:', line[4])
                print('Fare: Rs.', line[3])
                print('Miles:', line[2])
                print('Payment made with:', line[9])
                print('Driver username:', line[5])
                print('Driver Contact:', line[6])
                print('Pickup Address:', line[0])
                print('Destination Address:', line[1])
                print('Vehicle:', line[7], line[8])
            else:
                print('Confirmed Booking Details:')
                print('Date and time:', line[4])
                print('Fare: Rs.', line[3])
                print('Miles:', line[2])
                print('Payment made with:', line[9])
                print('Driver username:', line[5])
                print('Driver Contact:', line[6])
                print('Pickup Address:', line[0])
                print('Destination Address:', line[1])
                print('Vehicle:', line[7], line[8])

        infile.close()


class Driver(Person):  # inheritance with person class
    def __init__(self, username, password, contact, vehicle_obj):
        super().__init__(username, password, contact)
        # Vehicle class is aggregated
        self.vehicle_obj = vehicle_obj

    def profile_display(self):
        # Overrides method in Person
        super().profile_display()
        self.vehicle_obj.display()

    def trip_history(self):
        infile = open('Booking.txt', 'r')
        for line in infile:
            line = line.strip('\n').split(',')
            if self.username == line[1]:
                if line[6] == 'Cancelled':
                    print()
                    print('Cancelled Booking by Customer:')
                    print('Date and time:', line[0])
                    print('Driver name:', line[1])
                    print('Pickup Address:', line[2])
                    print('Destination Address:', line[3])
                    print('Customer name:', line[4])
                    print('Fare:', line[5])
                else:
                    print()
                    print('Ride Completed:')
                    print('Date and time:', line[0])
                    print('Driver name:', line[1])
                    print('Pickup Address:', line[2])
                    print('Destination Address:', line[3])
                    print('Customer name:', line[4])
                    print('Total earning for this trip:', line[5])


class Vehicle:
    def __init__(self, v_type, model):
        self.v_type = v_type
        self.model = model

    def display(self):
        print('Vehicle type:', self.v_type)
        print('Vehicle Model:', self.model)


class Car(Vehicle):  # Inheritance with Vehicle
    def __init__(self, v_type, model):
        super().__init__(v_type, model)


class Auto(Vehicle):  # Inheritance with Vehicle
    def __init__(self, v_type, model):
        super().__init__(v_type, model)
        # if child class doesnt have the display function then it takes from parent class


class CarBooking:
    def __init__(self, pickup, destination, miles, date, driver_obj):
        self.date = date
        self.pickup = pickup
        self.destination = destination
        self.miles = miles
        self.fare = None
        # Driver class is aggregated
        self.driver_obj = driver_obj

    def set_fare(self, car_type):
        if car_type == 'Car':
            self.fare = self.miles * 40
        else:
            self.fare = self.miles * 30

    def get_fare(self):
        return self.fare

    def display(self, payment_obj):  # Association with payment class
        print('Date and Time:', self.date)
        print('Pickup Location:', self.pickup)
        print('Destination:', self.destination)
        payment_obj.payment_details()
        print('Assigned Driver:')
        self.driver_obj.profile_display()


class Payment:  # Grandfather class
    def __init__(self, amount):
        self.amount = amount

    def payment_details(self):
        print("Total Fare is:", self.amount, "rupees.")


class CashPayment(Payment):  # Inheritance with payment class (Father class)
    def __init__(self, amount, pay_type='Cash'):
        super().__init__(amount)
        self.pay_type = pay_type

    def get_paytype(self):
        return self.pay_type

    def payment_details(self):
        super().payment_details(),
        print('Paid by', self.pay_type)


class CardPayment(CashPayment):  # Multilevel Inheritance with Cashpayment class (Son/Derived class)
    def __init__(self, amount, card_number, name, c_type, expiry_date, pay_type='Card'):
        super().__init__(amount)
        self.card_number = card_number
        self.name = name
        self.c_type = c_type
        self.expiry_date = expiry_date
        self.pay_type = pay_type

    def get_paytype(self):
        return self.pay_type

    def payment_details(self):
        super().payment_details()
        print('Card Used:', self.c_type, '\nLast four digits of card:', str(self.card_number)[-4:])


def create_account(role):
    infile = open(role + '.txt', 'a+')
    username = input('Enter new username: ')
    password = input('Enter new password: ')
    contact = input('Enter contact number: ')
    print(username, password, contact, sep=',', file=infile)
    print('Account created.')
    infile.close()


def login(username, password, role):
    infile = open(role + '.txt', 'r')
    found = False
    contact = None
    for line in infile:
        line = line.rstrip('\n').split(',')
        if username == line[0] and password == line[1]:
            found = True
            contact = line[2]
    infile.close()
    return found, contact


def pay(amount):
    print('Your Fare for the trip is: Rs.', amount)
    print('1. Pay with Cash.')
    print('2. Pay with Card.')
    pay_choice = int(input('3. Enter your input (1/2): '))
    print()
    while (1 <= pay_choice <= 3) is False:
        pay_choice = int(input("Invalid input, Enter your input again (1/2): "))

    if pay_choice == 1:  # Pay with Cash
        payment_obj = CashPayment(amount)
        return payment_obj

    elif pay_choice == 2:  # Pay with Card
        c_type = input('Enter the card type (Debit/Credit): ').capitalize()
        while (c_type == 'Debit' or c_type == 'Credit') is False:
            c_type = input("Invalid input, Enter the card type again. (Debit/Credit): ").capitalize()

        card_number = input('Enter the card number: ')
        name = input('Enter the name on the card: ')
        expiry_date = input('Enter card Expiry date. (DD/MM/YYY): ')
        payment_obj = CardPayment(amount, card_number, name, c_type, expiry_date)
        return payment_obj


def main():
    # menu
    print('Cab Booking System')
    print('1. Customer Account.')
    print('2. Driver Account.')
    user_choice = int(input('Enter your input (1/2): '))
    print()

    while (1 <= user_choice <= 2) is False:  # Validation of input
        user_choice = int(input("Invalid input, Enter your input again (1/2): "))

    ext = False
    while not ext:
        # For customer login
        if user_choice == 1:
            print('1. Login.')
            print('2. Create Account.')
            inp = int(input('Enter your input (1/2): '))
            print()

            while (1 <= inp <= 2) is False:
                inp = int(input("Invalid input, Enter your input again (1/2): "))

            if inp == 2:  # Customer Create Account
                create_account('customer')

            elif inp == 1:  # Customer Login
                sign_in = False
                while not sign_in:
                    username = input('Enter username: ')
                    password = input('Enter password: ')
                    # Function Call to check if Username or password is in created file
                    login_check, contact = login(username, password, 'customer')
                    # returns a tuple with contact and login_check

                    if login_check:  # If login Info matches
                        customer_obj = Customer(username, password, contact, None)
                        print('Signed In Successfully!')
                        print('Your Profile:')
                        customer_obj.profile_display()
                        print()
                        sign_in = True

                        exit_two = False
                        while not exit_two:
                            print('1. Book a ride.')
                            print('2. View Trip History.')
                            print('3. Exit')
                            choice = int(input('4. Enter your input (1/2/3): '))
                            while (1 <= choice <= 3) is False:
                                choice = int(input("Invalid input, Enter your input again (1/2/3): "))

                            if choice == 1:  # Book Ride

                                pickup = input('Enter the pickup address: ')
                                destination = input('Enter the destination address: ')
                                miles = round(float(input('Enter miles: ')), 2)
                                print('Select the ride.')
                                print('1. Car')
                                print('2. Auto')
                                vehicle = int(input('Enter your input (1/2): '))
                                while (1 <= vehicle <= 2) is False:
                                    vehicle = int(input("Invalid input, Enter your input again (1/2): "))

                                # Get the Current Date and time
                                from datetime import datetime
                                now = datetime.now()
                                date_time = now.strftime("%d/%m/%Y %H:%M:%S")

                                # get Driver and Car details

                                import random

                                infile = open('driver.txt', 'r')
                                driver_list = []
                                for line in infile:
                                    line = line.strip('\n').split(',')
                                    if vehicle == 1 and line[3] == 'Car':  # If vehicle is a car
                                        driver_list.append(line)
                                    elif vehicle == 2 and line[3] == 'Auto':  # If vehicle is an auto
                                        driver_list.append(line)

                                assigned_driver = random.choice(driver_list)
                                driver_username = assigned_driver[0]
                                driver_password = assigned_driver[1]
                                driver_contact = assigned_driver[2]
                                driver_car_type = assigned_driver[3]
                                driver_car_name = assigned_driver[4]
                                if assigned_driver[3] == 'Car':
                                    vehicle_obj = Car(driver_car_type, driver_car_name)
                                else:
                                    vehicle_obj = Auto(driver_car_type, driver_car_name)

                                infile.close()

                                driver_obj = Driver(driver_username, driver_password, driver_contact, vehicle_obj)
                                booking_obj = CarBooking(pickup, destination, miles, date_time, driver_obj)
                                booking_obj.set_fare(driver_car_type)
                                customer_obj = Customer(username, password, contact, booking_obj)

                                cancel = None
                                menu_exit = False
                                payment_obj = None

                                while not menu_exit:
                                    amount = booking_obj.get_fare()
                                    # Function call to check whether payment is made with cash/card
                                    payment_obj = pay(amount)

                                    print('1. Confirm and view Booking.')
                                    print('2. Cancel Booking')
                                    print('3. Exit')
                                    menu_option = int(input('4. Enter your input (1/2/3): '))
                                    while (1 <= menu_option <= 3) is False:
                                        menu_option = int(input("Invalid input, Enter your input again (1/2/3): "))

                                    if menu_option == 1:  # Customer views and confirm Booking details
                                        print()
                                        print('Your Booking is Confirmed')
                                        customer_obj.booking_display(payment_obj)
                                        cancel = False
                                        menu_exit = True

                                    elif menu_option == 2:
                                        print('Booking Cancelled')
                                        print()
                                        inpfile = open('Booking.txt', 'a+')
                                        print(date_time, driver_username, pickup, destination, username,
                                              booking_obj.get_fare(), 'Cancelled', sep=',', file=inpfile)
                                        inpfile.close()

                                        book_file = open(str(username) + '.txt', 'a+')
                                        print(pickup, destination, miles, booking_obj.get_fare(), date_time,
                                              driver_username, driver_contact,
                                              driver_car_type, driver_car_name,
                                              payment_obj.get_paytype(), 'Cancelled', sep=',', file=book_file)
                                        book_file.close()
                                        cancel = True
                                        menu_exit = True

                                    else:
                                        menu_exit = True
                                        ext = True
                                        exit_two = True

                                if not cancel:  # Booking details for the customer is stored in file only when the
                                    # customer confirms booking
                                    book_file = open(str(username) + '.txt', 'a+')
                                    print(pickup, destination, miles, booking_obj.get_fare(), date_time,
                                          driver_username, driver_contact,
                                          driver_car_type,
                                          driver_car_name, payment_obj.get_paytype(), 'Completed', sep=',', file=book_file)
                                    book_file.close()

                                    inpfile = open('Booking.txt', 'a+')
                                    print(date_time, driver_username, pickup, destination, username,
                                          booking_obj.get_fare(), 'Completed', sep=',', file=inpfile)
                                    inpfile.close()

                            elif choice == 2:  # View Trip History
                                customer_obj.trip_history()
                                print()

                            else:
                                exit_two = True
                                ext = True

                    else:
                        print('Incorrect credentials, try again!')

        # For Driver Login
        elif user_choice == 2:
            first_exit = False
            while not first_exit:
                print('1. Login.')
                print('2. Create Account.')
                inp = int(input('Enter your input (1/2): '))
                print()

                while (1 <= inp <= 2) is False:
                    inp = int(input("Invalid input, Enter your input again (1/2): "))

                if inp == 2:  # Create Account - Can create multiple accounts before loging in
                    infile = open('driver.txt', 'a+')
                    username = input('Enter new username: ')
                    password = input('Enter new password: ')
                    car_type = input('Vehicle Type: Car or Auto: ').capitalize()
                    car_name = input('Enter vehicle name: ')
                    contact = int(input('Enter your contact number: '))
                    # write to file
                    print(username, password, contact, car_type, car_name, sep=',', file=infile)
                    print('Account created!')
                    print()
                    infile.close()

                elif inp == 1:  # Driver login
                    sign_in = False
                    while not sign_in:
                        username = input('Enter username: ')
                        password = input('Enter password: ')
                        car_type = None
                        car_name = None
                        contact = None
                        # Get Driver Profile Details
                        infile = open('driver.txt', 'r')
                        found = False
                        for line in infile:
                            line = line.rstrip('\n').split(',')
                            if username == line[0] and password == line[1]:
                                found = True
                                contact = line[2]
                                car_type = line[3]
                                car_name = line[4]

                        infile.close()

                        if found:
                            print('Signed In Successfully!')
                            print()
                            sign_in = True

                            if car_type == 'Car':
                                vehicle_obj = Car(car_type, car_name)
                            else:
                                vehicle_obj = Auto(car_type, car_name)
                            driver_obj = Driver(username, password, contact, vehicle_obj)
                            print('Your Profile:')
                            driver_obj.profile_display()
                            first_exit = True

                            exit_two = False
                            while not exit_two:
                                print()
                                print('1.View Trips taken.')
                                print('2.Total Earnings.')
                                print('3.Exit.')
                                driver_inp = int(input('Enter your input (1/2/3): '))
                                while (1 <= driver_inp <= 3) is False:
                                    driver_inp = int(input("Invalid input, Enter your input again (1/2/3): "))

                                if driver_inp == 1:  # View Trips taken
                                    driver_obj.trip_history()

                                elif driver_inp == 2:  # Total Earnings for today
                                    print('Enter date:')
                                    date = input('Earnings for: (dd/mm/yyyy). ')
                                    total = 0
                                    inputfile = open('Booking.txt', 'r')
                                    for line in inputfile:
                                        line = line.strip('\n').split(',')
                                        onlydate = line[0].split(' ')
                                        print(onlydate[0])
                                        if onlydate[0] == date and line[1] == username and line[6] == 'Completed':
                                            total += float(line[5])

                                    if total == 0:
                                        print('No data found against this date.')
                                    else:
                                        print('Total Earnings for', date, 'is', total)

                                else:
                                    exit_two = True

                            ext = True

                        else:
                            print('Incorrect credentials, try again!')


main()
