import sys
import LEXER.PHPlexer as phplexer
import PARSER.PHPparser as phpparser
import ply.lex as lexer
import ply.yacc as yacc

def testLexer(data, builtLexer):
    print("========= TESTEANDO LEXER =========")
    print("Salida: ")
    builtLexer.input(data)
    while True:
        tok = builtLexer.token()
        if not tok:
            break
        print(tok)
    print("===================================\n\n")


def testParser(data, builtParser):
    print("========= TESTEANDO PARSER =========")
    print("Entrada:")
    print(data)
    builtParser.parse(data, debug=True)
    print(None if phpparser.ERROR else "\n\n -----> FELICIDADES. Su codigo no tiene errores!")
    print("===================================\n\n")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Reading arguments from command line
    # if we pass more than one argument, the only string that will be caught is test.txt
    # Example of what you don't have to pass: python3 test.txt <filename> ...
    if len(sys.argv) > 1:
        fin = sys.argv[1]
    else:
        testNumber = 1  # Change to 1 to test test1.txt or 2 to test test2.txt
        fin = f'tests/test{testNumber}.txt'
    f = open(fin, 'r')
    data = f.read()
    testLexer(data, phplexer.phplexer)
    testParser(data, phpparser.phpparser)
