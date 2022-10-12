
# LEIA UM NUMERO E DER O SUCESSOR É O ANTECESSOR DESSE NUMERO.

N1 = int(input('Um valor '))
print('Seu sucessor {} '.format(N1+1))
print('Seu antecessor {} '.format(N1-1))


# mostre o dobro e o tripo de um numero 

Numero = int(input(' Digite um numero '))
print('Seu dobro é : {}'.format(Numero * 2))
print('Seu tripo é {}'.format(Numero * 3))



# Leia 2 nota e de a media

Nota1 = float(input('primeira nota'))
Nota2 = float(input('Segunda nota'))
Media = (Nota1 + Nota2)/2
print("A media entre {} e {} : {} ".format(Nota1, Nota2, Media))


# converter Real para dolar

Dinheiro = float(input('Quanto você tem na carteira : '))
Dola = (Dinheiro / 5.50)
print(' Com $ {} reais você troca por {} reais'.format(Dinheiro, Dola))
