<!-- 🤖 README melhorado por IA - GitHub Copilot -->

# A Arte da Estatística

O nome desta série é inspirado na famosa coleção de Donald Knuth chamada “The Art of Computer Programming”, veja (tarara, xxx). Esta série ou coleção será construída com base em minhas notas de aulas e exercícios resolvidos.

## Livros construidos com [Quarto](https://quarto.org/)

> **Projeto acadêmico para criação de livros e materiais educacionais** utilizando Quarto, R, Python e LaTeX, com foco em disciplinas de Estatística, Matemática e Ciência da Computação.

## 📁 Estrutura do Projeto

```
books/
├── ⚙️  .vscode/              # Configurações VS Code + Copilot
├── 🔧 .github/               # Templates e workflows GitHub
│   ├── 📖 README.md          # Documentação principal
│   ├── 📖 workflows          # Ações Automaticas do GitHub
├── 🌐 book/                  # Lista dos livros renderizados
├── 🌐 build/                 # Arquivos compilados e disciplinas
│   ├── 📊 CIC0007/           # Introdução à Computação (Python)
│   ├── 📈 EST0033/           # Estatística Exploratória
│   ├── 📈 ....               # Livro com nome-padão [A-Z]{3}[0-9]{4}
│   📄 disciplinas.json       # Lista de disciplinas
└── 📄 .gitignore             # Arquivos ignorados pelo Git
```

> Com a nova versão do projeto, a pasta `/book/` será abandonada. Uma action detecta as mudanças em `build/` e dispara uma notificação para ao repositório principal, que por sua vez renderiza, padroniza componentes e publica os livros atualizados. Veja [https://www.estatistica.pro/book/](https://www.estatistica.pro/book/)
> **Obs:** A pasta `/build/` é onde os livros são construídos. Cada disciplina tem sua própria pasta, nomeada com um código padrão `[A-Z]{3}[0-9]{4}` (exemplo: `EST0033` para Estatística Exploratória).


## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests. Para grandes mudanças, por favor, abra uma issue primeiro para discutir o que você gostaria de mudar.

## Branchs
- **`main`**: Branch principal, contém a versão estável do projeto.
- **`stag`**: Branch de testes, usada para validar mudanças antes de serem mescladas na `main`.
- **`book`**: Branch usada pela action para atualizar os livros renderizados criando pull_request automaticos.
- **`devX`**: Branch de desenvolvimento implementadas pelo `devX`

> Por favor, evite usar as branch `main`, `stag`, `dev0`, `dev1`, `dev2`, `news`, `book` para desenvolvimento direto. Crie uma nova branch a partir de `stag` para suas alterações usando como nome o sufixo `devX`, onde X é o próximo número de devs disponível. Branches de test devem ser enviadas como `devX-test`, ou faça o merge e envia o push em `devX`.

## 🚀 Como Usar

1. **Clone o repositório** e navegue para a pasta do projeto.

   ```{bash}
   git clone https://github.com/cesargabrielphd/books.git
   ```

2. **Instale as dependências**:

   ```{bash}
   # Quarto
   https://quarto.org/docs/get-started/
   ```

3. **Abra no VS Code** onde está o projeto clonado. 
   ```{bash}
   code .
   ```

## 📝 **Escrevendo**
Pode adicionar suas notas de aulas, interpretações sobre determinado assundo, apenas corrigir erros textuais, ajudar com formulas LaTeX, etc...

## **Renderizar um documento Quarto:**

- Caso deseje apenas renderizar o arquivo e ver o resultado final, use o comando abaixo. Ele renderizará para o formato html, salvando na pasta /book/ na raiz do repositório. `$folder` é o nome da pasta do código da disciplina que deseja renderizar, por exemplo `EST0033`. Veja a lista de disciplinas no arquivo `disciplinas.json`, para o curso de estatistica ofertado pela Universidade de Brasília.


  ```{bash}
  quarto render "build/$folder" --to html --execute --output-dir "./../book$folder"
  ```

- Para atualizações em tempo real, basta usar o parametro `preview` ao invés do `render`

  ```{bash}
  quarto preview "build/$folder" --to html --execute --output-dir "./../book$folder"
  ```

Após terminar de editar, use `CTRL + C` para parar o processo, adicione as mudanças ao git e faça o commit.
Não precisa criar um pull_request, uma action cuidará de atualizar a branch `book` e notificar o repositório principal para renderizar os livros atualizados.

**Exemplo de Commit:**

```{bash}
feat(quarto): adicionar análise estatística para EST0033

🤖 Código 85% gerado por GitHub Copilot
- Análise exploratória de dados
- Gráficos com ggplot2
- Documentação em português
```

## 🚀 **Tecnologias Utilizadas:**

- **[Quarto](https://quarto.org/)**: Sistema de publicação científica e técnica
- **LaTeX**: Formulas matemáticas elegantes
- **R**: Análise estatística e visualização de dados
- **Python**: Ciência de dados e automação
- **GitHub Actions**: Automação de fluxos de trabalho
- **Git**: Controle de versão
- **Visual Studio Code**: Ambiente de desenvolvimento integrado (IDE)
- **GitHub Copilot**: Assistente de codificação
- **Coude Sonnet 4**: Assistente de codificação
- **Coude Gemini Pro**: Assistente de codificação