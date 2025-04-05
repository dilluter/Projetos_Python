numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


uniao = conjunto1 | conjunto2
print(uniao)  #junta tudo


intersecao = conjunto1 & conjunto2
print(intersecao)  # o que repete nos 2


diferenca = conjunto1 - conjunto2
print(diferenca)  # os elementos do conjunto1 que não estão no conjunto2


diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # os elementos que estão em um ou no outro, mas não nos dois conjuntos