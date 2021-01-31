filename = "data/learning_python.txt"

with open(filename) as textfile:
    content = textfile.read()
print(content)

with open(filename) as textfile:
    for line in textfile:
        print(line.strip())

with open(filename) as textfile:
    lines = textfile.readlines()

python_lines = ""
for line in lines:
    python_lines += line.lstrip()
print(python_lines)