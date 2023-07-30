#code here
class ParkingGarage:
    def __init__(self):
        self.taken_tickets = []
        self.spaces_taken = []
        self.current_tickets = {}
        self.spaces_avail = 50
        self.tickets_avail = 50


    def take_ticket(self):
        if self.spaces_avail > 0:
            print(f"Welcome to the Parking Garage, there are {self.spaces_avail} spaces available, please take your ticket.")
            self.paid = "Unpaid"
            self.spaces_taken.append(self.spaces_avail)
            self.taken_tickets.append(self.tickets_avail)
            self.current_tickets.update({self.spaces_avail: self.paid})
            self.spaces_avail -= 1 
            self.tickets_avail -= 1
            print(self.current_tickets)

        else:
            print("Sorry, the garage is full. No available tickets.")
    
    
    

    
fams = ParkingGarage()
fams.take_ticket()