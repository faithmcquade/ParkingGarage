import random

class ParkingGarage:
    def __init__(self):
        self.spaces_taken = []
        self.current_tickets = {}
        self.spaces_avail = ["A1", "B2", "C3", "D1", "E2", "F3", "G1", "H2", "I3"]
        self.tickets_avail = 9


    def take_ticket(self):
        if self.tickets_avail > 0:
            print(f"Welcome to the Parking Garage, there are {self.tickets_avail} tickets available, please take one.")
            self.assign_space = random.choice(self.spaces_avail)
            self.spaces_avail.remove(self.assign_space)
            self.spaces_taken.append(self.assign_space)
            self.current_tickets.update({"Paid": False})
            self.tickets_avail -= 1

        else:
            print("Sorry, the garage is full. No available tickets.")

    def pay_for_parking(self):
        self.rate_hourly = 20
        paid_in_full = False

        while not paid_in_full:
            
            self.hours_stayed = int(input("How many hours did you stay? Please be honest...\n"))
            self.cust_total = (self.rate_hourly * self.hours_stayed)
            print(f"Your total is: ${self.cust_total}")
            self.payment = int(input("Please insert your payment: (Bills accepted: $5, $10, $20, $50, $100)\n"))
            
            if self.payment == self.cust_total:
                print("Ticket has been paid. You have 15 minutes to leave")
                self.current_tickets.update({"Paid": True})
                paid_in_full = True
                self.leave_garage()
                
            elif self.payment > self.cust_total:
                print("Please take your change.")
                self.current_tickets.update({"Paid": True})
                paid_in_full = True
                self.leave_garage()
                
            elif self.payment < self.cust_total:
                print("Not enough money! You can't leave until you pay me.")
                
                
                self.payment_addl = int(input(f"${self.cust_total - self.payment} left due. (Bills accepted: $5, $10, $20, $50, $100)\n"))
                if (self.payment_addl + self.payment) == self.cust_total:
                    print("Ticket has been paid. You have 15 minutes to leave.")
                    self.current_tickets.update({"Paid": True})
                    paid_in_full = True
                    self.leave_garage()
                else:
                    self.payment += self.payment_addl
    
    def leave_garage(self):
        if True in self.current_tickets.values():
            print("Thank you, have a wonderful day! :)")
            self.tickets_avail += 1
            self.spaces_taken.remove(self.assign_space)
            self.spaces_avail.append(self.assign_space)
            print(self.spaces_taken)
        elif False in self.current_tickets.values():
            print("Please return to pay.")
        return


        


    
fams = ParkingGarage()
fams.take_ticket()
fams.pay_for_parking()
