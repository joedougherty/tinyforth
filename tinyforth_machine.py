def execute(word, input_list_ref):
    if callable(DICTIONARY[word]): # Internally defined
        try:
            DICTIONARY[word]()
        except IndexError:
            print("Empty stack!!!")
    elif isinstance(DICTIONARY[word], list): # User-defined
        fn_list = copy(DICTIONARY[word])
        interpret(fn_list)
    else:
        print("`{}` is not a word I know about!".format(word))


def interpret(input_list):
    while input_list:
        word = input_list.pop(0)

        if is_a_literal(word):      # Push literals
            push_literal(word)
        elif word in DICTIONARY:    # Execute word
            execute(word, input_list_ref)
        else:
            print("I don't know what to do with `{}`!".format(word))


if __name__ == '__main__':
    while True:
        try:
            interpret(tokenize('tinyforth> '))
            print('ok')
        except KeyboardInterrupt:
            print('')
        except EOFError:
            print('')
            sys.exit(0)
