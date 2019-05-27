import taxxLexico
import codecs
import ply.lex as lex

class Taxx(object):
	"""docstring for Taxx"""
	def __init__(self):
		super(Taxx, self).__init__()
	
	def compilar(self,archivo):	
		fp=codecs.open(archivo,'r')
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
		