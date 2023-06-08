import ply.yacc as yacc
import LEXER.PHPlexer as phplexer
from LEXER.PHPlexer import tokens
import sys

VERBOSE = 1
ERROR = False
NUMBEROFERRORS = 0

precedence = (
    # ('left', 'INCLUDE', 'REQUIRE'),
    ('left', 'COMMA'),
    ('right', 'EQUAL', 'PLUSEQUAL', 'MINUSEQUAL'),
    ('left', 'SEMICOLON'),
    ('left', 'OR'),
    ('left', 'XOR'),
    ('left', 'AND'),
    ('nonassoc', 'ISEQUAL', 'DEQUAL'),
    ('nonassoc', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('right', 'LBRACKET'),
    ('nonassoc', 'NEW', 'CLONE'),
    ('left', 'ELSEIF'),
    ('left', 'ELSE'),
    ('right', 'PRIVATE', 'PROTECTED', 'PUBLIC'),
)


def p_program(p):
    'program : OPENTAG declaration_list CLOSETAG'
    pass


def p_declaration_list(p):
    '''declaration_list : declaration_list  declaration
                           | declaration
    '''
    pass


def p_declaration(p):
    '''declaration : var_declaration
                | echo_stmt
                | selection_stmt
			    | iteration_stmt
                | fun_declaration
				| header_declaration
	'''
    pass


def p_echo_stmt(p):
    '''echo_stmt : echo_stmt ECHO data_type SEMICOLON
                | echo_stmt ECHO IDVAR SEMICOLON
                | echo_stmt ECHO fun_declaration SEMICOLON
                | empty
	'''


def p_boolean(p):
    '''boolean : TRUE
			   | FALSE
	'''
    pass


def p_var_declaration_1(p):
    'var_declaration : var_declaration2 SEMICOLON'


def p_var_declaration_2(p):
    '''var_declaration2 : IDVAR var_declaration2
                | IDVAR
                | TIMESTIMES IDVAR
                | TIMESTIMES IDVAR var_declaration2
                | IDVAR EQUAL data_type var_declaration2
                | IDVAR EQUAL data_type
                | IDVAR EQUAL IDVAR var_declaration2
                | IDVAR EQUAL IDVAR
                | AMPERSANT IDVAR var_declaration2
                | AMPERSANT IDVAR EQUAL IDVAR  var_declaration2
                | AMPERSANT IDVAR EQUAL IDVAR
                | AMPERSANT IDVAR
                | IDVAR EQUAL simple_expression
	'''
    pass


def p_datatype_1(p):
    'data_type : NUMBER'
    pass


def p_datatype_2(p):
    'data_type : boolean'
    pass


def p_datatype_3(p):
    'data_type : STRING'
    pass


def p_fun_declaration(p):
    '''fun_declaration : FUNCTION ID LPAREN params RPAREN
					   | FUNCTION ID LPAREN params RPAREN compount_stmt
	'''
    pass


def p_params(p):
    '''params : param_list
			  | empty
	'''
    pass


def p_param_list(p):
    '''param_list : param_list COMMA param_list
				  | param
	'''
    pass


def p_param(p):
    '''param : IDVAR
             | IDVAR LBRACKET RBRACKET
    '''
    pass


def p_compount_stmt(p):
    'compount_stmt : LBLOCK echo_stmt local_declarations echo_stmt statement_list echo_stmt RBLOCK'
    pass


def p_local_declarations(p):
    '''local_declarations : local_declarations var_declaration
						  | empty
	'''
    pass


def p_statement_list(p):
    '''statement_list : statement_list statement
					  | empty
	'''
    pass


def p_statement(p):
    '''statement : expression_stmt
				| compount_stmt
				| selection_stmt
				| iteration_stmt
				| echo_stmt
				| return_stmt
	'''
    pass


def p_expression_stmt(p):
    '''expression_stmt : expression SEMICOLON
					| SEMICOLON
	'''
    pass


def p_selection_stmt_1(p):
    '''selection_stmt : IF LPAREN expression RPAREN statement
					  | IF LPAREN expression RPAREN statement selection
	'''
    pass


def p_selection(p):
    '''selection : ELSE statement
				 | ELSEIF statement selection
	 '''
    pass


def p_selection_stmt_2(p):
    '''selection_stmt : SWITCH LPAREN var RPAREN statement
					  | CASE NUMBER COLON statement BREAK SEMICOLON
					  | DEFAULT COLON statement BREAK SEMICOLON
	'''
    pass


def p_iteration_stmt_1(p):
    'iteration_stmt : FOR LPAREN var_declaration2 SEMICOLON expression SEMICOLON additive_expression RPAREN statement '
    pass


def p_iteration_stmt_2(p):
    'iteration_stmt : WHILE LPAREN expression RPAREN statement'
    pass


def p_iteration_stmt_3(p):
    'iteration_stmt : DO LBLOCK statement SEMICOLON RBLOCK WHILE LPAREN expression RPAREN'
    pass


def p_return_stmt(p):
    '''return_stmt : RETURN SEMICOLON
				   | RETURN expression SEMICOLON
	'''
    pass


def p_expression_1(p):
    'expression : var EQUAL expression'
    pass


def p_expression_2(p):
    r'expression : simple_expression'
    pass


def p_expression_3(p):
    r'expression : var EQUAL AMPERSANT IDVAR'
    pass


def p_expression_4(p):
    r'expression : expression logic_operator expression'
    pass


def p_logic_operator(p):
    '''
	logic_operator : AND
					| OR
					| XOR
	'''
    pass


def p_var(p):
    '''var : IDVAR
		   | IDVAR LBRACKET expression RBRACKET
	'''
    pass


def p_simple_expression_1(p):
    'simple_expression : additive_expression relop additive_expression'
    pass


def p_simple_expression_2(p):
    'simple_expression : additive_expression'


def p_relop(p):
    '''relop : LESS
			 | LESSEQUAL
			 | GREATER
			 | GREATEREQUAL
			 | DEQUAL
			 | DISTINT
			 | ISEQUAL
	'''
    pass


def p_additive_expression_1(p):
    'additive_expression : additive_expression addop term'
    pass


def p_additivie_expression_2(p):
    'additive_expression : term'
    pass


def p_additive_expression_3(p):
    'additive_expression : term MINUSMINUS'
    pass


def p_additive_expression_4(p):
    'additive_expression : term PLUSPLUS'
    pass


def p_addop(p):
    '''addop : PLUS
			 | MINUS
	'''
    pass


def p_term(p):
    '''term : term mulop factor
			| factor
	'''
    pass


def p_mulop(p):
    '''mulop : TIMES
			 | DIVIDE
	'''
    pass


def p_factor(p):
    '''factor : LPAREN expression RPAREN
			  | var
			  | NUMBER
			  | boolean
			  | ID LPAREN args RPAREN
	'''
    pass


def p_args(p):
    '''args : args_list
			| empty
			| VOID
	'''
    pass


def p_args_list(p):
    '''args_list : args_list COMMA expression
				 | expression
	'''
    pass


def p_header_declaration(p):
    '''header_declaration : REQUIRE LPAREN STRING RPAREN SEMICOLON
                          | INCLUDE LPAREN STRING RPAREN SEMICOLON
    '''
    pass


def p_empty(p):
    'empty :'
    pass


# def p_error(p):
#     global ERROR
#     ERROR = True
#     if VERBOSE:
#         if p is not None:
#             print("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
#         else:
#             print("ERROR SINTACTICO EN LA LINEA: " + str(phplexer.lexer.lineno))
#     else:
#         raise Exception('syntax', 'error')

def p_error(p):
    global NUMBEROFERRORS, ERROR
    ERROR = True

    if VERBOSE:
        if p:
            NUMBEROFERRORS += 1
            print(f"Numero de errores: {NUMBEROFERRORS} - ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
         # Just discard the token and tell the parser it's okay.
            print()
            phpparser.errok()
    else:
         print("Syntax error at EOF")


phpparser = yacc.yacc()

