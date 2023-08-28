# HAFSAH SHAHBAZ
# 251684784
# ASSIGNMENT # 2

# Task 1
class vehicle:  # base class
    def __init__(self, manufacturer, no_of_cylinder, personobj):  # aggregation with the owner
        self.manufacturer = manufacturer
        self.no_of_cylinder = no_of_cylinder
        self.personobj = personobj

    def display(self):
        print('Manufacturer: ', self.manufacturer, '\nNumber of cylinder: ', self.no_of_cylinder, "\nOwner's name: ", self.personobj.getname())

class truck(vehicle):  #inherited from vehicle
    def __init__(self, load_capacity, towing_capacity, manufacturer, no_of_cylinder, personobj):
        super().__init__(manufacturer,no_of_cylinder, personobj)
        self.load_capacity = load_capacity
        self.towing_capacity = towing_capacity

    def display(self):  # Overrides method display in vehicle
        print('Truck info: ')
        super().display()
        print('Load capacity: ', self.load_capacity,'\nTowing capacity: ',self.towing_capacity)
        print()

class bus(vehicle):  #inherited from vehicle
    def __init__(self, no_of_passengers, luggage_weight, manufacturer, no_of_cylinder, personobj):
        super().__init__(manufacturer, no_of_cylinder, personobj)
        self.no_of_passengers = no_of_passengers
        self.luggage_weight = luggage_weight

    def display(self):  #function to display the RouteInfo - association with route
        # Overrides method display in vehicle
        print('Bus info: ')
        super().display()
        print('Number of passengers: ', self.no_of_passengers,'\nLuggage weight: ',self.luggage_weight)
        print()

    def routeinfo(self, routeobj): #function to display the RouteInfo - association with route
        print('Route Info:\nTravelling time: ', routeobj.travelling_time,'\nDistance: ',routeobj.distance, '\nSource: ',routeobj.source,'\nDestination: ',routeobj.destination,'\nFare: ',routeobj.fare)
        print()
class person:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

class route:
    routelist = []
    def __init__(self, travelling_time, distance, source, destination, fare):
        self.travelling_time = travelling_time
        self.distance = distance
        self.source = source
        self.destination = destination
        self.fare = fare
        route.routelist.append(self)

def main():
    objlist = []
    num_t = int(input('How many trucks do you want to enter: '))
    for i in range(num_t):
        print('Truck ', i + 1)
        load = round((float(input('Load capacity: '))),3)
        tow = int(input('Towing capacity: Kg. '))
        manu = input('Manufacturer: ')
        cylinder = int(input('No. of cylinder: '))
        owner = input('Enter the owner: ')
        personobj = person(owner)
        objlist.append(truck(load, tow, manu, cylinder, personobj))
        print()

    num_b = int(input('How many buses do you want to enter: '))
    for x in range(num_b):
        print('Bus ', x + 1)
        passenger = int(input('No of passengers: '))
        luggage = int(input('Luggage weight: '))
        manufacturer = input('Manufacturer: ')
        no_cylinder = int(input('No. of cylinder: '))
        owner_name = input('Enter the owner: ')
        time = input('Travelling time: ')
        distance = input('Distance travelled: ')
        source = input('Source: ')
        destination = input('Destination: ')
        fare = input('Fare: ')
        routeobj = route(time,distance,source,destination,fare)
        person_obj = person(owner_name)
        objlist.append(bus(passenger, luggage, manufacturer, no_cylinder, person_obj))
        print()
    print()

    i=0
    for object in objlist:
        if isinstance(object, truck):
            object.display()
            print()
        else:
            object.display()
            object.routeinfo(route.routelist[i])
            i += 1
main()

## Task 2

from abc import ABC, abstractmethod
class player:  # base class
    def __init__(self, name, matches):
        self.name = name
        self.matches = matches
    def display(self):
        print('Player’s name: ', self.name, '\nNumber of matches player played: ', self.matches)

    @abstractmethod
    def playertype(self):  # abstract method
        pass

class batsman(player):
    def __init__(self, name, matches, total_score, per_match_score, average=''):
        super().__init__(name, matches)  # super class call
        self.total_score = total_score
        self.per_match_score = per_match_score
        self.average = average

    def calculate_avg(self):
        self.average = int((self.total_score/self.matches))
        return self.average

    def display(self):  # overriding the display in player
        super().display()
        print('Total score: ', self.total_score,'\nPer match score: ', self.per_match_score,'\nAverage: ',self.average)

    def playertype(self):  # overriding abstract method
        print('Player: Batsman')

class bowler(player):
    def __init__(self,name, matches, no_of_wickets, per_match_wickets):
        super().__init__(name, matches)  # super class call
        self.no_of_wickets = no_of_wickets
        self.per_match_wickets = per_match_wickets

    def display(self):  # overriding the display in player
        super().display()
        print('No. of wickets: ', self.no_of_wickets, '\nPer match wickets: ', self.per_match_wickets)

    def playertype(self):  # overriding abstract method
        print('Player: Bowler')

def main():
    check = int(input('How many batsman: '))
    for i in range(check):
        per_match_score_list = []
        total = 0
        player_name = input('Enter the players name: ')
        match_num = int(input('Enter the number of matches the player played: '))
        for i in range(1,match_num+1):
            print('Match ',i)
            per_match_score_list.append(int(input('Enter score: ')))
        for x in per_match_score_list:
            total += x
        print()
        batsmanobj = batsman(player_name,match_num,total,per_match_score_list)
        batsmanobj.calculate_avg()
        batsmanobj.playertype()
        batsmanobj.display()
        print()

    check = int(input('How many ballers: '))
    for i in range(check):
        per_match_wickets_list = []
        pname = input('Enter the players name: ')
        num_of_match = int(input('Enter the number of matches the player played: '))
        wicket_num = int(input('Total number of wickets the bowler has taken: '))
        for y in range(1,num_of_match + 1):
            print('Match ',y)
            per_match_wickets_list.append(int(input('Enter wickets: ')))
            print()
            bowlerobj = bowler(pname,num_of_match,wicket_num,per_match_wickets_list)
        bowlerobj.playertype()
        bowlerobj.display()
        print()
main()

# Task 3

from abc import ABC, abstractmethod
class carbonFootprint:
    @abstractmethod
    def getcarbonFootprint(self):
        pass

class building(carbonFootprint):
    def __init__(self,avgMonthly_electric_bill,avgMonthly_gas_bill,price_thousand_cubic_feet = 3.00,gas_emissions_factor=120.61, price_kwh=8.00, electricity_emissions_factor=1.37):
        self.avgMonthly_electric_bill = avgMonthly_electric_bill
        self.price_kwh = price_kwh
        self.electricity_emissions_factor = electricity_emissions_factor
        self.avgMonthly_gas_bill = avgMonthly_gas_bill
        self.price_thousand_cubic_feet = price_thousand_cubic_feet
        self.gas_emissions_factor = gas_emissions_factor

    def getcarbonFootprint(self):  #Overrides method in carbonFootprint
        x =round(((self.avgMonthly_electric_bill/self.price_kwh) * self.electricity_emissions_factor * 12),3)
        y =  round(((self.avgMonthly_gas_bill/self.price_thousand_cubic_feet) *self.gas_emissions_factor * 12),3)
        total = x+y

        print('Electricity CO2 emissions in pounds: ', x)
        print('Natural Gas CO2 emissions in pounds: ', y)
        print('Total CO2 emissions from buildings in pounds:', total)
        print()

class car(carbonFootprint):
    def __init__(self,mile,fuel_efficiency ):
        self.mile = mile
        self.fuel_efficiency =fuel_efficiency

    def getcarbonFootprint(self):
        y = ((self.mile* 52 )/ self.fuel_efficiency) * 19.4 * (100/95)
        print('CO2 emissions in pounds from cars: ', y)
        print()

class bicycle(carbonFootprint):

    def getcarbonFootprint(self):
        print('No CO2 emissions from bicycle')

def main():

    obj1 = building(40000,2000)
    obj2 = car(500,30)
    obj3 = bicycle()
    objlist = [obj1,obj2,obj3]
    for i in objlist:
        i.getcarbonFootprint()
main()