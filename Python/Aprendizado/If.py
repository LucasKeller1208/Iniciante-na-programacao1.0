# -*- coding: utf-8 -*-
#DECISÃO_IF
nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
prioridade="NÃO"
if idade>=65: #if é usado como SE, SE a idade for maior ou igual a 65
    prioridade="SIM"
else: #Else é usado como o contrário de if, SE NÃO
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")
