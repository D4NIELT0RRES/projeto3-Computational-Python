
# === Helper de verificacao (pode ignorar) ===
# A funcao `verifica` compara o seu valor com a resposta correta (que
# fica escondida em formato de hash). Voce nao precisa entender ela -
# se voce errou, ela imprime "Valor errado: voce colocou X" e o assert
# logo abaixo dispara.
import hashlib
def verifica(valor, codigo):
    valores = [valor]
    if isinstance(valor, list):
        valores = [sorted(valor)]
    elif isinstance(valor, int) and not isinstance(valor, bool):
        valores.append(float(valor))
    elif isinstance(valor, float):
        valores.append(int(valor))
    respostas = [hashlib.sha224(str(valor).encode('utf-8')).hexdigest() == codigo for valor in valores]
    if not any(respostas):
        print(f'Valor errado: voce colocou "{valor}" na variavel')
        return False
    return True
# fim do helper


'''
EXPLICACAO

Bem-vindo ao exercicio da forca! Vamos modelar dois jogadores -
lucas e heloisa - que tentam adivinhar palavras letra por letra.

Cada jogador tem uma PALAVRA escondida. A cada chute, todas as
posicoes daquela letra na palavra sao reveladas de uma vez. Errar
a letra custa uma VIDA. Quando todas as posicoes da palavra
estiverem reveladas, voce ganhou; se as vidas chegarem a 0 antes,
voce perdeu.

NOVIDADES NESSE EXERCICIO

Voce vai usar tres construcoes novas (ou que apareceram pouco):

    - range(len(lista)): quando o for precisa do INDICE, nao so
      do elemento (ex: para escrever em outra lista paralela).
    - break:    sai do for completamente. Para quando ja achou
                o que queria ou bateu uma condicao final.
    - continue: pula o resto da volta atual do for e vai pra
                proxima iteracao.

ESTRUTURAS

Uma palavra eh so uma string:

    palavra = "banana"

Strings em Python se comportam como listas de letras:

    palavra[0]           # 'b'
    palavra[1]           # 'a'
    len(palavra)         # 6
    "a" in palavra       # True
    palavra.count("a")   # 3  (quantas vezes 'a' aparece)

Mas strings sao IMUTAVEIS: nao da pra fazer palavra[0] = "B".

Por isso usamos uma LISTA paralela chamada `reveladas`, que comeca
toda com "_" e vai sendo preenchida:

    reveladas = ["_", "_", "_", "_", "_", "_"]
    # apos chutar "a":
    reveladas = ["_", "a", "_", "a", "_", "a"]

Repare que reveladas[i] corresponde a palavra[i]. Eh por isso que vai
ser interessante usar `range(len(palavra))`.

Teremos mais duas estruturas:

    letras_tentadas = ["a", "n"]   # lista das letras ja chutadas
    vidas = 6                       # int, comeca em 6 e desce a cada erro

'''


# ===== FASE 1 - Aquecimento: lendo uma palavra =====

palavra_exemplo = "banana"

'''
EXERCICIO

Considere palavra_exemplo acima.

Preencha as variaveis usando uma EXPRESSAO Python que produz o
valor (em vez de escrever o valor literal direto). Se nao
conseguir, pode comecar com o valor literal pra ver o teste
passar, mas depois tente reescrever como expressao.

1) Qual a primeira letra de palavra_exemplo? (string)

   Dica: palavra_exemplo[0]
'''
primeira_letra = palavra_exemplo[0]

'''
2) Quantas letras tem palavra_exemplo? (numero)
'''
tamanho_da_palavra = len(palavra_exemplo)

'''
3) Quantas vezes a letra "a" aparece em palavra_exemplo? (numero)

   Dica: use .count("a")
'''
quantas_letras_a = palavra_exemplo.count("a")

'''
4) A letra "z" aparece em palavra_exemplo? (True ou False)

   Dica: use o operador `in`
'''
tem_z = 'z' in palavra_exemplo

'''
5) Crie uma lista de "_" com o tamanho de palavra_exemplo. Esse
   eh o estado inicial das letras reveladas (nenhuma revelada
   ainda). Esperado: ["_", "_", "_", "_", "_", "_"]

   Dica: em Python, ["_"] * 3 produz ['_', '_', '_']. Voce pode
   usar len() pra nao escrever o numero a mao.
'''
reveladas_iniciais = ["_"] * len(palavra_exemplo)

assert verifica(primeira_letra, 'c681e18b81edaf2b66dd22376734dba5992e362bc3f91ab225854c17'), 'primeira_letra incorreta'
assert verifica(tamanho_da_palavra, '31da1a042dc910775ed8b487afbdafd929a7afdeaadc660cb963bd26'), 'tamanho_da_palavra incorreta'
assert verifica(quantas_letras_a, '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474'), 'quantas_letras_a incorreta'
assert verifica(tem_z, '623d4fc7bd6d8878dd37a9fd4a591ddfa41a2487f53809e84fd9e7c4'), 'tem_z incorreta'
assert verifica(reveladas_iniciais, 'e3d6140c9c83b4f888489372e0653fd8d7cb9b8462a186016efc1b2e'), 'reveladas_iniciais incorreta'
print('Exercicio lendo uma palavra: OK')


'''
EXERCICIO

Calculo a mao. Considere:

    palavra = "abacaxi"
    reveladas = ["a", "_", "a", "_", "a", "_", "_"]

Quantas letras ainda FALTAM revelar nessa palavra? (numero)

Dica: conte quantos "_" tem na lista reveladas. Existe um comando python para isso
'''
quantas_falta_revelar = 4

assert verifica(quantas_falta_revelar, '271f93f45e9b4067327ed5c8cd30a034730aaace4382803c3e1d6c2f'), 'quantas_falta_revelar incorreta'
print('Exercicio calculo a mao: OK')


# ===== FASE 2 - A funcao revela_letra =====

'''
EXPLICACAO

Vamos comecar a escrever as funcoes. Lembre-se: as funcoes desse
exercicio NAO acessam variaveis globais. Recebem tudo por
parametro.

A funcao `revela_letra` recebe a palavra, a lista reveladas e a
letra que o jogador chutou. Para cada posicao onde a palavra tem
aquela letra, ela copia a letra para reveladas naquela posicao.

NOVIDADE: range(len(...))
=========================

Pra escrever em reveladas[i], a funcao precisa saber o INDICE de
cada posicao. O for "comum" so da o elemento:

    for letra in palavra:      # so temos a letra, nao o indice (a posicao) dela
        ...                     # nao tem como editar a lista 'reveladas'

Pra ter o indice, usamos range(len(...)):

    for i in range(len(palavra)):   # i vai de 0 ate len(palavra)-1
        if palavra[i] == letra:
            reveladas[i] = letra    # agora consegue escrever!

Esse padrao eh classico quando voce tem listas paralelas (`palavra`
e `reveladas` se correspondem por indice).
'''


'''
EXERCICIO

Faca a funcao revela_letra(palavra, reveladas, letra) que:
    - percorre cada posicao da palavra (use range(len(palavra)))
    - se palavra[i] == letra, escreve letra em reveladas[i]
    - retorna QUANTAS posicoes ela revelou (0 se a letra nao
      aparece na palavra, >0 se aparece)

A funcao MUTA reveladas (escreve nela). NAO modifica palavra
(strings sao imutaveis e nao dah mesmo).

    >>> palavra = "banana"
    >>> reveladas = ["_", "_", "_", "_", "_", "_"]
    >>> revela_letra(palavra, reveladas, "a")
    3
    >>> reveladas
    ["_", "a", "_", "a", "_", "a"]

    >>> revela_letra(palavra, reveladas, "n")
    2
    >>> reveladas
    ["_", "a", "n", "a", "n", "a"]

    >>> revela_letra(palavra, reveladas, "z")
    0
    (reveladas nao muda - z nao aparece em banana)
'''
# percorra palavra usando range(len(palavra)), se achar a letra, escreva em reveladas e conte quantas vezes revelou
def revela_letra(palavra, reveladas, letra):
    cont = 0
    for i in range(len(palavra)):
        if palavra[i] == letra:
            reveladas[i] = letra
            cont += 1
    return cont

# teste 1: revela todas as 'a'
palavra_t = "banana"
reveladas_t = ["_", "_", "_", "_", "_", "_"]
n = revela_letra(palavra_t, reveladas_t, "a")
assert n == 3, f'revela_letra deveria retornar 3 (3 ocorrencias de a), retornou {n}'
assert reveladas_t == ["_", "a", "_", "a", "_", "a"], f'reveladas errado: {reveladas_t}'

# teste 2: revela as 'n' em cima das 'a'
n = revela_letra(palavra_t, reveladas_t, "n")
assert n == 2, f'revela_letra deveria retornar 2 (2 ocorrencias de n), retornou {n}'
assert reveladas_t == ["_", "a", "n", "a", "n", "a"], f'reveladas errado: {reveladas_t}'

# teste 3: letra que nao aparece -> retorna 0 e nao muta reveladas
reveladas_t = ["_", "_", "_", "_", "_", "_"]
n = revela_letra(palavra_t, reveladas_t, "z")
assert n == 0, f'revela_letra deveria retornar 0 (z nao aparece), retornou {n}'
assert reveladas_t == ["_", "_", "_", "_", "_", "_"], f'z nao deveria mudar reveladas, virou {reveladas_t}'

print('Exercicio revela_letra: OK')


# ===== FASE 3 - A funcao ganhou =====

'''
EXPLICACAO

Agora uma funcao simples: dado o estado de reveladas, dizer se o
jogador ganhou (todas as posicoes ja preenchidas, nenhum "_"
sobrou).

Em vez de percorrer reveladas inteira sempre, a funcao pode
retornar LOGO que achar um "_": se tem um, ja sabe que NAO
ganhou. Nao adianta continuar o for.

    for x in reveladas:
        if x == "_":
            return False    # achou um, sai aqui mesmo
    return True             # chegou no fim sem achar "_": ganhou

Esse padrao de "achei o que procurava, retorna logo" reduz a computacao,
deixa nosso codigo mais rapido e barato de rodar
'''


'''
EXERCICIO

Faca a funcao ganhou(reveladas) que retorna True se nao tem mais
nenhum "_" em reveladas, e False caso contrario.

A funcao NAO modifica reveladas.

    >>> ganhou(["_", "a", "_"])
    False
    >>> ganhou(["b", "a", "n", "a", "n", "a"])
    True
'''
#percorra reveladas, se achar um "_", retorna False. Se chegar no fim, retorna True.
def ganhou(reveladas):
    for x in reveladas:
        if x == "_":
            return False
    return True

assert ganhou(["_", "a", "_"]) == False, 'ganhou com underscores deveria ser False'
assert ganhou(["b", "a", "n", "a", "n", "a"]) == True, 'ganhou sem underscores deveria ser True'
assert ganhou(["_"]) == False, 'ganhou com so um underscore deveria ser False'
assert ganhou(["a", "_", "a"]) == False, 'ganhou com underscore no meio deveria ser False'

# nao deve modificar a entrada
reveladas_antes = ["_", "a", "_"]
reveladas_copia = ["_", "a", "_"]
ganhou(reveladas_antes) 
assert reveladas_antes == reveladas_copia, 'ganhou NAO deveria modificar reveladas'

print('Exercicio ganhou: OK')


# ===== FASE 4 - A funcao processa_chutes =====

'''
EXPLICACAO

A funcao processa_chutes recebe uma LISTA de chutes (varias letras
de uma vez) e processa um por um. Pra cada chute:

    1) se a letra JA foi tentada antes, pula (nao gasta vida)
    2) se nao, adiciona em letras_tentadas
    3) chama revela_letra; se nao revelou nada, vidas -= 1
    4) se ja ganhou OU as vidas chegaram a 0, para de processar

NOVIDADES: continue e break
============================

`continue` - pula o resto da volta atual do for, vai pra proxima:

    for x in lista:
        if condicao_pular:
            continue            # nao executa nada abaixo;
                                # vai pro proximo x
        faz_alguma_coisa(x)
        outra_coisa(x)

`break` - sai do for por completo:

    for x in lista:
        if condicao_acabar:
            break               # sai do for; nao processa o
                                # resto da lista
        faz_alguma_coisa(x)

Nesta funcao:
    - continue eh usado pra IGNORAR letra ja tentada (sem voltar
      pra processar revela_letra, sem descontar vida)
    - break eh usado pra PARAR o jogo (vidas==0 ou ja ganhou)
'''


'''
EXERCICIO

Faca a funcao processa_chutes(palavra, reveladas, letras_tentadas, vidas, chutes):

Para cada `letra` em `chutes`:
    - se letra esta em letras_tentadas: continue (nao gasta vida,
      nao re-processa, volta pro começo do for e pega a proxima)
    - acrescente letra a letras_tentadas (.append)
    - chame revela_letra(palavra, reveladas, letra). Se retornou
      0 (chute errado), faca vidas = vidas - 1
    - se vidas == 0 OU ganhou(reveladas): break

Retorne o valor final da variavel vidas.

A funcao MUTA (de mutação, ou seja, ALTERA) reveladas (via revela_letra) e letras_tentadas
(via append). Vidas eh int (imutavel) - retorna o novo valor.

    >>> palavra = "banana"
    >>> reveladas = ["_", "_", "_", "_", "_", "_"]
    >>> letras_tentadas = []
    >>> processa_chutes(palavra, reveladas, letras_tentadas, 6, ["a", "n"])
    6
    >>> reveladas
    ["_", "a", "n", "a", "n", "a"]
    >>> letras_tentadas
    ["a", "n"]

    >>> # letra repetida -> continue. Nao gasta vida nem entra duas
    >>> # vezes em letras_tentadas:
    >>> palavra = "banana"
    >>> reveladas = ["_", "_", "_", "_", "_", "_"]
    >>> letras_tentadas = []
    >>> processa_chutes(palavra, reveladas, letras_tentadas, 6, ["a", "a", "a"])
    6 #6 vidas. Nao perdeu vida, pois a eh letra valida
    >>> letras_tentadas
    ["a"]

    >>> # chute errado gasta vida:
    >>> processa_chutes("banana", ["_"]*6, [], 3, ["z"])
    2 # vidas era 3, ficou sendo 2
'''
def processa_chutes(palavra, reveladas, letras_tentadas, vidas, chutes):
    for letra in chutes:
        if letra in letras_tentadas:
            continue
        letras_tentadas.append(letra)
        n_revelou = revela_letra(palavra, reveladas, letra)
        if n_revelou == 0:
            vidas -= 1
        if vidas == 0 or ganhou(reveladas):
            break
    return vidas

# Nota: nos testes abaixo usamos "argumentos nomeados" (passar os
# parametros pelo nome em vez de pela posicao). E equivalente a
# escrever processa_chutes(palavra_t, reveladas_t, letras_t, 6, [...]),
# mas fica mais legivel quando a funcao tem muitos parametros e
# varios deles sao listas.

# teste 1: chutes certos sem repeticao -> vidas inalteradas
palavra_t = "banana"
reveladas_t = ["_"] * 6
letras_t = []
v = processa_chutes(palavra=palavra_t, reveladas=reveladas_t,
                    letras_tentadas=letras_t, vidas=6, chutes=["a", "n"])
assert v == 6, f'sem erros, vidas deveria continuar 6, virou {v}'
assert reveladas_t == ["_", "a", "n", "a", "n", "a"], f'reveladas errado: {reveladas_t}'
assert letras_t == ["a", "n"], f'letras_tentadas errado: {letras_t}'
# repare: a funcao tem 3 efeitos: 
# * calcular a nova quantidade de vidas, que ela retorna
# * modificar a lista "reveladas"
# * modificar a lista de letras tentadas

# teste 2: chute repetido -> continue (nao gasta vida, nao entra duas vezes)
reveladas_t = ["_"] * 6
letras_t = []
v = processa_chutes(palavra="banana", reveladas=reveladas_t,
                    letras_tentadas=letras_t, vidas=6, chutes=["a", "a", "a"])
assert v == 6, f'letras repetidas nao gastam vida, virou {v}'
assert letras_t == ["a"], f'letra repetida nao deveria entrar 2x em letras_tentadas: {letras_t}'
assert reveladas_t == ["_", "a", "_", "a", "_", "a"], f'reveladas errado: {reveladas_t}'


# teste 3: chutes errados gastam vida
reveladas_t = ["_"] * 6
letras_t = []
v = processa_chutes(palavra="banana", reveladas=reveladas_t,
                    letras_tentadas=letras_t, vidas=3, chutes=["z", "x"])
assert v == 1, f'2 erros com 3 vidas deveriam deixar 1, virou {v}'
assert reveladas_t == ["_"] * 6, f'reveladas nao deveria mudar (chutes errados): {reveladas_t}'
assert letras_t == ["z", "x"], f'letras_tentadas errado: {letras_t}'

# teste 4: vidas chegam a 0 no meio -> break (chutes posteriores ignorados)
reveladas_t = ["_"] * 6
letras_t = []
v = processa_chutes(palavra="banana", reveladas=reveladas_t,
                    letras_tentadas=letras_t, vidas=1, chutes=["z", "x", "y"])
assert v == 0, f'1 vida + 1 erro deveria zerar, virou {v}'
assert reveladas_t == ["_"] * 6, f'reveladas nao deveria mudar: {reveladas_t}'
assert letras_t == ["z"], f'apos vidas=0, demais chutes deveriam ser ignorados (break): {letras_t}'

# teste 5: ganhou no meio -> break (chutes posteriores ignorados)
letras_t = []
reveladas_t = ["_"] * 6
# "banana" tem so b, a, n - apos ["b","a","n"] ja ganhou. O "z" depois nao deve entrar.
v = processa_chutes(palavra="banana", reveladas=reveladas_t,
                    letras_tentadas=letras_t, vidas=6, chutes=["b", "a", "n", "z"])
assert v == 6, f'ganhou sem erros, vidas deveriam continuar 6, virou {v}'
assert reveladas_t == ["b", "a", "n", "a", "n", "a"], f'reveladas errado: {reveladas_t}'
assert letras_t == ["b", "a", "n"], f'apos ganhar, "z" nao deveria entrar em letras_tentadas: {letras_t}'

# teste 6: lista de chutes vazia
reveladas_t = ["_"] * 6
letras_t = []
v = processa_chutes(palavra="banana", reveladas=reveladas_t,
                    letras_tentadas=letras_t, vidas=6, chutes=[])
assert v == 6, f'chutes vazios nao deveriam mudar vidas, virou {v}'
assert reveladas_t == ["_"] * 6, f'reveladas nao deveria mudar (chutes vazios): {reveladas_t}'
assert letras_t == [], f'letras_tentadas nao deveria mudar (chutes vazios): {letras_t}'

print('Exercicio processa_chutes: OK')


# ===== FASE 5 - Simulacao lucas e heloisa =====

'''
EXPLICACAO

Agora cada um joga sua palavra, usando as MESMAS funcoes - basta
chamar com argumentos diferentes. Como em apostas, QUEM CHAMA
reatribui o que eh imutavel (vidas) e confia na mutacao do que eh
mutavel (reveladas, letras_tentadas).
'''

# lucas vai adivinhar "banana"
palavra_lucas = "banana"
reveladas_lucas = ["_"] * len(palavra_lucas)
letras_lucas = []
vidas_lucas = 6

# heloisa vai adivinhar "abacaxi"
palavra_heloisa = "abacaxi"
reveladas_heloisa = ["_"] * len(palavra_heloisa)
letras_heloisa = []
vidas_heloisa = 6

'''
EXERCICIO

Antes de rodar processa_chutes, PREVEJA o resultado.

lucas vai chutar: ["a", "n", "a"]   (palavra "banana")
    - "a": revela quantas posicoes? gasta vida?
    - "n": revela quantas? gasta vida?
    - "a": ja foi chutada - o que acontece?

heloisa vai chutar: ["a", "x", "z"]    (palavra "abacaxi")
    - "a": revela quantas?
    - "x": revela quantas?
    - "z": gasta vida?

Preencha:

1) Quantas vidas lucas vai ter no final? (numero)
'''
vidas_lucas_previsto = 

'''
2) Quantas vidas heloisa vai ter no final? (numero)
'''
vidas_heloisa_previsto = 'coloque o valor aqui'

'''
3) Quantas letras (posicoes nao "_") reveladas_lucas vai ter no
   final? (numero)
'''
quantas_reveladas_lucas = 'coloque o valor aqui'

'''
4) Quantas letras (posicoes nao "_") reveladas_heloisa vai ter no
   final?
'''
quantas_reveladas_heloisa = 'coloque o valor aqui'

assert verifica(vidas_lucas_previsto, '31da1a042dc910775ed8b487afbdafd929a7afdeaadc660cb963bd26'), 'vidas_lucas_previsto incorreto'
assert verifica(vidas_heloisa_previsto, 'b51d18b551043c1f145f22dbde6f8531faeaf68c54ed9dd79ce24d17'), 'vidas_heloisa_previsto incorreto'
assert verifica(quantas_reveladas_lucas, 'b51d18b551043c1f145f22dbde6f8531faeaf68c54ed9dd79ce24d17'), 'quantas_reveladas_lucas incorreta'
assert verifica(quantas_reveladas_heloisa, '271f93f45e9b4067327ed5c8cd30a034730aaace4382803c3e1d6c2f'), 'quantas_reveladas_heloisa incorreta'
print('Exercicio previsao lucas e heloisa: OK')

# Roda a simulacao - mesma funcao, argumentos diferentes
vidas_lucas = processa_chutes(palavra=palavra_lucas, reveladas=reveladas_lucas,
                               letras_tentadas=letras_lucas, vidas=vidas_lucas,
                               chutes=["a", "n", "a"])
vidas_heloisa  = processa_chutes(palavra=palavra_heloisa, reveladas=reveladas_heloisa,
                               letras_tentadas=letras_heloisa, vidas=vidas_heloisa,
                               chutes=["a", "x", "z"])

# Confere com o esperado
assert vidas_lucas == 6, f'vidas_lucas deveria ser 6 (sem erros), virou {vidas_lucas}'
assert reveladas_lucas == ["_", "a", "n", "a", "n", "a"], f'reveladas_lucas errado: {reveladas_lucas}'
assert letras_lucas == ["a", "n"], f'letras_lucas errado: {letras_lucas}'

assert vidas_heloisa == 5, f'vidas_heloisa deveria ser 5 (1 erro: z), virou {vidas_heloisa}'
assert reveladas_heloisa == ["a", "_", "a", "_", "a", "x", "_"], f'reveladas_heloisa errado: {reveladas_heloisa}'
assert letras_heloisa == ["a", "x", "z"], f'letras_heloisa errado: {letras_heloisa}'

print('Exercicio simulacao lucas e heloisa: OK')


print('\n=== PARABENS! Todos os exercicios completos! ===')


# ===== FASE 6 - INTERFACE CLI (se voce nao conseguir terminar, fazer em casa) =====
#
# Menu pra jogar a forca. Para rodar, descomente a linha "main()"
# no final.
#
# Algumas opcoes estao marcadas como [implementar] - sao pra voce
# completar.

def main():
    palavra_lucas = "banana"
    reveladas_lucas = ["_"] * len(palavra_lucas)
    letras_lucas = []
    vidas_lucas = 6

    palavra_heloisa = "abacaxi"
    reveladas_heloisa = ["_"] * len(palavra_heloisa)
    letras_heloisa = []
    vidas_heloisa = 6

    while True:
        print()
        print("=== FORCA ===")
        print(f"lucas: {' '.join(reveladas_lucas)}  | vidas: {vidas_lucas} | tentadas: {letras_lucas}")
        print(f"heloisa:  {' '.join(reveladas_heloisa)}  | vidas: {vidas_heloisa} | tentadas: {letras_heloisa}")
        print("1. lucas chuta letra")
        print("2. heloisa chuta letra")
        print("3. Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            letra = input("  Letra: ")
            # passa uma LISTA de um elemento so - como a funcao
            # recebia uma lista, esse eh o jeito de passar uma unica letra
            # a funcao eh interessante, justamente porque pode receber 
            # um "lote" de dados (um bocado de dados de uma vez -- chamamos isso de "lote"
            # ou, mais frequentemente "batch") ou uma soh letra (se a gente)
            # lembrar de quardar essa letra em uma string
            vidas_lucas = processa_chutes(palavra_lucas, reveladas_lucas, letras_lucas, vidas_lucas, [letra])
            if vidas_lucas == 0:
                print(f"  lucas perdeu! A palavra era '{palavra_lucas}'")
                break
            if ganhou(reveladas_lucas):
                print(f"  lucas ganhou!")
                break
        elif opcao == "2":
            print("  [implementar: chute da heloisa, mas deixar ela digitar mais de uma letra, usando split]")
        elif opcao == "3":
            break
        else:
            print("Opcao invalida")


# Para rodar a interface, descomente:
# main()
