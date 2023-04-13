class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = [ ]

    # I need to remember to interacct with the Person object

    # Multiple classes lab - 
    # A
    def drive(self):
        return "Brum brum"
    # B
    # need to give out the number of passengers that are on the bus
    # use len() to get length of passengers list
    def passenger_count(self):
        return len(self.passengers)
    # C
    # need to add passenger as argument as user needs to input a new passenger
    # use insert(0, passenger) to put new passenger at the front of the passengers list (index 0)
    def pick_up(self, person):
        self.passengers.insert(0, person)
    # D
    # need to add passenger as argument as user inputs passenger that leaves the bus
    # use remove() to remove the passenger that has left the bus
    def drop_off(self, person):
        self.passengers.remove(person)

    # E 
    # need to empty the passengers list so there's nothing in it
    # use clear() to remove the passenger that has left the bus
    def empty_bus(self, passengers):
        self.passengers.clear(passengers)

    # 1
    def has_route_number(self):
        return self.route_number in Bus # should give True
    # 2
    def has_destination(self):
        return self.destination in Bus # should give True
    # 3
    def can_drive(self):
        self.drive(self)
    # 4
    def starts_with_no_passengers(self):
        return len(self.passengers) == []
    # 5
    # need to check if passenger_count is within 75, wasn't sure so used this as an example
    # creat bus_passenger_capacity 
    # use len() to check if there's 75 people, if there's less than 75 then passenger can get on the bus
    def can_pick_up_passenger(self):
        bus_passenger_capacity = 75
        return len(self.passengers) <= bus_passenger_capacity
    # 6
    # need to check if passenger_count is taking one away
    # call passenger_count() method
    def can_drop_off_passenger(self):
        return self.passenger_count() > 0
    

    


        

        









# create a Bus class [X]
# give the following properties:
    # - route_number: 22 int
    # - destination: "Ocean Terminal" str
    # - passengers [ ]
# create some methods:
    # - drive() - make sure it returns "Brum brum" string [X]


    # - total_passengers() - 
    # - add_passenger_total_passengers()


    # - drop_off_one_passenger()
    # - remove_all_passengers()

# create a Person class
    # give the following properties:
    # - name
    # - age

