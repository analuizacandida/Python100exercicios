produto = float(input('Qual o preço do produto?'))
desconto = produto -(produto *5 / 100)
print('O produto vale {:.2f}, mas com o desconto de 5% vale {:.2f}'.format(produto,desconto))
