"""print("======== Para seguirmos com o serviço, por favor insira as seguintes informações ========")
 
dia = input("Dia: ")
mes = input("Mês: ")
ano = input("Ano: ")

print("Com base nas informações inseridas a cima, podemos determinar que:")
print(".")
print(".")
print(".")
print("Você nasceu no dia", dia, "de",mes, "de", ano,) """

"""----------calculadora basicassa:----------"""
num1= int(input())

resultado = input()

num2= int(input())

multiplicação = (num1 * num2)

soma = (num1 + num2)

menos = (num1 - num2)

divisao = (num1 / num2)

if resultado == "*":
    print("resultado:",multiplicação)

elif resultado == "+":
    print("resultado:",soma)

elif resultado == "-":
    print("resultado:", menos)

elif resultado == "/":
    print("resultado:", divisao)

else: 
    print("Tipo de caracter não aceito, por favor tente novamente")