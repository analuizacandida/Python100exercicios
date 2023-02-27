frase = str(input('digite uma frase:')).upper().strip()
print('A letras A aparece {} vezes na frase'.format(frase.count ('A')))
print(' a primeira letras apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
