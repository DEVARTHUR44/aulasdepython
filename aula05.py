import os
os.system("cls")
#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")

#replace("valor1","valor2") = substitui o v1 pelo v2
# print("="*6, "CALCULADOR DE MEDIA P/ PREGUIÇOSOS", "="*6)

# nota1 = float(input("NOTA DA PRIMEIRA ETAPA:").replace(",","."))
# nota2 = float(input("NOTA DA SEGUNDA ETAPA:").replace(",","."))

# media = (nota1 + nota2) /2

# if media < 5:
#     print("o aluno esta reprovado")
# elif media > 5 < 6 < 7:
#     print("o aluno esta em recuperação")
# elif media > 7:
#     print("o aluno esta aprovado")
# print("a media é", media)

# nome = input("oi cal seu nome? ")
# if nome == "rodrigo" :
#     print("bruxo")
# if nome == "debora" :
#     print("volta linda tenho saudades amore")

#CORREÇÃO DO SOR
# nota1 = float(input("NOTA DA PRIMEIRA ETAPA:").replace(",","."))
# nota2 = float(input("NOTA DA SEGUNDA ETAPA:").replace(",","."))

# media = (nota1 + nota2) /2
# #:.@f -> formata para 2 casas decimais apenas no fstring
# print(f"media: {media:.2f}")

# if media < 5:
#     print("reprova")
# elif media >=5 and media<=7:
#     print('recuperacao')
# else:
#     print("aprovado")


#ATV 3

# peso = float(input("Digite o seu peso: ").replace(",","."))
# altura = float(input("Digite sua altura: ").replace(",","."))

# imc = peso/(altura*altura)

# if imc <17:
#     print("Voce esta muito abaixo do peso com ", imc)
# elif imc>=17 and imc<=18.49:
#     print("Abaixo do peso com ", imc)
# elif imc>=18.5 and imc<=24.99:
#     print("Voce tem um peso normal, de ", imc )
# elif imc>=25 and  imc<=29.99:
#     print("Voce esta acima do peso com", imc )
# elif imc>=30 and imc<=34.99:
#     print("Voce tem obesidade tipo 1 com", imc, )
# elif imc>=35 and imc<=39.99:
#     print("Voce tem obesidade tipo 2", imc )
# elif imc <40:
#     print("Voce tem obesidade mórbida com", imc )


#raw string -> deixar um desenho rodar no print
# print("="*4, "AUTOCAR" ,"="*4)
# print(r"""
#    -           __
#  --          ~( @\   \
# ---   _________]_[__/_>________
#      /  ____ \ <>     |  ____  \
#     =\_/ __ \_\_______|_/ __ \__D
# ________(__)_____________(__)____
# """)

# salario = float(input("Digite seu salário: ").replace(",","."))
# if salario > 2799.99:
#     aumento = salario * 20 /100
#     print(" o aumento sera de 20%, com o salario de", aumento)
# elif salario == 2800.00 and salario == 6999.99:
#     aumento = salario * 15 /100
#     print("o aumento sera de 15%, com o salario de", aumento)
# elif salario == 7000.00 and salario== 14999.99:
#     aumento = salario * 10/100
#     print("o aumento sera de 10%, com o salario de", aumento)
# elif salario = 7000.00 and
