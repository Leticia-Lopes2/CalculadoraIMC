print('               Calculadora IMC              ')
nome = input('Qual seu nome? ')
idade = input(f'Olá {nome}, qual sua idade? ')
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso/(altura*altura)
if imc >= 18.5:
    print(f'Seu IMC é {round(imc, 3)}, Parabéns seu IMC esta normal!')
elif imc <= 18.5:
    print(f'Seu IMC é: {round(imc, 3)} você está abaixo do peso!')
elif imc >= 25.0:
    print(f'Sei IMC é {round(imc, 3)}, você está acima do peso!')
else:
    quit()
#Leticia Moura