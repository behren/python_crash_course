files = ["cats.txt", "dogs.txt"]

for filename in files:
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except:
        # FileNotFoundError(print(f"The file {filename} doesn't exist."))
        pass
    else:
        if filename == "cats.txt":
            print(f"The names of the cats are: \n{contents.title()}")
        if filename == "dogs.txt":
            print(f"The names of the dogs are: \n{contents.title()}")