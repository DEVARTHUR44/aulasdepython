import os
os.system("cls")
#SWITCH CASE => (math case) escolha caso
#ESTRUTURA =
#math valor:
    #case valor:
    
# linguagem = input("Diga algo de programação e saia correndo: ")
# match linguagem:
#     case "python":
#         print("é foda e coça a tetinha")
#     case "Eu acho que gosto de t.i":
#         print("não não voce não gosta")
#     case _ :
#         print("whatever neh")

# print("="*8, "DESCUBRA QUE DIA É HOJE", "="*8)

# dia = float(input("DIGITE QUE DIA DA SEMANA: "))
# match dia:
#     case 1:
#         print("Hoje é segunda")
#     case 2:
#         print("Hoje é terça-feira")
#     case 3:
#         print("Hoje é quarta-feira")
#     case 4:
#         print("Hoje é quinta-feira")
#     case 5:
#         print("Hoje é sexta-feira")
#     case 6:
#         print("Hoje é sabado")
#     case 7:
#         print("Hoje é Domingo")
#     case 10.1:
#         print("Feliz aniversario arthur")
#     case 18.4:
#         print("18 DE ABRIL LANA DEL REY LANÇOU BLUEBIRD... TENHO VONTADE DE DAR UM JEITO... UM JEITO NA MINHA VIDA.")
#     case _ :
#         print("VOCE É LESADO???? É DE 1 A 7 SEU ACÉFALO")

# dia = float(input("DIGITE O DIA: "))
# if dia == 1:
#     print("segunda")
# elif dia == 2:
#     print("terça")
# elif dia == 3:
#     print("quarta")
# elif dia == 4:
#     print("quinta")
# elif dia == 5:
#     print("sexta")
# elif dia == 6:
#     print("sabado")
# elif dia == 7:
# print(f"hoje é {dia}")

# print("-"*4, "LOJA DANIEL&GRILLO CERRYS", "-"*4)
      
# print(""" 
# 1 - iphone 15 - R$5000.00
# 2 - redmi 13 - R$ 2500.00
# 3 - samsung - 6999.99

# FRETES POR ESTADO
# 1 sp = 10.00
# 2 mg = 15.00
# 3 rs = 20.00
# """)

# print("-"*7)

# celular = float(input("DIGITE O NUMERO DO PRODUTO: "))
# estado = float(input("DIGITE A SIGLA DO ESTADO: "))

# print("-"*7)

# match celular:
#     case 1:
#         print(f"PREÇO TOTAL: {5000.00+ 10.00}")
#     case 2:
#         print(f"PREÇO TOTAL: {2500.00 + 15.00}")
#     case 3:
#         print(f"PREÇO TOTAL: {6999.99 + 20.00}")
#     case 4:
#         print(f"PREÇO TOTAL: {5000.00+20.00}")
#     case 5:
#         print(f"PREÇO TOTAL: {5000.00+15.00}")
#     case 6:
#         print(f"PREÇO TOTAL: {2500.00 + 20.00}")
#     case 7:
#         print(f"PREÇO TOTAL: {2500.00 + 10.00}")
#     case 8:
#         print(f"PREÇO TOTAL: {6999.99 + 10.00}")
#     case 9:
#         print(f"PREÇO TOTAL: {6999.99 + 15.00}")
# print("="*7)

#atv corrigida
# print(""" 
# MUNDO CELULAR
      
# 1-IPHONE -> 5000
# 2-MOTO G -> 3000
# 3-LENOVO -> 2500

# FRETE: 
#       SP -> 10,00
#       RS -> 20,00
#       RJ -> 30,00      
# """)

# celular = int(input("Digite a opção desejada: "))
# estado = input("Digite a sigla do estado para entrega: ").lower()
# valor=0
# frete=0
# valortotal=0
# match celular:
#     case 1:
#         valor=5000
#     case 2:
#         valor=3000
#     case 3:
#         valor=2500

# match estado:
#     case "sp":
#         frete=10
#     case "rs":
#         frete=20
#     case "rj":
#         frete=30

# valortotal= valor + frete

# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valor+frete:.2f}")
import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")

#ATV pedra papel tesoura


# papel=   """""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# pedra = """""
#  _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """


# tesoura = """""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# """
# print("PEDRA PAPEL TESOURA 2 -- O SITE OFICIAL")

# jogador = input("DIGITE UM ITEM: ")

# match jogador:
#     case _ if jogador == "pedra":
#         print("VOCE ESCOLHEU PEDRA")
#         print(f"{pedra}")
#     case _ if jogador == "tesoura":
#         print("VOCE ESCOLHEU TESOURA")
#         print(f"{tesoura}")
#     case _ if jogador == "papel":
#         print("VOCE ESCOLHEU PAPEL")
#         print(f"{papel}")

# sistema = random.randint(1,3)

# match sistema:
#     case _ if sistema == 1:
#         print("A MÁQUINA ESCOLHEU PAPEL")
#         print(f"{papel}")
#     case _ if sistema == 2:
#         print("A MÁQUINA ESCOLHEU PEDRA")
#         print(f"{pedra}")
#     case _ if sistema == 3:
#         print("A MÁQUINA ESCOLHEU TESOURA")
#         print(f"{tesoura}")

# match jogador:
#     case _ if jogador == "pedra" and sistema == 3:
#         print("o jogador venceu")
#     case _ if jogador == "tesoura" and sistema ==3:
#         print("EMPATE, TESOURINHAS")
#     case _ if jogador == "tesoura" and sistema == 2:
#         print("A MAQUINA VENCEU")
#     case _ if jogador == "pedra" and sistema == 2:
#         print("EMPATE")
#     case _ if jogador == "PEDRA" and sistema == 1:
#         print("o jogador venceu")
#     case _ if jogador == "tesoura" and sistema == 1:
#         print("o jogador venceu")
#     case _ if jogador == "papel" and sistema == 1:
#         print("EMPATE")
#     case _ if jogador == "papel" and sistema == 2:
#         print("A MAQUINA VENCEU")
#     case _ if jogador == "papel" and sistema == 3:
#         print("A MAQUINA VENCEU")


#VERSOES DO PROFESSOR
# print("JOGO PEDRA PAPEL TESOURA")

# papel = """
# PAPEL
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# pedra = """
# PEDRA
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """


# tesoura = """
# TESOURA
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# """

# jogador = input("Escolha entre pedra, papel ou tesoura: ")
# match jogador:
#     case "pedra":
#         jogador=pedra
#     case "tesoura": 
#         jogador =tesoura
#     case "papel":
#         jogador = papel

# #1-> pedra , 2-> papel , 3->tesoura

# maquina = random.randint(1,3)

# match maquina:
#     case 1:
#         maquina=pedra
#     case 2: 
#         maquina =papel
#     case 3:
#         maquina =tesoura


# print(f"voce escolheu  {jogador}")
# print(f"maquina escolheu {maquina}")

# match jogador:
#     case _ if jogador == maquina:
#         print("empate")
#     case _ if jogador==pedra and maquina ==tesoura:
#         print("Voce ganhou")
#     case _ if jogador == tesoura and maquina ==papel:
#         print("Voce ganhou")
#     case _ if jogador == papel and maquina ==pedra:
#         print("voce ganhou")
#     case _ :
#         print("voce perdeu")


# print("2 MODO - PEDRA PAPEL TESOURA")


# print("JOGO PEDRA PAPEL TESOURA ")

# papel = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# pedra = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """


# tesoura = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# """

#pedra=1 papel=2 tesoura=3
# mao = input("Digite pedra ou papel ou tesoura :")
# maquina = random.randint(1,3)

# match maquina :
#     case 1:
#         maquina = "pedra"
#     case 2:
#         maquina = "papel"
#     case 3 :
#         maquina ="tesoura"

# match mao:

#     case _ if mao== "pedra" and maquina=="pedra" :
#         print(f"Maquina: {maquina} {pedra}")
#         print(f"Você: {mao}  {pedra}")
#         print("EMPATOU!")
    
#     case _ if mao== "pedra" and maquina=="papel":
#         print(f"Maquina: {maquina} {papel}")
#         print(f"Você: {mao}  {pedra}")
#         print("PERDEU!")
#     case _ if mao== "pedra" and maquina=="tesoura":
#         print(f"Maquina: {maquina} {tesoura}")
#         print(f"Você: {mao}  {pedra}")
#         print("GANHOU!")
#     case _ if mao== "papel" and maquina=="papel":
#         print(f"Maquina: {maquina} {papel}")
#         print(f"Você: {mao}  {papel}")
#         print("EMPATOU!")
#     case _ if mao== "papel" and maquina=="pedra":
#         print(f"Maquina: {maquina} {pedra}")
#         print(f"Você: {mao}  {papel}")
#         print("GANHOU")
#     case _ if mao== "papel" and maquina=="tesoura":
#         print(f"Maquina: {maquina} {tesoura}")
#         print(f"Você: {mao}  {papel}")
#         print("PERDEU!")
#     case _ if mao== "tesoura" and maquina=="pedra":
#         print(f"Maquina: {maquina} {pedra}")
#         print(f"Você: {mao}  {tesoura}")
#         print("PERDEU!")
#     case _ if mao== "tesoura" and maquina=="papel":
#         print(f"Maquina: {maquina} {papel}")
#         print(f"Você: {mao}  {tesoura}")
#         print("GANHOU!")
#     case _ if mao== "tesoura" and maquina=="tesoura":
#         print(f"Maquina: {maquina} {tesoura}")
#         print(f"Você: {mao}  {tesoura}")
#         print("EMPATOU!")
#     case _:
#         print("DIGITOU ERRADO! ESCOLHA PAPEL OU TESOURA OU PEDRA")

