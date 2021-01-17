from lottery import Lottery

possibilities = [
    "A",
    "B",
    "N",
    "Q",
    "X",
    "9",
    "3",
    "6",
    "8",
    "19",
    "1",
    "0",
    "4",
    "16",
    "10",
]

plays = 0
won = False

ticket = Lottery(possibilities)
my_ticket = ticket.draw_ticket()

while not won:
    new_ticket = ticket.draw_ticket()
    won = ticket.check_ticket(my_ticket, new_ticket)
    plays += 1
    if won:
        print(f"You won and it took only {plays} plays!")
        print("Congratulations!")
        print(f"Your ticket: {my_ticket}")
        print(f"Winning ticket: {new_ticket}")
    else:
        print(f"Losing ticket: {new_ticket}")
        print(f"You didn't win yet, let's draw another one.")