players = ['reus', 'haaland', 'guerreiro', 'brandt', 'hummels']
print(players)
print(players[0])
print(players[-2])

print(f"Mein Lieblingsspieler ist {players[1].title()}.")

players[3] = "hazard"
print(players)

players.append("brandt")
print(players)

players.insert(0, "dede")
print(players)

del players[0]
print(players)

legende = players.pop(0)
print(players)
print(f"{legende.title()} ist eine Dortmunder Legende.")

players.remove("brandt")
print(players)

print(sorted(players))
print(players)

players.reverse()
print(players)

players.reverse()
print(players)

print(len(players))

print(players[3])