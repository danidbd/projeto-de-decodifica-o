#Criptografia RSA - Ciências da Computação
#Turma 1P - 2022



# INÍCIO #


import random


#################################################################################################

# Função que verifica se o número digitado pelo usuário é ou não primo

def primo (num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True

    else:
        return False

#################################################################################################


#################################################################################################

# Função que realiza o cálculo do Máximo Divisor Comum

def mdc(num1,num2):
    while num2 !=0:
        resto = num1 % num2
        num1 = num2
        num2 = resto

    return num1

#################################################################################################


#################################################################################################

# Função que realiza o cáculo de função modular, resto da divisão entre dois números

def mod(num1,num2):
    if num1 < num2:
        return num1
    else:
        resp = num1 % num2
        return resp

#################################################################################################


#################################################################################################

# Coleta os números de P e Q e só coleta a mensagem para avanças quando P e Q forem primos

p = int(input("Digite o primeiro número primo: "))
while (primo(p)) == False:
    print("Por favor, digite um número que seja primo: ")
    p = int(input("Digite um número e veja se ele é primo: "))

q = int(input("Digite o segundo número primo: "))
while (primo(q)) == False:
    print("Por favor, digite um número que seja primo: ")
    q = int(input("Digite o segundo número primo: "))

mensagem = input("Digite sua mensagem: ")

#################################################################################################


#################################################################################################

# Realiza os cálculos para encontrar N, o Totiente de N, e as chaves primária E e secundária D
n = p*q
totiente = (p - 1) * (q - 1) # Função totiente


# Encontra possíveis valores de E, que satisfaçam as condições propostas
listaE = []
i = 1
for i in range (i,totiente):
    if mdc(totiente,i) == 1 and 1 < i < totiente:
        listaE.append(i)
    i = i + 1


# Seleciona aleatoriamente um dos possíveis valores de E, armazenados em listaE
e = random.choice(listaE)


# Com E selecionado, encontra os possíveis valores para D, que satisfaça as condições propostas
d = 0
while(mod(d*e,totiente)!=1):
    d = d + 1
else:
    D = d


#Exibe os valores encontrados até então
print("\nO valor de N é {} e seu totiente é {}" .format(n,totiente))
print("Aqui está sua chave primária {},{}" .format(n,e))
print("Aqui está sua chave secundária {},{}\n" .format(n,d))

#################################################################################################


#################################################################################################

# Realiza as operações de codificação na mensagem, caracter por caracter, e armazena em textoEncode
textoEncode = []
i = 0
elementos1 = len(mensagem)
while i < elementos1:
    unidade = mensagem[i]
    unidade_unicode1 = ord(unidade)
    x = unidade_unicode1**e
    cifrado = mod(x,n)
    textoEncode.append(cifrado)
    i = i + 1


print("Seu texto encriptado é: ",textoEncode)


# Realiza o caminho reverso da codificação, caracter por caracter, e armazena em textoDecode
textoDecode = []
j = 0
elementos2 = len(textoEncode)
while j < elementos2:
    y = textoEncode[j]**D
    unidade_unicode2 = mod(y,n)
    decifrado = chr(unidade_unicode2)
    textoDecode.append(decifrado)
    j = j + 1


print("Seu texto decriptado é: ",textoDecode)


#################################################################################################

# FIM #







