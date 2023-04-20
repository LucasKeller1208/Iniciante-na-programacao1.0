'''
letra = input("Diga uma letra : ")
if letra == "a" or letra == "e" or letra == "i" or letra =="o" or letra =="u":
    print(f"{letra} é vogal")
else:
    print(f"{letra} é consoante")


num1 = input("digite um numero : ")
num2 = input("digite um numero : ")

print(num1 + num2)


#cadastra em duas variaveis um usuario e uma senha
#
nome = "dan"
senha = "1234"
user = input("Diga seu usuario : ")
password = input("Diga sua senha : ")

contagem = 1
while (user != nome or senha != password) and contagem <=3:
    print(f"vacilão vc tem {3-contagem} tentativas")
    user = input("Diga seu usuario : ")
    password = input("Diga sua senha : ")
    contagem +=1
print("acerto")
'''

resposta = input("Voce quer conhecer a minha calculadora ?? (s/n) ")
while not (resposta == "s" or resposta == "n"):
    print("tem que ser (s/n)")
    resposta = input("Voce quer conhecer a minha calculadora ?? (s/n) ")
if resposta == "s":
    while True:
        op = input("qual operação voce quer fazer ? (+,-,/,*) ")
        while not (op == "+" or op == "-" or op == "/" or op == "*"):
            op = input("pelo amor de deus mano !!!!!! (+,-,/,*) ")
        num1 = int(input("diga um numero : "))
        num2 = int(input("diga um numero : "))
        if op == "+":
            resultado = num1 + num2
        elif op == "-":
            resultado = num1 - num2
        elif op == "/":
            resultado = num1 / num2
        else:
            resultado = num1 * num2
        print(f"A operação {op} entre {num1} e {num2} dá {resultado}")
        perg = input("quer fazer mais conta? (s/n)")
        if perg=="n":
            break
else:
    print("boboca")
