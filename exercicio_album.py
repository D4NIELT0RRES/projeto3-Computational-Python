
# === Boilerplate (pode ignorar) ===
# Esse codigo so serve para o professor testar o gabarito em casa. Voce nao precisa dele. Pode ignorar ou deletar
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

try:
    import gabarito_NAO_MANDAR as _gab
    _GAB = {k: v for k, v in vars(_gab).items() if not k.startswith('_')}
except ImportError:
    _gab = None
    _GAB = {}

def _aplica(nome):
    if nome in _GAB:
        globals()[nome] = _GAB[nome]

def _resync(nome):
    if _gab is None:
        return
    valor = globals()[nome]
    setattr(_gab, nome, valor)
    _GAB[nome] = valor
# fim do boilerplate


'''
EXPLICACAO

Bem-vindo ao exercicio do album de figurinhas! A ideia e modelar um
album estilo Copa do Mundo: voce vai ganhando figurinhas, algumas
repetem (vem repetidas no pacote), outras voce ainda nao tem.

Vamos guardar isso em uma LISTA DE STRINGS:

    album = ["pele", "ronaldo", "pele"]

Aqui:
    - album[0] = "pele"
    - album[1] = "ronaldo"
    - album[2] = "pele"  (repetida! ja tinha pele em album[0])

A "pele" aparece duas vezes - voce ganhou ela em dois pacotes
diferentes e a lista guarda as duas.

Algumas operacoes uteis em listas:
    > len(album)            # quantas figurinhas tem na lista
    3
    > album.count("pele")   # quantas vezes a "pele" aparece
    2
    > "ronaldo" in album    # ronaldo esta na lista?
    True
    > "zico" in album       # e o zico?
    False
'''


# ===== FASE 1 - Aquecimento: lendo um album =====

album = ["pele", "ronaldo", "pele", "garrincha", "pele"]

'''
EXERCICIO

Considere o album acima:

    album = ["pele", "ronaldo", "pele", "garrincha", "pele"]

Preencha as variaveis usando uma EXPRESSAO Python que produz o valor
(em vez de escrever o numero/booleano direto). As tres expressoes
estao na EXPLICACAO la em cima.

1) Quantas figurinhas tem no album? (numero)
'''
quantas_figurinhas = len(album) 

'''
2) Quantas vezes a "pele" aparece no album? (numero)
'''
quantas_peles = album.count("pele") 

'''
3) O "zico" esta no album? (True ou False)
'''
tem_zico = "zico" in album 

_aplica('quantas_figurinhas'); _aplica('quantas_peles'); _aplica('tem_zico') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

assert verifica(quantas_figurinhas, 'b51d18b551043c1f145f22dbde6f8531faeaf68c54ed9dd79ce24d17'), 'quantas_figurinhas incorreta'
assert verifica(quantas_peles, '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474'), 'quantas_peles incorreta'
assert verifica(tem_zico, '623d4fc7bd6d8878dd37a9fd4a591ddfa41a2487f53809e84fd9e7c4'), 'tem_zico incorreta'
print('Exercicio lendo um album: OK')


# ===== FASE 2 - As funcoes do album =====

'''
EXPLICACAO

Agora vamos para o album de verdade. O album tem dois "lados":

1. As figurinhas que VOCE TEM, na ordem em que ganhou, podendo repetir.
2. As figurinhas que EXISTEM no album, lista fixa definida pelo album.

Vamos guardar isso em duas listas globais (declaradas fora de qualquer
funcao):

    figurinhas_existentes = ["pele", "ronaldo", "zico", "garrincha", "rivelino"]
    album = []  # comeca vazio: voce ainda nao ganhou nenhuma figurinha

Quando voce ganha uma figurinha, ela vai pro album. Se voce ja tem ela,
fica repetida (a lista pode ter "pele" varias vezes).
'''

figurinhas_existentes = ["pele", "ronaldo", "zico", "garrincha", "rivelino"]
album = []
_aplica('album') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar


'''
EXERCICIO

Faca a funcao adiciona_figurinha(nome) que adiciona uma figurinha nova
na lista global `album`.

Dica: use album.append(nome).

A funcao nao precisa retornar nada.

    >>> album -> []
    >>> adiciona_figurinha("pele")
    >>> album -> ["pele"]
    >>> adiciona_figurinha("pele")
    >>> album -> ["pele", "pele"]
    >>> adiciona_figurinha("ronaldo")
    >>> album -> ["pele", "pele", "ronaldo"]
'''
def adiciona_figurinha(nome):
    album.append(nome)
_aplica('adiciona_figurinha') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

album.clear()
adiciona_figurinha("pele")
assert album == ["pele"], f'album errado: {album}'
adiciona_figurinha("pele")
assert album == ["pele", "pele"], f'album errado: {album}'
adiciona_figurinha("ronaldo")
assert album == ["pele", "pele", "ronaldo"], f'album errado: {album}'
print('Exercicio adiciona_figurinha: OK')


'''
EXERCICIO

Antes de escrever as funcoes que listam REPETIDAS e FALTANTES, vamos
calcular na mao!

Considere o seguinte album (uma lista de strings):

    album_exemplo = ["pele", "ronaldo", "pele", "garrincha", "pele", "ronaldo"]

E lembre que figurinhas_existentes (definida la em cima) e:

    ["pele", "ronaldo", "zico", "garrincha", "rivelino"]

REPETIDA = figurinha que aparece MAIS DE UMA VEZ no album_exemplo.
FALTANTE = figurinha que esta em figurinhas_existentes mas NAO esta
           no album_exemplo.

1) Lista das REPETIDAS (sem duplicar - cada nome aparece so uma vez
   no resultado, mesmo que esteja la varias vezes):
'''

album_exemplo = ["pele", "ronaldo", "pele", "garrincha", "pele", "ronaldo"]

repetidas_a_mao = ['pele', 'ronaldo']  

'''
2) Lista das FALTANTES:
'''
faltantes_a_mao = ['zico', 'rivelino']

_aplica('repetidas_a_mao'); _aplica('faltantes_a_mao') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

assert verifica(repetidas_a_mao, '65c73ca3057393481b28bc1823e935340c5199a8bef79c87aee4e6c9'), 'repetidas_a_mao incorreta'
assert verifica(faltantes_a_mao, 'b360c61cd2cb0e662e1a4423f591f0be448d43120f2f2439a4e7352c'), 'faltantes_a_mao incorreta'
print('Exercicio calculo manual de repetidas e faltantes: OK')


'''
EXERCICIO

Faca a funcao faltantes() que retorna a lista das figurinhas que estao
em figurinhas_existentes mas NAO estao em album.

A ordem do resultado e a mesma de figurinhas_existentes.

Lembre que figurinhas_existentes e:
    ["pele", "ronaldo", "zico", "garrincha", "rivelino"]

Dicas:
    - percorra figurinhas_existentes com um for
    - use nome not in album

    >>> album -> ["pele"]
    >>> faltantes()
    ["ronaldo", "zico", "garrincha", "rivelino"]
    >>> album -> ["pele", "ronaldo", "zico", "garrincha", "rivelino"]
    >>> faltantes()
    []
    >>> album -> []
    >>> faltantes()
    ["pele", "ronaldo", "zico", "garrincha", "rivelino"]
'''
def faltantes():
    resultado = []
    for nome in figurinhas_existentes:
        if nome not in album:
            resultado.append(nome)
    return resultado
_aplica('faltantes') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

album = ["pele"]
_resync('album') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar
assert faltantes() == ["ronaldo", "zico", "garrincha", "rivelino"], f'faltantes() errado: {faltantes()}'

album = ["pele", "ronaldo", "zico", "garrincha", "rivelino"]
_resync('album') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar
assert faltantes() == [], f'faltantes() errado: {faltantes()}'

album = []
_resync('album') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar
assert faltantes() == ["pele", "ronaldo", "zico", "garrincha", "rivelino"], f'faltantes() errado: {faltantes()}'

print('Exercicio faltantes: OK')

'''
EXERCICIO

Faca a funcao repetidas() que retorna uma lista com os nomes das
figurinhas que aparecem MAIS DE UMA VEZ na lista global `album`. Cada
nome aparece so uma vez no resultado, mesmo que esteja repetido varias
vezes no album.

A ordem do resultado e a ordem de PRIMEIRA aparicao no album.

Dicas:
    - percorra o album com um for
    - para cada nome, use album.count(nome) > 1 para saber se e repetida
    - use nome not in resultado para evitar adicionar duas vezes

    >>> album -> ["pele", "ronaldo", "pele"]
    >>> repetidas()
    ["pele"]
    >>> album -> ["pele", "ronaldo", "pele", "ronaldo", "zico"]
    >>> repetidas()
    ["pele", "ronaldo"]
    >>> album -> ["zico"]
    >>> repetidas()
    []
'''
def repetidas():
    resultado = []
    for nome in album:
        # para cada nome, se ele aparece mais de uma vez no album e ainda nao esta no resultado, adiciona ele no resultado
        if album.count(nome) > 1 and nome not in resultado:
            resultado.append(nome)
    return resultado
_aplica('repetidas') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar

album = ["pele", "ronaldo", "pele"]
_resync('album') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar
assert repetidas() == ["pele"], f'repetidas() deveria ser ["pele"], obteve {repetidas()}'

album = ["pele", "ronaldo", "pele", "ronaldo", "zico"]
_resync('album') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar
assert repetidas() == ["pele", "ronaldo"], f'repetidas() deveria ser ["pele", "ronaldo"], obteve {repetidas()}'

album = ["zico"]
_resync('album') #essa linha só serve para o professor testar o exercicio em casa. Pode ignorar ou deletar
assert repetidas() == [], f'repetidas() deveria ser [], obteve {repetidas()}'

print('Exercicio repetidas: OK')



print('\n=== Funcoes prontas, agora vamos implementar o menu ===')


# ===== INTERFACE CLI DO ALBUM =====
#
# Menu simples para usar o album de verdade. Para rodar, descomente
# a linha "main()" no fim do arquivo.

def main():
    while True:
        print()
        print("=== ALBUM ===")
        print("1. Adicionar figurinha")
        print("2. Sobrando")
        print("3. Faltantes")
        print("4. Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            nome = input("  Nome da figurinha: ")
            adiciona_figurinha(nome)
            print(f"  Figurinha '{nome}' adicionada.")
        elif opcao == "2":
            print(f"  Sobrando: {repetidas()}")
        elif opcao == "3":
            print(f"  Faltantes: {faltantes()}")
        elif opcao == "4":
            break
        else:
            print("Opcao invalida")


# Para rodar a interface CLI, descomente a linha abaixo:
main()


'''
EXERCICIO: implemente a opcao 3 do menu (Faltantes). Para isso, basta
editar dentro do elif:

    elif opcao == "3":
        print("  implementar")  <- editar aqui

Use a funcao faltantes() que voce ja implementou. A saida pode ser no
mesmo estilo da opcao 2 (Sobrando).
'''


print('\n=== PARABENS! Todos os exercicios completos! ===')
