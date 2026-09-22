# =============== FUNÇÕES DO PROGRAMA MOVIES ===============
from rich import print
import os
import time
import emoji

# Função que limpa a tela do terminal.
def limparTela():
    os.system('cls')

# Função que permite o usuário digitar ENTER para o programa continuar.
def enterParaContinuar():
    input("Digite ENTER para continuar...")

# Função que gera e retorna o código do filme.
def geradorCodigo(titulo):
    espacos = titulo.replace(" ", "").upper()
    codigo = espacos[:4] + espacos[-2:]
    return codigo

# Função que simula uma tela de carregamento.
def loading():
    limparTela()
    print("Loading", end="")
    for i in range(1, 6):
        print(".", end="", flush=True)
        time.sleep(0.5)

# Função que classifica o filme de acordo com a nota.
def classificarFilme(nota):
    if (nota <= 1):
        mensagem = "CARA, NÃO PERCA O SEU TEMPO!"
    elif (nota <= 4):
        mensagem = "RUINZINHO!"
    elif (nota <= 6):
        mensagem = "SE NÃO TIVER NADA PARA FAZER, ASSISTA!"
    elif (nota <= 8):
        mensagem = "BOM, INVISTA SEU TEMPO"
    else:
        mensagem = "OMG! MORRI E RESSUSCITEI, OBRA PRIMA!"
    return mensagem

# Função que gera uma mensagem específica para cada gênero de filme.
def geraMensagemGenero(genero):
    opcao = genero[:2].upper()
    match opcao:
        case "AÇ":
            mensagem_genero = emoji.emojize(f"{genero} :water_pistol:")
        case "TE":
            mensagem_genero = emoji.emojize(f"{genero} :ghost:")
        case "AV":
            mensagem_genero = emoji.emojize(f"{genero} :cowboy_hat_face:")
        case "FI":
            mensagem_genero = emoji.emojize(f"{genero} :alien:")
        case "RO":
            mensagem_genero = emoji.emojize(f"{genero} :beating_heart:")
        case "CO":
            mensagem_genero = emoji.emojize(f"{genero} :rolling_on_the_floor_laughing:")
        case _:
            mensagem_genero = emoji.emojize(f"Amigo, não conheço esse aí {genero}")
    
    return mensagem_genero

# Função que pede para o usuário e verifica se a nota é válida.
def pedeEVerificaNotaValida():
    nota = int(input("AVALIE SEU FILME DE 0 À 10: "))
    while nota < 0 or nota > 10:
        print("Cara, Para de querer ferrar o Programador")
        nota = int(input("AVALIE SEU FILME DE 0 À 10: "))
    return nota

# Função que cadastro todas as informações de um filme.
def cadastrarFilme(catalogo):
    
    limparTela()
    
    print("[bold green]-=@ CADASTRO DO FILME @=-[/bold green]\n")
    
    titulo = input("DIGITE O NOME DO FILME: ").strip().title()
    genero = input("DIGITE O GÊNERO DO FILME: ").strip().capitalize()
    ano_lancamento = int(input("DIGITE O ANO DE LANÇAMENTO DO FILME: "))
    sinopse = input("DIGITE A SINOPSE DO FILME: ").strip().capitalize()
    nota = pedeEVerificaNotaValida()
    codigo = geradorCodigo(titulo)
    
    mensagem = classificarFilme(nota)
    mensagem_genero = geraMensagemGenero(genero)
    
    novo_filme = {"codigo": codigo,
                  "titulo": titulo,
                  "genero": genero,
                  "ano_lancamento": ano_lancamento,
                  "sinopse": sinopse,
                  "nota": nota,
                  "mensagem": mensagem,
                  "mensagem_genero": mensagem_genero}
    
    catalogo.append(novo_filme)
    enterParaContinuar()

# Função que exibe o menu de opções para o usuário.
def exibirMenu():
    limparTela()
    print("="*40)
    print("""      [bold green]-=@ BEM VINDO AO MOVIES @=-[/bold green]
            
Escolha uma opção para continuar:
    
    1-Cadastrar filme
    2-Exibir filme 
    3-Estatísticas do Catálogo
    4-Sair
    """)
    print("="*40)

# Função que imprime a Ficha Final do filme com todas as informações.
def exibirFichaFinal(catalogo):
    limparTela()
    print("[gray]=[/gray]"*30)
    print(f"""[bold green]INFORMAÇÕES DO SEU FILME:[/bold green]""")

    for i in range(len(catalogo)):
        print(f"""
[bold red]{catalogo[i]["codigo"]}[/bold red]

TÍTULO: {catalogo[i]["titulo"]}
GÊNERO: {catalogo[i]["mensagem_genero"]}
NOTA DO FILME: {catalogo[i]["nota"]}/10
AVALIAÇÃO: {catalogo[i]["mensagem"]}
ANO DE LANÇAMENTO: {catalogo[i]["ano_lancamento"]}
SINOPSE: {catalogo[i]["sinopse"]}""")
    print("[gray]=[/gray]"*30)
    enterParaContinuar()

# Função que adiciona todas as notas de um filme e uma lista de notas.
def reuneNotasFilmes(catalogo):
    notas = []
    for i in range(len(catalogo)):
        notas.append(catalogo[i]["nota"])
    return notas
    
# Função que calcula as notas máximas, mínimas e a média das notas.
def estatisticaNotasFilmes(notas):
    maxima = max(notas)
    minima = min(notas)
    media = sum(notas) / len(notas)
    return maxima, minima, media

# Função que imprime as estatísticas das notas.
def buscaFilmeMaiorNota(catalogo, maxima, minima, media):
    limparTela()
    for filme in catalogo:
        if maxima == filme["nota"]:
            print("FILME COM MAIOR NOTA")
            print(f"{filme["titulo"]} --> {maxima}")
        if minima == filme["nota"]:
            print("\nFILME COM MENOR NOTA")
            print(f"{filme["titulo"]} --> {minima}")
    print(f"\nMÉDIA DAS NOTAS --> {media}")
    enterParaContinuar()

