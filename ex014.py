salario = float(input('Qual é o salário do funcionário?'))
aumento = salario + (salario * 15/100)
print('Um funcionário que ganhava {:.2f}, com o aumento de 15%, passa a receber {:.2f}'. format(salario,aumento))
