import sys
import math

n = 1000

for x in range(n):

	digits = []
	y = x**2

	while (y > 0):
		digits.append(y%10)
		y=y//10

	digits.reverse()
	
	sumOneDigit = 0

	#somma uno per uno
	for i in digits:
		sumOneDigit += i
	#print(sumOneDigit)

	if sumOneDigit == x:
		print(x)
	#somma 









	#sommare in tutti i modi possibili i digits di x e vedere se sono uguali a x*x


















