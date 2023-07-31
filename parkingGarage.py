import random

class ParkingGarage:
    def __init__(self):
        self.spaces_taken = []
        self.current_tickets = {}
        self.spaces_avail = ["A1", "A2", "A3", "B1", "B2", "F3", "F6", "G12", "G2"]
        self.tickets_avail = 9
        self.rate_hourly = 60

    def take_ticket(self):
        """
        Takes ticket from machine, assigns space from available spaces at random.
        Subtracts available tickets by 1.
        Sets default payment status to False.
        """
        if self.tickets_avail > 0:
            print(
                f"Welcome to the Parking Garage, our hourly rate is ${self.rate_hourly} per hour."
                f"there are {self.tickets_avail} tickets available, please take one."
            )
            self.assign_space = random.choice(self.spaces_avail)
            self.spaces_avail.remove(self.assign_space)
            self.spaces_taken.append(self.assign_space)
            self.current_tickets.update({"Paid": False})
            self.tickets_avail -= 1
            print(f"Your assigned space is {self.assign_space}")
        else:
            print("Sorry, the garage is full. No available tickets.")

    def pay_for_parking(self):
        """
        Asks user for how many hours they stayed, calculates against hourly rate.
        Determines if payment is paid in full and returns True on ticket status.
        """
        paid_in_full = False

        while not paid_in_full:
            self.hours_stayed = int(
                input("How many hours did you stay? Please be honest...\n")
            )
            self.cust_total = self.rate_hourly * self.hours_stayed
            print(f"Your total is: ${self.cust_total}")
            self.payment = int(
                input(
                    "Please insert your payment: (Bills accepted: $5, $10, $20, $50, $100)\n"
                )
            )

            if self.payment == self.cust_total:
                print("Ticket has been paid. You have 15 minutes to leave")
                self.current_tickets.update({"Paid": True})
                paid_in_full = True

            elif self.payment > self.cust_total:
                print("Please take your change.")
                self.current_tickets.update({"Paid": True})
                paid_in_full = True

            elif self.payment < self.cust_total:
                while self.payment != self.cust_total:
                    print("Not enough money! You can't leave until you pay me.")
                    self.payment_addl = int(
                        input(
                            f"${self.cust_total - self.payment} left due. (Bills accepted: $5, $10, $20, $50, $100)\n"
                        )
                    )
                    if (self.payment_addl + self.payment) == self.cust_total:
                        print("Ticket has been paid. You have 15 minutes to leave.")
                        self.current_tickets.update({"Paid": True})
                        paid_in_full = True
                        break
                    else:
                        self.payment += self.payment_addl
                        continue

    def leave_garage(self):
        """
        If ticket was paid in full, reassign space to available and adds ticket to pool.
        Lets person escape garage.
        """
        if True in self.current_tickets.values():
            self.tickets_avail += 1
            self.spaces_taken.remove(self.assign_space)
            self.spaces_avail.append(self.assign_space)
            print(self.spaces_avail)
            print("Thank you, have a wonderful day! :)")


fams = ParkingGarage()
fams.take_ticket()
fams.pay_for_parking()
fams.leave_garage()
