# faça um programa que leia o nome de uma pessoa e mostre ele separadamente.
nome = str(input(' Digite seu nome completo:')) .strip()
separa = nome.split()
print(' seu nome separado fica {}'.format(separa))