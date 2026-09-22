# MOVIES
import functions as f

f.limparTela()

catalogo = []
while True:
    f.exibirMenu()
    
    menu= int(input("Digite sua opção: "))
    match menu:
        case 1:
            f.cadastrarFilme(catalogo)
        case 2:
            f.loading()
            f.exibirFichaFinal(catalogo)
        case 3:
            notas = f.reuneNotasFilmes(catalogo)
            maxima, minima, media = f.estatisticaNotasFilmes(notas)
            f.buscaFilmeMaiorNota(catalogo, maxima, minima, media)
        case 4:
            print("SAINDO...")
            break
        case _:
            f.limparTela()
            print("irmão ta errado isso ai")
            f.enterParaContinuar()