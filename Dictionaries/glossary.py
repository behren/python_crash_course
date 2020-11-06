programming_words = {
    'string': 'a conjunction of words (can contain blanks)',
    'int': 'a whole number',
    'float': 'a floating point number',
    'loop': 'a "loop" that runs under certain conditions',
    'boolean': 'is either true or false',
    }

for word in programming_words:
    print(f"{word.title()}:\n {programming_words[word].title()}\n")