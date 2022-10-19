# o computador vai pensar em um numero digite o certo.
cont = 0
num = 0

while num != 3:
    cont = cont + 1
    num = int(input(' Entre 1 e 20, digite o numero certo : '))
print(" Parabens o numero e o 3, voce teve {} tentativas ".format(cont))
