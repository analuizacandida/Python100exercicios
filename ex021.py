import math
an = float(input('informe o valor do angulo:'))
sen = math.sin(math.radians(an))
print('o ângulo de {} tem o SENO de {:.2f}'.format(an,sen))
cosseno= math.cos(math.radians(an))
print(' o ângulo de {} tem o conseno de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('o ângulo de{} tem a tangente de {:.2f}'. format(an,tangente))



