xa=float(input("Digite a coordenada x do ponto A: "))
ya-float(input("Digite a coordenada y do ponto A: "))
xb=float(input("Digite a coordenada x do ponto B: "))
yb=float(input("Digite a coordenada y do ponto B: "))
m=(yb-ya)/(xb-xa)
cl=-m*xa+ya

if cl>=0:
  print("A equação da reta que passa pelos pontos dados é: y = " , m,"x +",cl)
else:
print("A equação da reta que passa pelos pontos dados é: y = ",m,"x +",cl)


