# ------------------------------------------------------------
# PHPlexer.py
#
# tokenizer for a PHP-like syntax
# This module just contains the lexing rules
# ------------------------------------------------------------

#Token lists

reserved = {
#Keywords
    "ABSTRACT": "ABSTRACT",
    "BREAK": "BREAK",
    "ARRAY": "ARRAY",
    "CALLABLE": "CALLABLE",
    "CASE": "CASE",
    "CATCH": "CATCH",
    "CLASS": "CLASS",
    "CLONE": "CLONE",
    "CONST": "CONST",
    "CONTINUE": "CONTINUE",
    "DECLARE": "DECLARE",
    "DEFAULT": "DEFAULT",
    "DIE": "DIE",
    "DO": "DO",
    "ECHO": "ECHO",
    "ELSE": "ELSE",
    "ELSEIF": "ELSEIF",
    "EMPTY": "EMPTY",
    "ENDDECLARE": "ENDDECLARE",
    "ENDFOR": "ENDFOR",
    "ENDFOREACH": "ENDFOREACH",
    "ENDIF": "ENDIF",
    "ENDSWITCH": "ENDSWITCH",
    "ENDWHILE": "ENDWHILE",
    "EVAL": "EVAL",
    "EXIT": "EXIT",
    "EXTENDS": "EXTENDS",
    "FINAL": "FINAL",
    "FINALLY": "FINALLY",
    "FN": "FN",
    "FOR": "FOR",
    "FOREACH": "FOREACH",
    "FUNCTION": "FUNCTION",
    "GLOBAL": "GLOBAL",
    "GOTO": "GOTO",
    "IF": "IF",
    "IMPLEMENTS": "IMPLEMENTS",
    "INCLUDE": "INCLUDE",
    "INCLUDE_ONCE": "INCLUDE_ONCE",
    "INSTANCEOF": "INSTANCEOF",
    "INSTEADOF": "INSTEADOF",
    "INTERFACE": "INTERFACE",
    "ISSET": "ISSET",
    "LIST": "LIST",
    "MATCH": "MATCH",
    "NAMESPACE": "NAMESPACE",
    "NEW": "NEW",
    "OR": "OR",
    "PRINT": "PRINT",
    "PRIVATE": "PRIVATE",
    "PROTECTED": "PROTECTED",
    "PUBLIC": "PUBLIC",
    "READONLY": "READONLY",
    "REQUIRE": "REQUIRE",
    "REQUIRE_ONCE": "REQUIRE_ONCE",
    "RETURN": "RETURN",
    "STATIC": "STATIC",
    "SWITCH": "SWITCH",
    "THROW": "THROW",
    "TRAIT": "TRAIT",
    "TRY": "TRY",
    "UNSET": "UNSET",
    "USE": "USE",
    "VAR": "VAR",
    "WHILE": "WHILE",
    "XOR": "XOR",
    "YIELD": "YIELD",
    "INT": "INT",
    "FLOAT": "FLOAT",
    "BOOL": "BOOL",
    "TRUE": "TRUE",
    "FALSE": "FALSE",
    "NULL": "NULL",
    "VOID": "VOID",
    "ITERABLE": "ITERABLE",
    "OBJECT": "OBJECT",
    "MIXED": "MIXED",
    "NEVER": "NEVER",
}
tokens = [
    # Symbols
    'PLUS',
    'PLUSPLUS',
    'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    'MINUSEQUAL',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'DOT',
    'QUOTE',
    'DOUBLEQUOTE',
    # 'DOLLARSIGN',
    'QUESTIONMARK',
    #Others
    "ID",
    "NUMBER",
    "STRING"
] + list(reserved.values())

#Token definition

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_LESS = r'<'
t_GREATER = r'>'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_QUOTE = r'\''
t_DOUBLEQUOTE = r'\"'
# t_DOLLARSIGN = r'\$'
t_QUESTIONMARK = r'\?'

def t_ID(t):
    r'\$?[a-zA-Z_][a-zA-Z_0-9]*'
    # TODO: With the example: fuction fibo() {}, the lexer should recognize fuction as ID?. or as a error?
    #       Or this would go on parser?
    t.type = reserved.get(t.value.upper(),'ID')
    return t

def t_NUMBER(t):
    # r'\d+^[a-zA-Z0-9_](\.\d+)?((E|e)(-|\+)?\d+(\.\d+)?)?'
    r'\d(\.\d +)?((E | e)(- |\+)?\d + (\.\d+)?)?'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value
    return t

def t_LESSEQUAL(t):
    r'<='
    return t


def t_GREATEREQUAL(t):
    r'>='
    return t


def t_DEQUAL(t):
    r'!='
    return t


def t_ISEQUAL(t):
    r'=='
    return t


def t_MINUSMINUS(t):
    r'--'
    return t


def t_PLUSPLUS(t):
    r'\+\+'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    # print(t.value)
    print("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)
