'''Faça um programa que calcule a soma entre todos os números que são
múltiplos de 3 e que se encontram no intervalo de 1 até 500.'''

soma = 0
for c in range(1, 501):
    if c % 3 == 0:
        soma += c
        print(c)
print('A soma entre os números múltiplos de 3 é: {}.'.format(soma))

