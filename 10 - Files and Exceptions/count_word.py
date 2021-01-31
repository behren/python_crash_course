filename = "data/DerSchatzImSilbersee.txt"
word = "die"

try:
    with open(filename, encoding="utf-8") as f:
        content = f.read()
except:
    FileNotFoundError(print(f"The file '{filename}' does not exist"))
else:
    occurances = content.lower().count(word)
    print(f"The word '{word}' occured {occurances} times.")