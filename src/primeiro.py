# Calcular a nota no curso com certo número de alunos
#
# Para cada aluno, Ler K notas(reais) e K pesos (inteiros)
# Cada nota tem um peso definido como uma entrada
# Caso de teste:
# 1) peso positivo
# 2) notas no intervalo de [0,10]

def validar_notas(notas, pesos):
    executa = True
    msg_erro: str = "\n"
    i = 0
    while executa == True and i < len(notas):
        if notas[i] < 0 or notas[i] > 10:
            executa = False
            msg_erro = "Nota %d tem valor inválido" % (i + 1)
        if pesos[i] <= 0:
            executa = False
            msg_erro = msg_erro + "Peso %d tem valor inválido!" % (i + 1)

        i = i + 1
    return executa, msg_erro


def calcular_media(notas, pesos):
    temp_nota = 0.0
    temp_peso = 0
    for i in range(0, len(notas)):
        temp_nota = temp_nota + (notas[i] * pesos[i])
        temp_peso = temp_peso + pesos[i]

    media_final: float = temp_nota / temp_peso

    return media_final


def ler_notas(nro_notas):
    notas = []
    #Quantidade de notas e armazenamento
    #nro_notas = int(input("Quantas notas você deseja inserir?: "))
    for i in range(0, nro_notas):
        nota = float(input("Insira a %dª nota: " % (i + 1)))
        notas.append(nota)

    return notas


def ler_pesos(nro_pesos):
    pesos = []
    for i in range(0, nro_pesos):
        peso = int(input("Insira o %dº peso: " % (i + 1)))
        pesos.append(peso)

    return pesos


def main():
    nro_alunos = int(input("Insira a quantidade de alunos: "))

    for i in range(0, nro_alunos):
        nro_notas = int(input("Insira o número de notas para o %dº aluno: " % (i + 1)))
        pesos = ler_pesos(nro_notas)
        notas = ler_notas(nro_notas)

        executa, msg_erro = validar_notas(notas, pesos)

        if executa:
            media = calcular_media(notas, pesos)
            print("Média do %dº aluno: %.2f" % (i + 1, media))
        else:
            print("Entrada de dados inválida!")
            print(msg_erro)


if __name__ == "__main__":
    main()
