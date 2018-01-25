def tokenize(input_line):
    input_line = input_line.strip().  \
           replace('(', '( ').  \
           replace(')', ' )').  \
           replace(';', ' ; '). \
           split(' ')

    return [w for w in input_line if w != '']
