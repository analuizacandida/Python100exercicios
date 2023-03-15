import datetime

try:
    ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
    if ano == 0:
        ano_atual = datetime.date.today().year
        if ano_atual % 4 == 0 and (ano_atual % 100 != 0 or ano_atual % 400 ==0):
            print('O ano atual ({}) é Bissexto'.format(ano_atual))
        else:
            print('O ano atual ({}) NÃO é Bissexto'.format(ano_atual))
    else:
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 ==0):
            print('O ano {} é Bissexto'.format(ano))
        else:
            print('O ano {} NÃO é Bissexto'.format(ano))
except ValueError:
    print('Entrada inválida. Por favor, insira um número inteiro válido.')

