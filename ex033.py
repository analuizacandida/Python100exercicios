'''nome= str(input('Qual o seu nome?'))
if nome =='Ana':
    print('Que nome lindo você têm!')
else:
    print('seu nome é tão normal :/')
print('Bom dia, {}!'.format(nome)) '''

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print ('a sua média foi {:.2f}'.format(m))
if m >=6.0:
    print('sua média foi boa! Parabéns!!')
else:
    print('sua média foi ruim! :(')
