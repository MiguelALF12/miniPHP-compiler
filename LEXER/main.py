# This is a sample Python script.

# Press ⌥⇧R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import PHPlexer
import ply.lex as lexer

# Tests

def test(data, builtLexer):
    builtLexer.input(data)
    while True:
        tok = builtLexer.token()
        if not tok:
            break
        print(tok)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Reading arguments from command line
    # if we pass more than one argument, the only string that will be caught is test.txt
    # Example of what you don't have to pass: python3 test.txt <filename> ...

    if len(sys.argv) > 1:
        fin = sys.argv[1]
    else:
        testNumber = 1 # Change to 1 to test test1.txt or 2 to test test2.txt
        fin = f'./LEXER/tests/test{testNumber}.txt'
    f = open(fin, 'r')
    data = f.read()
    print(data)
    #Build the lexer
    miniPHP = lexer.lex(module=PHPlexer)
    test(data, miniPHP)

    # input()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
