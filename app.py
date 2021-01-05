import random

print('--------------------------------------')
print('CHUTE O NÚMERO')
print('DIGITE 1 PARA JOGAR')
print('--------------------------------------')

Answer = input('')

if Answer == '1':
	#Gerador de números aleatorios
	Number1 = random.randrange(0,11)
	Number2 = random.randrange(0,11)
	#Inputs de resposta do úsuario
	Try1 = input('Digite um número:')
	Try2 = input('Digite outro número:')
	if Try1 == Number1 and Try2 == Number2:
		print('Parabéns, você ganhou com 2 acertos!')
	elif Try1 == Number1 and Try2 != Number2:
		print('Você fez 1 ponto! mas infelizmente não foi dessa vez D:')
	elif Try1 != Number1 and Try2 == Number2:
		print('Você fez 1 ponto! mas infelizmente não foi dessa vez D:')
	elif Try1 != Number1 and Try2 != Number2:
		print('infelizmente não foi dessa vez D:')
	print('Os números sorteados foram:')
	print(Number1)
	print(Number2)