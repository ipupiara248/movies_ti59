# MOVIES
import functions as f

f.limparTela()

catalogo = []
while True:
    f.exibirMenu()

    try:
        menu= int(input("Digite sua opção: "))

        match menu:
            case 1:
                f.cadastrarFilme(catalogo)
            case 2:
                f.loading()
                f.exibirFichaFinal(catalogo)
            case 3:
                notas = f.reuneNotasFilmes(catalogo)
                if len(notas) != 0:
                    maxima, minima, media = f.estatisticaNotasFilmes(notas)
                    f.buscaFilmeMaiorNota(catalogo, maxima, minima, media)
                else:
                    print("Nenhuma nota cadastrada até o momento.")
                    f.enterParaContinuar
            case 4:
                print("SAINDO...")
                break
            case _:
                f.limparTela()
                print("irmão ta errado isso ai")
                f.enterParaContinuar()
            
    except ValueError, TypeError:
        print("Só aceitamos números!")
