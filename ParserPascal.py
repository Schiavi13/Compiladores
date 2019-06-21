import ply.yacc as yacc
from analizadorLexicoPascal import tokens
import analizadorLexicoPascal
import sys

VERBOSE = 1

def p_program_i(p):
    'program_i : PROGRAM identifier SEMICOLON block DOT'
    pass

def p_block(p):
    'block : variable_declaration_part procedure_or_function statement_part'
    pass

def p_variable_declaration_part(p):
    """variable_declaration_part : VAR variable_declaration_list
                                | empty
    """
    pass

def p_variable_declaration_list(p):
    """variable_declaration_list : variable_declaration variable_declaration_list
                                | variable_declaration
    """
    pass

def p_variable_declaration(p):
    'variable_declaration : identifier COLON type SEMICOLON'
    pass

def p_procedure_or_function(p):
    """procedure_or_function : proc_or_func_declaration SEMICOLON procedure_or_function
                            | empty
    """
    pass

def p_proc_or_func_declaration(p):
    """proc_or_func_declaration : procedure_declaration
                                | function_declaration
    """
    pass

def p_procedure_declaration(p):
    'procedure_declaration : procedure_heading SEMICOLON block'
    pass

def p_procedure_heading(p):
    """procedure_heading : PROCEDURE identifier
                        | PROCEDURE identifier LPAREN parameter_list RPAREN
    """
    pass

def p_function_declaration(p):
    'function_declaration : function_heading SEMICOLON block'
    pass

def p_function_heading(p):
    """function_heading : FUNCTION type
                        | FUNCTION identifier COLON type
                        | FUNCTION identifier LPAREN parameter_list RPAREN COLON type
    """
    pass

def p_parameter_list(p):
    """parameter_list : parameter COMMA parameter_list
                    | parameter
    """
    pass

def p_parameter(p):
    'parameter : identifier COLON type'
    pass

def p_type(p):
    """type : TREAL
            | TINTEGER
            | TSTRING
            | TCHAR
    """
    pass

def p_statement_part(p):
    'statement_part : BEGIN statement_sequence END'
    pass

def p_statement_sequence(p):
    """statement_sequence : statement SEMICOLON statement_sequence
                        | statement
    """
    pass

def p_statement(p):
    """statement : assignment_statement
                | statement_part
                | if_statement
                | while_statement
                | repeat_statement
                | for_statement
                | procedure_or_function_call
                | empty
    """
    pass

def p_procedure_or_function_call(p):
    """procedure_or_function_call : identifier LPAREN param_list RPAREN
                                | identifier
    """
    pass

def p_param_list(p):
    """param_list : param_list COMMA param
                | param
    """
    pass

def p_param(p):
    'param : expression'
    pass

def p_if_statement(p):
    """if_statement : IF expression THEN statement ELSE statement
                    | IF expression THEN statement
    """
    pass

def p_while_statement(p):
    'while_statement : WHILE expression DO statement'
    pass

def p_repeat_statement(p):
    'repeat_statement : REPEAT statement UNTIL expression'
    pass

def p_for_statement(p):
    """for_statement : FOR assignment_statement TO expression DO statement
                    | FOR assignment_statement DOWNTO expression DO statement
    """
    pass

def p_assignment_statement(p):
    'assignment_statement : identifier ASSIGN expression '
    pass

def p_expression(p):
    """expression : expression and_or expression_m
                | expression_m
    """
    pass

def p_expression_m(p):
    """expression_m : expression_s
                    | expression_m sign expression_s
    """
    pass

def p_expression_s(p):
    """expression_s : element
                    | expression_s psign element
    """
    pass

def p_and_or(p):
    """and_or : AND
            | OR
    """
    pass

def p_psign(p):
    """psign : TIMES
            | DIVIDE
    """
    pass

def p_sign(p):
    """sign : PLUS
            | MINUS
            | DIV
            | MOD
            | EQUAL
            | ISNOTEQ
            | LESSER
            | LESSEREQ
            | GREATER
            | GREATEREQ
    """
    pass

def p_element(p):
    """element : identifier
                | real
                | integer
                | string
                | char
                | LPAREN expression RPAREN
                | NOT element
                | function_call_inline
    """
    pass

def p_function_call_inline(p):
    'function_call_inline : identifier LPAREN param_list RPAREN'
    pass

def p_identifier(p):
    'identifier : ID'
    pass

def p_real(p):
    'real : REAL'
    pass

def p_integer(p):
    'integer : INTEGER'
    pass

def p_string(p):
    'string : STRING'
    pass

def p_char(p):
    'char : CHAR'
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')



parser = yacc.yacc()

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'pruebaParserPascal.pas'
    f = open(fin, 'r')
    data = f.read()
	#print (data)
    parser.parse(data, tracking=True)
    print("El parcero reconoce todo")

