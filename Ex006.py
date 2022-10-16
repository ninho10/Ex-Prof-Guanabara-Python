# MEDIDOR DE VELOCIDADE É DE 80KM VC E MULTADO 7 REAIS CADA KM ACIMA DE 80KM

print('  MEDIDOR DE VELOCIDADE')
print('')

V = int(input(' Qual foi a velocidade que seu carro passou --> '))

if V > 80:
    print('Voce foi multado')
    print(" multa de R$ ", (V-80) * 7)
else:
    print("velocidade permitida")
