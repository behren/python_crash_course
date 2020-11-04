guests = ['Gandalf', 'Frodo', 'Gimli']
print(f"Hallo {guests[0]}, hiermit lade ich dich herzlich zu meiner Party ein!")
print(f"Hallo {guests[1]}, hiermit lade ich dich herzlich zu meiner Party ein!")
print(f"Hallo {guests[2]}, hiermit lade ich dich herzlich zu meiner Party ein!")

unavailable_guest = guests.pop(1)
print(f"{unavailable_guest} schafft es leider nicht zu der Party.")

guests.append("Aragorn")
print(f"Hallo {guests[0]}, hiermit lade ich dich herzlich zu meiner Party ein!")
print(f"Hallo {guests[1]}, hiermit lade ich dich herzlich zu meiner Party ein!")
print(f"Hallo {guests[2]}, hiermit lade ich dich herzlich zu meiner Party ein!")

print("Hallo zusammen, ich habe einen größeren Dinnertisch gefunden und kann nun mehr Gäste einladen!")

guests.insert(0, "Baumbart")
guests.insert(1, "Legolas")
guests.append("Boromir")

print(f"Hallo {guests[0]}, hiermit lade ich dich herzlich zu meiner Party ein!")
print(f"Hallo {guests[1]}, hiermit lade ich dich herzlich zu meiner Party ein!")
print(f"Hallo {guests[2]}, hiermit lade ich dich herzlich zu meiner Party ein!")
print(f"Hallo {guests[3]}, hiermit lade ich dich herzlich zu meiner Party ein!")
print(f"Hallo {guests[4]}, hiermit lade ich dich herzlich zu meiner Party ein!")
print(f"Hallo {guests[5]}, hiermit lade ich dich herzlich zu meiner Party ein!")

print(f"Dann sind wir {(len(guests))} Gäste!")

print("Hey zusammen, leider hat sich herausgestellt, dass ich nur Platz für zwei von euch haben werde!")

removed_guest = guests.pop(0)
message = f"Hallo, {removed_guest}, leider müssen wir die Party auf ein andermal verschieben!"
print(message)

removed_guest = guests.pop(0)
message = f"Hallo, {removed_guest}, leider müssen wir die Party auf ein andermal verschieben!"
print(message)

removed_guest = guests.pop(0)
message = f"Hallo, {removed_guest}, leider müssen wir die Party auf ein andermal verschieben!"
print(message)

removed_guest = guests.pop(0)
message = f"Hallo, {removed_guest}, leider müssen wir die Party auf ein andermal verschieben!"
print(message)

print(guests)

print(f"Hallo {guests[0]}, du bist noch immer eingeladen, ich freue mich auf dich!")
print(f"Hallo {guests[1]}, du bist noch immer eingeladen, ich freue mich auf dich!")

del guests[0]
del guests[0]

print(guests)