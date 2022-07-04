# Mini exercícios

#ler um número inteiro e imprimir falando o tipo do mesmo

num = 50
print(num)
print(type(num))

# Ler um numero real e imprimir mostrando o tipo do mesmo

num1 = 12.50
print(num1)
print(type(num1))

# Coletar 3 números do usuário - somar e imprimir a soma

num2 = int(input("digite um numero inteiro"))
num3 = int(input("digite um numero inteiro"))
num4 = int(input("digite um numero inteiro"))

soma = num2 + num3 + num4
print(soma)

# raiz quadrada de número real
num5 = 12.50**2
print(num5)

# quinta parte de um número real
num6 = 500.25%5
print(num6)

# Ler uma temperatura em graus celsius e apresentar ela convertida em graus fahrenheit

temp = 20 * 9/5
print(temp)
temp = 36 + 32
print(temp)
print(f'20 graus convertido em Fahrenheit é igual a {temp}!')

# Ler a temperatura em Fahrenheit e converter para graus celsius
# F = 100
temp2 = 5 * (100 - 32) / 9
print(temp2)
print(f' 100 Fahrenheit convertido em celsius é igual a {temp}!')

#  Ler uma temperatura em graus Kelvin e converter para celsius
temperatura = 55
celsius = 55 - 273.15
print(celsius)

# Temperatura em Celsisus para kelvin
temperatura1 = 100
# K = C + 273.15
celsius1 = 100 + 273.15
print(celsius1)


# Ler uma velocidade em km e apresente em m/s
# M = k/3.6
velocidade1 = 30
mili = velocidade1/3.6
print(mili)

# Ler uma velocidade em m/s transformando para KM
velocidade2 = 30
# K = M * 3,6
km = 30 * 3.6
print(f'A velocidade em KM será {km}')

# Ler uma distancia em quilometros e apresentar em milhas
# M = k / 1.61
distancia = 250
milhas = 250 / 1.61
print(f'A Distância em milhas será de {milhas}')

#Ler um angulo em graus e apresentar convertido em radianos
graus = 60
radiano = 60 * 180 / 3.14
print(f'Um angulo em radiano medirá {radiano}')

# Leia um valor de volume em litros e apresente em metros cubicos
volumelitro = 2000
metrocubico = 2000 / 1000
print(f'O valor em metros cubicos será {metrocubico} Litros')

# Leia um valor da massa em quilogramas e apresente convertido em libras
kg = 500
libras = 500 / 0.45
print(f'O valor convertido em libras será {libras}')
