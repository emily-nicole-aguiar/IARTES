# Modulo 01
Deposite aqui as suas repostas

# Aula sobre Conceitos básicos
1. Escreva um script python que define duas variáveis do tipo inteiro (__int__)
e atribui um valor positivo para elas. Imprima as duas variáveis.

variavel1 = 10
variavel2 = 5
print(variavel1, variavel2)

2. Seja x = 2 + 4j, descubra qual é o tipo associado a essa variável pelo interpretador.

x = 2 + 4j
type(x)
Resposta: <class 'complex'>

3. Experimente a inicialização de variáveis como segue:
   1. urnas = {}
   2. sessao = {"escola municipal", 103}
   descubra qual é o tipo da variável __urnas__ e da variável __sessao__. Explique se necessário
a razão dos tipos serem distintos.

>>> urnas = {}
>>> sessao = {"escola municipal", 103}
>>> type(urnas)
<class 'dict'>
>>> type(sessao)
<class 'set'>
A variável urnas é do tipo dicionário pois as chaves (abrindo e fechando) representam um dicionário vazio.
Já a variável sessao é do tipo conjunto por que ele apresenta somente o valor, em vez de associar a uma chave como ocorre no dicionário

4. Nas definições de nomes de variáveis abaixo quais têm nomes válidos e quais são invalidos
    1. ola = "mundo"  Resposta: Variável Válida;
    2. _ola = "mundo" Resposta: Inválida. A variável não pode iniciar com um caractere especial;
    3. _1_ola = "mundo" Resposta: Inválida. A variável não pode iniciar com um caractere especial;
    4. 1_ola = "mundo" Resposta: Inválida. A variável não pode iniciar com um número;
    5. ola_1 = "mundo" Resposta: Variável válida;
    6. meu mundo = "ola" Resposta: A variável não pode ter espaço.

aponte as razões para os nomes inválidos, indicando o item e a razão da violação
das regras de nomeação de variável.

5. No seguinte comando de atribuição 
   1. casa, senha = "minha", "ola" Resposta: Funcionou;
   2. casa, senha = "minha" Resposta: Não funcionou por que a variável senha não recebeu um valor;
   3. casa = "minha" Resposta: Funcionou.

Quais foram as atribuições que funcionaram e quais não funcionaram? Explique a razão dos problemas.
   
6. Considere as seguintes operações matemáticas, e indique o resultado de cada uma:
   1. (10 - 6)**2 = 16
   2. 10 - 6**2 = -26
   3. 10 - 3 // 2 = 9
   4. 10 - 3 / 2 = 8.5

7. Qual a importância de se criar ambiente virtuais para o desenvolvimentos de projetos usando Python?

O ambiente virtual ajuda a isolar os pacotes e dependências do projeto que está sendo desenvolvido.

8. Descubra e responda qual versão do python está instalado no seu ambiente de desenvolvimento. Que comando você usou 
para obter essa informação?

Estou usando a versão do Python 3.7.0;
Utilizei o comando python --version para verificar.

9. Uma tupla é um tipo imutável, portanto qualquer variável desse tipo pode ser alterada desde que os seus elementos 
sejam individualizados, como no código abaixo:

   __comprado = ("carro", "GM", "20K")__

   __comprado[1] = "Ford"__

   você concorda com essa afirmação? justifique sua resposta.
   Resposta: Não concordo. Para alterar uma tupla é necessário alterar tudo que está dentro dela, e não somente um valor como acontece na lista.

10. Considere o código abaixo:

      __numero = input()__
      print(numero*3)

      se o valor 3(três) for informado como entrada e armazenado na variável número.
Resposta: numero = input(3)
          print(numero * 3)

11. Revise o código disponibilizado em src/primeiro.py. Em seguida altere o programa
para que ele se torne generalista, i.e., aceite qualquer quantidade de notas que cada
aluno pode ter. 

A alteração foi feita na função notas onde a variável nro_notas informa quantas notas serão inseridas

def ler_notas(nro_notas):
    notas = []
    #Quantidade de notas e armazenamento
    #nro_notas = int(input("Quantas notas você deseja inserir?: "))
    for i in range(0, nro_notas):
        nota = float(input("Insira a %dª nota: " % (i + 1)))
        notas.append(nota)

    return notas