# -*- coding: utf-8 -*-

from random import shuffle

def cartas(simbolos, total_cartas):
	cartas_por_simbolo = total_cartas // len(simbolos)

	numero_carta = 0
	baraja = []

	for i in simbolos:
		for j in range(cartas_por_simbolo):
			baraja.append(str(j + 1) + i)

	shuffle(baraja)
	return baraja

simbolos = ['A', 'X', 'Y', 'B']
total_cartas = 52
print(cartas(simbolos, total_cartas))