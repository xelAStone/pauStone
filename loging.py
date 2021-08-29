import time
import sqlite3
timpo=time.ctime()
print(timpo)
def funcion(tiempo=0,resultado=None):
	while True:
		print('login user and password')
		usuario=input('User name --> : ')
		password=input('User password --> : ')
		tiempo=tiempo+1
		if tiempo >= 3:
			print('lo siento se te acabaron tus intentos perro')
			break
		dato={}
		dato[password]=dato
#		return dato
		print(dato)
funcion()
def sqlite():
	conexion=sqlite3.connect('/home/kali/Desktop','base.db')
	cursor=conexion.cursor()
	cursor.execute('''CREATE TABLE USER(Pasword VARCHAR(20)''')
	cursor.close()
	pass
def guardar(dato):
	conexion=sqlite3.connect('/home/kali/Desktop','base.db')
	pass
