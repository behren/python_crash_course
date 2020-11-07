programming_words = {
    'string': 'a conjunction of words (can contain blanks)',
    'int': 'a whole number',
    'float': 'a floating point number',
    'loop': 'a "loop" that runs under certain conditions',
    'boolean': 'is either true or false',
    'dictionary': 'contains keys and values',
    'while loop': 'runs as long as a condition is true',
    'for loop': 'runs through a list of conditions',
    'set': 'groups redundant keys and values in a dictionary',
    'print()': 'prints a string',
    }

for key, value in programming_words.items():
    print(f"{key.title()}:\n    {value.title()}\n")
