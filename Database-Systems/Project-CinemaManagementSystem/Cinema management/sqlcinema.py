import random


def generate_full_names(num_combinations):
    first_names = ['Manal', 'Alice', 'Bob', 'Shahzeb', 'Charlie', 'Daim', 'David', 'Eve', 'Frank', 'Grace',
                   'Areesha', 'Henry', 'Ivy', 'Jack', 'Kelly', 'Leo', 'Mia', 'Hafsah', 'Nathan', 'Kiran',
                   'Olivia', 'Peter', 'Quinn', 'Rose', 'Sam', 'Tina', 'Saad', 'Talal', 'Amina', 'Fatima',
                   'Mustafa', 'Nida']
    last_names = ['Adams', 'Brown', 'Clark', 'Davis', 'Evans', 'Foster', 'Gray', 'Hall', 'Irwin', 'Johnson',
                  'King', 'Lee', 'Miller', 'Nelson', 'Owens', 'Parker', 'Quinn', 'Roberts', 'Smith', 'Taylor',
                  'Ammad', 'Khalid', 'Kamran', 'Zahid', 'Shahbaz', 'Qaiser', 'Fareed', 'Ahmer', 'Qasim', 'Abbas',
                  'Zafar', 'Aslam']

    combinations = 0
    full_names = []

    while combinations < num_combinations:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        full_name = f'{first_name} {last_name}'

        if full_name not in full_names:
            full_names.append(full_name)
            combinations += 1

    return full_names


def insert_employees():
    # Insert employees for each branch
    branch_ids = [1, 2, 3]
    employee_id = 1

    for branch_id in branch_ids:
        # Generate a list of 20 unique full names for each role
        managers = generate_full_names(1)
        assistants = generate_full_names(10)
        janitorial = generate_full_names(5)
        snack_bar = generate_full_names(4)

        # Insert Manager
        manager_name = managers[0]

        manager_email = f'{manager_name.replace(" ", ".")}@gmail.com'
        print(f"insert into Employees(EmployeeId, BranchID, EmployeeName, Position, ContactNumber, Email)"
            f"\nvalues({employee_id}, {branch_id}, '{manager_name}', 'Manager', '03001234567', '{manager_email}')")

        # Insert Assistants
        for assistant_name in assistants:
            employee_id += 1

            assistant_email = f'{assistant_name.replace(" ", ".")}@gmail.com'
            print(f"insert into Employees(EmployeeId, BranchID, EmployeeName, Position, ContactNumber, Email)"
                  f"\nvalues({employee_id}, {branch_id}, '{assistant_name}', 'Assistance', "
                  f"'{random.randint(3001234567, 3099123456)}', '{assistant_email}')")

        # Insert Janitorial
        for janitorial_name in janitorial:
            employee_id += 1

            janitorial_email = f'{janitorial_name.replace(" ", ".")}@gmail.com'
            print(f"insert into Employees(EmployeeId, BranchID, EmployeeName, Position, ContactNumber, Email)"
                  f"\nvalues({employee_id}, {branch_id}, '{janitorial_name}', 'Janitorial', "
                  f"'{random.randint(3001234567, 3099123456)}', '{janitorial_email}')")

        # insert Snack Bar
        for snack_bar_name in snack_bar:
            employee_id += 1

            snack_bar_email = f'{snack_bar_name.replace(" ", ".")}@gmail.com'
            print(f"insert into Employees(EmployeeId, BranchID, EmployeeName, Position, ContactNumber, Email)"
                  f"\nvalues({employee_id}, {branch_id}, '{snack_bar_name}', 'Snack Bar', "
                  f"'{random.randint(3001234567, 3099123456)}', '{snack_bar_email}')")

        employee_id += 1


def insert_rooms():
    room_id = 0
    seat_num = 0
    seat_id = 0

    for i in range(3):  # cities

        for k in range(5):  # rooms
            room_id += 1

            for p in range(100):  # seats
                seat_id += 1
                seat_num += 1

                print(f"insert into Seats (SeatId , RoomId , SeatNumber) "
                      f"\nvalues({seat_id} , {room_id} , {seat_num})")

            seat_num = 0


def insert_food():
    food_id = 0
    branch_id = 0
    food_items = ['Nachos', 'Salted Popcorn', 'Caramel Popcorn', 'Lays', 'Ice Tea', 'Sprite', 'Fanta', 'Coke', 'Water',
                  'French Fries']

    price_list = [650, 300, 350, 200, 300, 150, 150, 150, 100, 350]

    for i in range(3):  # cities
        branch_id += 1

        for k in range(10):  # items
            food_id += 1
            food_name = food_items[k]
            price = price_list[k]

            print(f"insert into Food(FoodId, BranchID, FoodName, Price)"
                  f"\nvalues({food_id}, {branch_id}, '{food_name}', {price})")


def insert_shifts():
    shift_slots = ['12:00 - 17:00', '17:00 - 22:00', '22:00 - 03:00']
    shift_id = 0

    for k in range(3):
        shift_id += 1
        shift_time = shift_slots[k]

        print(f'insert into Shifts(ShiftId, ShiftTime)'
              f'\nvalues({shift_id}, \'{shift_time}\')')


def insert_schedule():
    schedule_id = 0

    for i in range(1, 31):  # dates for a month

        for j in range(1, 6):  # rooms in a branch

            for k in range(1, 4):  # shifts
                schedule_id += 1

                if i < 10:
                    print(f"({schedule_id}, {j}, {j}, {k}, '2023-06-0{i}'),")
                else:
                    print(f"({schedule_id}, {j}, {j}, {k}, '2023-06-{i}'),")


def insert_employee_shift():
    e_shift_id = 0
    employee_id = 0
    for i in range(1, 31):  # days

        for j in range(1, 4):  # shifts

            for k in range(1, 21):  # num of employees per branch
                e_shift_id += 1
                employee_id += 1

                print(f"insert into EmployeeShifts(EmployeeShiftId, EmployeeId, ShiftId, Date)"
                      f"\nvalues({e_shift_id}, {employee_id}, {j}, '2023-06-{i}'),")

        employee_id = 0


def generate_customer_names(num_combinations):
    first_names = [
        'Emma', 'Noah', 'Olivia', 'Liam', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia',
        'Harper', 'Evelyn', 'Abigail', 'Emily', 'Elizabeth', 'Mila', 'Ella', 'Avery', 'Sofia', 'Camila',
        'Aria', 'Scarlett', 'Victoria', 'Madison', 'Luna', 'Grace', 'Chloe', 'Penelope', 'Layla', 'Riley',
        'Zoey', 'Nora', 'Lily', 'Eleanor', 'Hannah', 'Lillian', 'Addison', 'Aubrey', 'Ellie', 'Stella',
        'Natalie', 'Zoe', 'Leah', 'Hazel', 'Violet', 'Aurora', 'Savannah', 'Audrey', 'Brooklyn', 'Bella',
        'Claire', 'Skylar', 'Lucy', 'Paisley', 'Everly', 'Anna', 'Caroline', 'Nova', 'Genesis', 'Emilia',
        'Kennedy', 'Samantha', 'Maya', 'Willow', 'Kinsley', 'Naomi', 'Aaliyah', 'Elena', 'Sarah', 'Ariana',
        'Allison', 'Gabriella', 'Alice', 'Madelyn', 'Cora', 'Ruby', 'Eva', 'Serenity', 'Autumn', 'Adeline'
    ]

    last_names = [
        'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson',
        'Martinez', 'Anderson', 'Taylor', 'Thomas', 'Hernandez', 'Moore', 'Martin', 'Jackson', 'Thompson',
        'White', 'Lopez', 'Lee', 'Gonzalez', 'Harris', 'Clark', 'Lewis', 'Robinson', 'Walker', 'Perez',
        'Hall', 'Young', 'Allen', 'Sanchez', 'Wright', 'King', 'Scott', 'Green', 'Baker', 'Adams',
        'Nelson', 'Hill', 'Ramirez', 'Campbell', 'Mitchell', 'Roberts', 'Carter', 'Phillips', 'Evans',
        'Turner', 'Torres', 'Parker', 'Collins', 'Edwards', 'Stewart', 'Flores', 'Morris', 'Nguyen',
        'Murphy', 'Rivera', 'Cook', 'Rogers', 'Morgan', 'Peterson', 'Cooper', 'Reed', 'Bailey', 'Bell'
    ]

    combinations = 0
    full_names = []

    while combinations < num_combinations:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        full_name = f'{first_name} {last_name}'

        if full_name not in full_names:
            full_names.append(full_name)
            combinations += 1
    return full_names


def insert_loyalty_customers(customer_list):
    customer_id = 1
    customer_name_list = customer_list

    for i in range(2000):
        customer_email = f'{customer_name_list[i].replace(" ", ".")}@gmail.com'
        print(f"insert into LoyaltyCustomers(CustomerId, CustomerName, ContactNumber, Email)"
              f"\nvalues({customer_id}, '{customer_name_list[i]}', "
              f"'{random.randint(3001234567, 3099123456)}', '{customer_email}')")

        customer_id += 1


def insert_reservations():
    shift_slots = ['12:00 - 17:00', '17:00 - 22:00', '22:00 - 03:00']
    book_seats = []
    checked_numbers = []
    reservation_id = 0
    check_list=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000]


    for date in range(1, 5):

        for shift in range(3):

            shift_time = shift_slots[shift]

            for movie_id in range(1, 6):
                total_reservations = random.randint(250, 300)

                for i in range(total_reservations):
                    reservation_id += 1
                    seat_id = random.randint(1, 1500)

                    while seat_id in book_seats:
                        checked_numbers.append(seat_id)
                        seat_id = random.randint(1, 1500)

                        if seat_id not in checked_numbers:
                            book_seats.append(seat_id)

                    customer_id = random.randint(1, 2000)

                    # ReservationId, MovieId, CustomerId, ReservationDate, ReservationTime, SeatId
                    if reservation_id in check_list:
                        print(f"insert into Reservations(ReservationId, MovieId, CustomerId, ReservationDate, ReservationTime, SeatId)\nvalues")


                    print(f"({reservation_id}, {movie_id}, {customer_id}, '2023-06-{date}', '{shift_time}', {seat_id}),")

            book_seats = []


#insert_employees()
#insert_rooms()
#insert_food()
#insert_shifts()
#insert_schedule()
#insert_employee_shift()
customer_names = generate_customer_names(2000)
insert_loyalty_customers(customer_names)
#insert_reservations()
