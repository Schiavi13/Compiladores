import ply.lex as lex
import sys

# list of tokens
tokens = [
    # Simbolos
    'PLUS', #suma +
    'MINUS', #resta -
    'TIMES', #por *
    'DIVIDE', #division /
    'EQUAL', #igual =
    'LESSER', #menor que <
    'GREATER', #mayor que >
    'LBRACKET', #cuadrado [
    'RBRACKET', #cuadrado ]
    'DOT', #punto .
    'COMMA', #coma ,
    'LPAREN', #parentesis (
    'RPAREN', #parentesis )
    'COLON', #dos puntos :
    'SEMICOLON', #punto y coma ;
    'POINTER', #se utiliza elevado ^
    'AT', #arroba @ se utiliza para punteros
    'LBRACE', #llave {
    'RBRACE', #llave }
    'DOLLAR', #peso $
    'NUMSIGN', #numeral #
    'AMPERSAND', #and per se and &
    'PERCENT', #porcentaje %
    'BACKQUOTE',#tilde invertida `
    'WHITESPACE', #espacio en blanco
    'TILDE', #virgulilla ~
    'BAR', #barra |
    'EXCLAMATION', #exclamacion !
    'ISNOTEQ', #no es igual <>
    'GREATEREQ', #mayor o igual >=
    'LESSEREQ', #menor o igual <=
    'LSHIFT', #binary left shift <<
    'RSHIFT', #binart right shift >>
    'SUBRANGE', #operador subrango doble punto ..
    'ASSIGN', #se usa := para asignar valores
    'QUOTE', #comilla '

    # otros
    'ID',
    'NUMBER',   
]

# Segun la documentacion de ply es mejor definir las palabras reservadas aparte 
reservadas = ['AND',
    'ARRAY',
    'BEGIN',
    'CASE',
    'CONST',
    'DIV',
    'DO',
    'DOWNTO',
    'ELSE',
    'END',
    'FILE',
    'FOR',
    'FUNCTION',
    'GOTO',
    'IF',
    'IN',
    'LABEL',
    'MOD',
    'NIL',
    'NOT',
    'OF',
    'OR',
    'PACKED',
    'PROCEDURE',
    'PROGRAM',
    'RECORD',
    'REPEAT',
    'SET',
    'THEN',
    'TO',
    'TYPE',
    'UNTIL',
    'VAR',
    'WHILE',
    'WITH',
]

# se agregan las palabras reservadas a la lista de tokens
tokens = tokens+reservadas

t_ignore = '\t'
# Expresiones regulares para tokens atomicos
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_LESSER   = r'<'
t_GREATER = r'>'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOT = r'\.'
t_COMMA  = r',' 
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_COLON   = r':'
t_SEMICOLON = r';'
t_POINTER = r'\^'
t_AT = r'@'
t_LBRACE   = r'\{'
t_RBRACE   = r'\}'
t_DOLLAR = r'\$'
t_NUMSIGN = r'\#'
t_AMPERSAND = r'&'
t_PERCENT = r'%'
t_BACKQUOTE = r'`'
t_WHITESPACE = r'\s+'
t_TILDE = r'~'
t_BAR = r'\|'
t_EXCLAMATION = r'!'
t_QUOTE = r'\''



def t_AND(t):
    r'and'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_BEGIN(t):
    r'begin'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CONST(t):
    r'const'
    return t

def t_DIV(t):
    r'div'
    return t

def t_DO(t):
    r'do'
    return t

def t_DOWNTO(t):
    r'downto'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_END(t):
    r'end'
    return t

def t_FILE(t):
    r'file'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_IF(t):
    r'if'
    return t

def t_IN(t):
    r'in'
    return t

def t_LABEL(t):
    r'label'
    return t

def t_MOD(t):
    r'mod'
    return t

def t_NIL(t):
    r'nil'
    return t

def t_NOT(t):
    r'not'
    return t

def t_OF(t):
    r'of'
    return t

def t_OR(t):
    r'or'
    return t

def t_PACKED(t):
    r'packed'
    return t

def t_PROCEDURE(t):
    r'procedure'
    return t

def t_PROGRAM(t):
    r'program'
    return t

def t_RECORD(t):
    r'record'
    return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_SET(t):
    r'set'
    return t

def t_THEN(t):
    r'then'
    return t

def t_TO(t):
    r'to'
    return t

def t_TYPE(t):
    r'type'
    return t

def t_UNTIL(t):
    r'until'
    return t

def t_VAR(t):
    r'var'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_WITH(t):
    r'with'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ISNOTEQ(t):
    r'<>'
    return t

def t_GREATEREQ(t):
	r'>='
	return t

def t_LESSEREQ(t):
	r'<='
	return t

def t_LSHIFT(t):
    r'<<'
    return t

def t_RSHIFT(t):
    r'>>'
    return t

def t_SUBRANGE(t):
    r'\.\.'
    return t

def t_ASSIGN(t):
    r':='
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_d]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_comentario_multi(t):
    r'\(\*(.|\n)*?\*\) | \{(.|\n)*?\}'
    t.lexer.lineno += t.value.count('\n')

def t_comentario_simple(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

def t_cadena(t):
    #r"\'[^']\'"
    r"\'([^'])*'"
    pass

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)




def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'fibo.pas'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()

