import os
import re
import codecs
import ply.lex as lex 


tokens = ['ID','NUMBER','PLUS','MINUS',
'TIMES','DIVIDE','ODD','ASSIGN','NE','LT','LTE','GT','GTE','LPARENT',
'RPARENT','COMMA','SEMMICOLOM','DOT','UPDATE']

reservadas=['ARK','PRT','AJA','TONCE','DURANTE','PRUEBA','GRITO','COMPLETO','SIEMPRE','PROCEDE','JUERA','METIO']

#reservadas{'ark':'ARK',#Arranca (begin)
#	'prt':'PRT',#Perate (end)
#	'aja':'AJA',#ajá (if)
#	'tonce':'TONCE',#entonces(then)
#	'durante':'DURANTE',#while
#	'prueba':'PRUEBA',#do
#	'grito':'GRITO',#llama(call)
#	'completo':'COMPLETO',#Entero(int)
#	'siempre':'SIEMPRE',#Constante(const)
#	'procede':'PROCEDE',#hagale(procedure)
#	'juera':'JUERA',#Out
#	'metio':'METIO',#IN	
#	}

#tokens = tokens+list(reservadas.values())
tokens = tokens+reservadas

t_ignore = '\t'
t_PLUS = r'\+'
t_ASSIGN = r'='
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='

def t_ID(t):
	r'~[a-zA-Z_](" ")?[a-zA-Z0-9_]*(\n)?'
	if t.value.upper() in tokens:
 		t.value = t.value.upper()
 		t.type = t.value
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

#dsfjksdlgjklsdgjsdgslxcvjlk-,.
def t_COMMENT(t):
	r'\#.*'
	pass

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print( "caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)


class Taxx():		
	def compilar(self,archivo):	
		fp=codecs.open(archivo,"r","utf-8")
		texto=fp.read()
		analizador=lex.lex()
		i=0
		analizador.input(texto)
		print('['+'/'*i + ']',i,'%', end='\r')
		while True:
			tok = analizador.token()
			if not tok:
				break
			else:			
				i=i+1
				print('\n',tok)
				print('['+'/'*i + ']',i,'%', end='\r')
		fp.close()


