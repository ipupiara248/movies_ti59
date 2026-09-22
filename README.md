# 🎬 Movies

Sistema de terminal para cadastro, consulta e avaliação de filmes, desenvolvido em Python.

## Funcionalidades

- **Cadastrar filme**: registra título, gênero, ano de lançamento, sinopse e nota (0 a 10).
- **Exibir catálogo**: lista todos os filmes cadastrados com suas informações completas.
- **Estatísticas do catálogo**: mostra o filme com maior nota, o de menor nota e a média geral.
- **Buscar filme**: localiza um filme pelo código gerado automaticamente.
- Classificação automática do filme conforme a nota (ex: "BOM, INVISTA SEU TEMPO", "OMG! MORRI E RESSUSCITEI, OBRA PRIMA!").
- Emoji temático de acordo com o gênero informado (Ação, Terror, Aventura, Ficção, Romance, Comédia).
- Persistência dos dados em arquivo `catalogo.json`.

## Como o código do filme é gerado

O código é formado pelas 4 primeiras letras do título (sem espaços) + as 2 últimas letras, tudo em maiúsculo.

Exemplo: `Interestelar` → `INTEAR`

## Requisitos

- Python 3.10+ (o projeto usa `match/case`, disponível a partir do Python 3.10)
- Bibliotecas:
  - [`rich`](https://pypi.org/project/rich/)
  - [`emoji`](https://pypi.org/project/emoji/)

Instalação das dependências:

```bash
pip install rich emoji
```

## Como executar

```bash
python movies.py
```

> Ajuste o nome do arquivo principal conforme o nome real do seu script de entrada.

## Estrutura do projeto

```
├── movies.py          # Arquivo principal (menu e loop do programa)
├── functions.py        # Funções do sistema (cadastro, exibição, estatísticas, etc.)
└── catalogo.json        # Base de dados dos filmes (gerado automaticamente)
```

## Menu principal

```
1 - Cadastrar filme
2 - Exibir catálogo
3 - Estatísticas do catálogo
4 - Buscar um filme
5 - Sair
```