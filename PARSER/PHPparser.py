import ply.yacc as yacc
import LEXER.PHPlexer as phplexer
from LEXER.PHPlexer import tokens
import sys

VERBOSE = 1


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
				   | fun_declaration
				   | area fun_declaration
				   | header_declaration
				   | class_declaration
				   | echo_stmt
				   | selection_stmt
			       | iteration_stmt
				   | typeclass
	'''
	pass


def p_echo_stmt(p):
	'''echo_stmt : echo_stmt ECHO STRING SEMICOLON
				 | echo_stmt ECHO IDVAR SEMICOLON
				 | echo_stmt ECHO NUMBER SEMICOLON
				 | echo_stmt ECHO boolean SEMICOLON
				 | echo_stmt ECHO fun_declaration SEMICOLON
				 | empty
	'''
	pass


def p_header_declaration(p):
	'''header_declaration : REQUIRE LPAREN STRING RPAREN SEMICOLON
                          | INCLUDE LPAREN STRING RPAREN SEMICOLON
    '''
	pass


def p_class_declaration(p):
	'''class_declaration : area CLASS ID LBLOCK attribute RBLOCK
						 | CLASS ID LBLOCK attribute RBLOCK
	'''
	pass


def p_attribute1(p):
	'''attribute : attribute area var_declaration
				 | area var_declaration
				 | attribute area fun_declaration
				 | area fun_declaration
	'''
	pass


def p_area(p):
	'''area : PRIVATE
			| PUBLIC
			| PROTECTED
	'''
	pass


def p_var_declaration(p):
	'''var_declaration : IDVAR SEMICOLON var_declaration
                       | IDVAR SEMICOLON
                       | TIMESTIMES IDVAR SEMICOLON
                       | TIMESTIMES IDVAR SEMICOLON var_declaration
                       | IDVAR EQUAL NUMBER SEMICOLON var_declaration
                       | IDVAR EQUAL NUMBER SEMICOLON
                       | IDVAR EQUAL boolean SEMICOLON var_declaration
                       | IDVAR EQUAL boolean SEMICOLON
                       | IDVAR EQUAL IDVAR SEMICOLON var_declaration
                       | IDVAR EQUAL IDVAR SEMICOLON
                       | AMPERSANT IDVAR SEMICOLON var_declaration
                       | AMPERSANT IDVAR EQUAL IDVAR SEMICOLON  selection_stmt
                       | AMPERSANT IDVAR SEMICOLON
                       | IDVAR EQUAL simple_expression SEMICOLON
	'''
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
			     | return_stmt
			     | class_declaration
				 | echo_stmt
	'''
	pass


def p_expression_stmt(p):
	'expression_stmt : expression SEMICOLON'
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
	'iteration_stmt : FOR LPAREN var_declaration SEMICOLON expression SEMICOLON additive_expression RPAREN statement'
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


def p_expression(p):
	'''expression : var EQUAL expression
				  | simple_expression
				  | var EQUAL AMPERSANT IDVAR
			      | expression AND expression
				  | expression OR expression
	'''
	pass


def p_var(p):
	'''var : IDVAR
		   | IDVAR LBRACKET expression RBRACKET
	'''
	pass


def p_simple_expression(p):
	'''simple_expression : additive_expression relop additive_expression
						 | additive_expression
	'''
	pass


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


def p_additive_expression(p):
	'''additive_expression : additive_expression addop term
    					   | term
    					   | term MINUSMINUS
    				       | term PLUSPLUS
	'''
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
			  | IDVAR LPAREN args RPAREN
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


def p_boolean(p):
	'''boolean : TRUE
			   | FALSE
	'''
	pass


def p_tclass(p):
	'typeclass : ID IDVAR EQUAL NEW constructor SEMICOLON'
	pass


def p_costructor(p):
	'''constructor : ID LPAREN RPAREN
				   | ID LPAREN args RPAREN
	'''
	pass


def p_empty(p):
	'empty :'
	pass


def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(phplexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')


phpparser = yacc.yacc()
