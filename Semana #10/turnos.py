# -*- coding: utf-8 -*-

from time import sleep

def turnos(numero_jugadores, modo):
	lista_jugadores = ["Jugador " + str(x + 1) for x in range(numero_jugadores)] # List Comprehensions
	
	if modo == 0:
		control_turnos_recursivo(lista_jugadores, 0, numero_jugadores)
	elif modo == 1:
		control_turnos_iterativo(lista_jugadores, numero_jugadores)
	else:
		print("Modo no válido")

def control_turnos_recursivo(lista_jugadores, inicio, numero_jugadores):
	turno = inicio % numero_jugadores
	print(lista_jugadores[turno])
	sleep(1) # Espera
	control_turnos_recursivo(lista_jugadores, inicio + 1, numero_jugadores)

def control_turnos_iterativo(lista_jugadores, numero_jugadores):
	turno = 0
	while True:
		print(lista_jugadores[turno % numero_jugadores])
		time.sleep(1) # Espera
		turno += 1

numero_jugadores = 5
modo = 0
turnos(numero_jugadores, modo)