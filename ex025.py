#fatiamento de string
#frase [9:13]= vai pegar do 9 ao 12, o 13 não vai contar
#frase[:5] = quando n coloca de onde vai começar, começa do 0 até o 4
#frase[15:] = vai do 15 até o final
#len (frase) = é o comprimento da frase
#frase.count('o') = quantas vezes aparece a letra o na frase
#frase.count ('o', 0,13) = do 0 ao 13 quantas vezes aparece a letra o
#frase.find('deo') = qual a posição que começa o 'deo'
#frase.find('android') = retorna o valor -1 pq não existe essa string
#'curso' in frase = vai procurar se existe essa palavra na frase e retorna true na tela
#frase.replace ('python', 'android') = substitui python por android
#frase.upper () = transforma as letras minusculas em maiusculas
#frase.lower () = transformar as letras maiusculas em minusculas
#frase.capitalize () = só o primeiro caractere fica em maiusculo na frase
#frase.title() = analisa quantas palavras tem e coloca o primeiro carctere delas em maiusculo
#frase.strip()= remove todos os espaços inuteis no inicio e no final da string
#divisão
#frase.split() = divisão considerando os espaços. cada uma dessas palavras é colocado em outra lista. divide uma string em uma lista
#Junção
#'-'.join(frase)