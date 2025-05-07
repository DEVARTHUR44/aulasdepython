#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)

#EXERCICIO 1 IF x ELSE E DESAFIO
import os
os.system("cls")
# idadeuser = int(input("Informe sua idade:" ))

# idadeuser > 0
# idadeuser < 120


# if idadeuser < 18:
#       print("voce tem ", idadeuser , "anos logo voce é menor de idade")
# else:
#       print("voce tem ", idadeuser , "anos logo voce é maior e idade")

# if idadeuser < 0 or idadeuser > 120:
#       print("idade invalida")



#EXERCICIO 3

# email = input("digite seu email:")
# if email == ("python@portalsesisp.org.br"):
#     print("email correto")
# else:
#     import os
#     os.system("color 4")
#     print("email incorreto. Verifique se foi digitado corretamente.")

# senha = (input("digite sua senha:"))


# if senha == ("Sesi@123"):
#     print("senha correta")
# else:
#     import os
#     os.system("color 4")
#     print("senha incorreta. Verifique se foi digitada corretaente ou se a-esqueceu")

    
#ATV 4

# print("="*9, "HORTINHA DO SESI", "="*9)

# unidade30 = 30.0
# unidade25 = 0.25
# print("R$" ,unidade30, "por menos que uma dúzia")
# print("R$" ,unidade25, "se fossem compradas pelo menos doze")

# quantidade = int("Digite a quantidade de maçãs que gostaria:")
# total = unidade30 + unidade25
# print( quantidade,": R$ 0.30, ")

#CORREÇÃO MACAS

# qtd = int(input("Digite a quantidade de macas q quer: "))

# if qtd < 12:
#     calc = qtd*0.30
#     print("Vc pagara por por 0,30 unidades R$:" , calc)
# else:
#     calc = qtd*0.25
#     print("Vc ira pagar por 0,25 unidades R$:" , calc)

#ATV 5 IF ELSE AND OR 
# print("*"*8, "VOGAL OU CONSOANTE", "*"*8)
# letra = input("DIGITE UMA LETRA:")
# if letra == "a" or letra == "e" or letra == "i" or letra== "o" or letra== "u" :
#     print("a letra" ,letra , "é uma vogal")
# else:
#     print("a letra" , letra , "é uma consoante")

#ATV 6
# print("*"*5, "DESCUBRA NUMERO MAIOR AKI", "*"*5)

# numero1 = float(input("Digite um numero:"))
# numero2 = float(input("Digite outro numero:"))

# if numero1 > numero2:
#     print("o maior numero:", numero1)
#     print("o menor numero:", numero2)
#     print("o numero" , numero1, "é maior que", numero2)
# else:
#     print("o maior numero:", numero2)
#     print("o menor numero:", numero1)
#     print("o numero" , numero2, "é maior que", numero1)
# else:
#     print("o numero", numero1, "é igual a", numero2)


#REESCREVENDO NA CORREÇÃO
#upper() -> converter td pra maisculo
#lower() -> converter td pra minusculo

#o programa nn reconhece letra maiuscula
# print("*"*8, "VOGAL OU CONSOANTE", "*"*8)
# letra = input("DIGITE UMA LETRA:").lower()
# if letra == "a" or letra == "e" or letra == "i" or letra== "o" or letra== "u" :
#     print("a letra" ,letra , "é uma vogal")
# else:
#     print("a letra" , letra , "é uma consoante")

#reescrita 
#AND OR in
# letra = input("Digite uma letra: ")
# if letra in "aeiouAEIOU":
#     print("vogal")
# else:
#     print("consoante")
