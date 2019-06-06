import ply.yacc as yacc
from calclexer import tokens
import calclexer
import sys

VERBOSE = 1

def p_exp1(p):
    '''exp1 : exp1 PLUS exp2
            | exp1 MINUS exp2
            | exp2
    '''

def p_exp2(p):
    '''exp2 : exp2 TIMES exp3
            | exp2 DIVIDE exp3
            | exp3
    '''

def p_exp3(p):
    '''exp3 : LPAREN exp1 RPAREN
            | NUMBER
    '''

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
        fin = 'pruebacalc.txt'
    f = open(fin, 'r')
    data = f.read()
	#print (data)
    parser.parse(data, tracking=True)
    print("El parcero reconoce todo")
