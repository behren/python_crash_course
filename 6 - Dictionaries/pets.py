bijou = {
    "kind": "dog",
    "owner": "niclas",
}

plötze = {
    "kind": "horse",
    "owner": "geralt",
}

brutus = {
    "kind": "hound",
    "owner": "hades",
}

pets = [bijou, plötze, brutus]

for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['kind'].title()}")
