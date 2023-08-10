# # Aula sobre Conceitos básicos

# 1. Escreva um script python que define duas variáveis do tipo inteiro (__int__)
# e atribui um valor positivo para elas. Imprima as duas variáveis.
variavel1 = 10
variavel2 = 5

print(variavel1, variavel2)

# 2. Seja x = 2 + 4j, descubra qual é tipo associado a essa variável pelo interpretador.
x = 2 + 4j
type(x)
#Resposta: <class 'complex'>

# 3. Experimente a inicialização de variáveis como segue:
#    1. urnas = {}
#    2. sessao = {"escola municipal", 103}
#    descubra qual é o tipo da variável __urnas__ e da variável __sessao__. Explique se necessário
# a razão dos tipos serem distintos.
urnas = {}
sessao = {"escola municipal", 103}
# >>> urnas = {}
# >>> sessao = {"escola municipal", 103}
# >>> type(urnas)
# <class 'dict'>
# >>> type(sessao)
# <class 'set'>
# A variável urnas é do tipo dicionário pois as chaves (abrindo efechando) representam um dicionário vazio
# A variável sessao é do tipo conjunto por que ele apresenta somente o valor, em vez de associar a uma chave como ocorre no dicionário

# 4. Nas definições de nomes de variáveis abaixo quais têm nomes válidos e quais são invalidos
#     1. ola = "mundo"
#     2. _ola = "mundo" Resposta: A variável não pode iniciar com um caractere especial
#     3. _1_ola = "mundo" Resposta: A variável não pode iniciar com um caractere especial
#     4. 1_ola = "mundo" Resposta: A variável não pode iniciar com um número
#     5. ola_1 = "mundo"
#     6. meu mundo = "ola" Resposta: A variável não pode ter espaço

# aponte as razões para os nomes inválidos, indicando o item e a razão da violação
# das regras de nomeação de variável.

