# Limpeza de HTMLs para Livros Quarto

Este script (`cleanBooks.py`) foi criado para automatizar a limpeza e padronização dos arquivos HTML gerados por projetos Quarto, especialmente para livros acadêmicos ou técnicos.

## O que o script faz?

- Remove headers específicos do Quarto (ex: `<header id="quarto-header">`).
- Substitui o conteúdo do `<head>` dos HTMLs por um modelo padrão (`head.html`).
- Preserva links SEO importantes (`<link rel="next">` e `<link rel="prev">`).
- Insere componentes globais (ex: `globalheader.html`) logo após a abertura da tag `<body>`.
- Permite customizar o local dos componentes com o argumento `--base-ac`.

## Como usar

### Renderize o livro normalmente com o Quarto

```powershell
cd .\build\TAS0000\
quarto render .

# ou mais compacto:
# cd .\build\TAS0000\ ; quarto render .

# voltar para a pasta raiz do projeto
cd ../..
```

### Limpe todos os HTMLs gerados

```powershell
python run/cleanBooks.py --base-dir book/
```

### Usando componentes personalizados

Se você tem um diretório específico para os componentes (ex: `build/ac/`):

```powershell
python run/cleanBooks.py --base-dir book/ --base-ac build/ac/
```

### Limpar um arquivo HTML específico

```powershell
python run/cleanBooks.py --file caminho/para/arquivo.html
```

## Argumentos

- `--base-dir`: Diretório base para limpeza recursiva dos arquivos HTML.
- `--file`: Caminho para um arquivo HTML único a ser limpo.
- `--base-ac`: Diretório dos componentes (ex: `globalheader.html`, `head.html`). Opcional, padrão é `build/`.

## Requisitos

- Python 3
- BeautifulSoup (`pip install beautifulsoup4`)

## Observações

- O script não altera arquivos PDF, apenas HTML.
- Links de navegação SEO são preservados automaticamente.
- O componente global (`globalheader.html`) é inserido em todos os HTMLs processados.

---

**Exemplo de uso completo:**

```powershell
python run/cleanBooks.py --base-dir book/ --base-ac build/ac/
```

---

Dúvidas ou sugestões? Abra uma issue ou envie um e-mail para o mantenedor do projeto.
