
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
            self.spaces_taken.append(self.spaces_avail)
            self.taken_tickets.append(self.tickets_avail)
            self.current_tickets.update({"Paid": False})
            self.spaces_avail -= 1 
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
                print("Ticket has been paid. Gate opening. Have a wonderful day :)")
                self.current_tickets.update({"Paid": True})
                break


            elif self.payment > self.cust_total:
                print("Please take your change. Have a wonderful day :)")
                self.current_tickets.update({"Paid": True})
                break

            elif self.payment < self.cust_total:
                print("Not enough money! You can't leave until you pay me.")
                
                while True:
                    self.payment_addl = int(input(f"${self.cust_total - self.payment} left due. (Bills accepted: $5, $10, $20, $50, $100)\n"))
                    if (self.payment_addl + self.payment) == self.cust_total:
                        print("Ticket has been paid. Gate opening. Have a wonderful day :)")
                        self.current_tickets.update({"Paid": True})
                        paid_in_full = True
                        break
                    else:
                        self.payment += self.payment_addl
                        continue


    
fams = ParkingGarage()
fams.take_ticket()
fams.pay_for_parking()