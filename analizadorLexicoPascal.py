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
reservadas = {'AND':'and',
    'ARRAY':'array',
    'BEGIN':'begin',
    'CASE':'case',
    'CONST':'const',
    'DIV':'div',
    'DO':'do',
    'DOWNTO':'downto',
    'ELSE':'else',
    'END':'end',
    'FILE':'file',
    'FOR':'for',
    'FUNCTION':'function',
    'GOTO':'goto',
    'IF':'if',
    'IN':'in',
    'LABEL':'label',
    'MOD':'mod',
    'NIL':'nil',
    'NOT':'not',
    'OF':'of',
    'OR':'or',
    'PACKED':'packed',
    'PROCEDURE':'procedure',
    'PROGRAM':'program',
    'RECORD':'record',
    'REPEAT':'repeat',
    'SET':'set',
    'THEN':'then',
    'TO':'to',
    'TYPE':'type',
    'UNTIL':'until',
    'VAR':'var',
    'WHILE':'while',
    'WITH':'with',
    }

# se agregan las palabras reservadas a la lista de tokens
tokens = tokens+list(reservadas.values())

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




def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_d]*'
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
    r"\'[^']\'"
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
		fin = 'holamundo.pas'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()

