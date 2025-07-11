# 📚 Books - Livros Acadêmicos com Quarto

<!-- 🤖 README melhorado por IA - GitHub Copilot -->

> **Projeto acadêmico para criação de livros e materiais educacionais** utilizando Quarto, R, Python e LaTeX, com foco em disciplinas de Estatística, Matemática e Ciência da Computação.

## 🎯 Descrição

Este repositório contém **anotações, códigos e projetos acadêmicos** desenvolvidos com o [Quarto](https://quarto.org/), organizados por disciplinas universitárias. O projeto combina diferentes linguagens e formatos para criar materiais educacionais interativos e de alta qualidade.

### 🚀 **Tecnologias Utilizadas:**

- **[Quarto](https://quarto.org/)**: Sistema de publicação científica e técnica
- **R**: Análise estatística e visualização de dados
- **Python**: Ciência de dados e automação
- **LaTeX**: Documentos acadêmicos formais
- **Jupyter Notebooks**: Análises interativas
- **HTML/CSS**: Apresentações web

### 🤖 **Desenvolvimento Assistido por IA**

- **Mínimo 75% do código é gerado ou assistido por IA** (GitHub Copilot)
- Todas as contribuições de IA são devidamente marcadas e documentadas
- Uso responsável e transparente de ferramentas de IA

## 📁 Estrutura do Projeto

```
books/
├── 📋 .devcontainer/          # Ambiente de desenvolvimento (Codespace)
├── 🔧 .github/                # Templates e workflows GitHub
├── ⚙️  .vscode/               # Configurações VS Code + Copilot
├── 🌐 build/                  # Arquivos compilados e disciplinas
│   ├── 📊 CIC0007/           # Introdução à Computação (Python)
│   ├── 📈 EST0033/           # Estatística Exploratória
│   ├── 📉 EST0046/           # Métodos Estatísticos
│   ├── 📐 EST0081/           # TCC - Trabalho de Conclusão
│   ├── 🔢 EST0091/           # Computação Estatística I
│   ├── 🧮 EST0092/           # Computação Estatística II
│   ├── ➕ MAT0075/           # Matemática Básica
│   ├── 📝 TAS0000/           # Tópicos Diversos
│   └── � _arquivos/         # Recursos compartilhados
├── 📄 .gitignore             # Arquivos ignorados pelo Git
└── 📖 README.md              # Documentação principal
```

### 📚 **Disciplinas Incluídas:**

- **CIC0007**: Introdução à Ciência da Computação
- **EST0033**: Estatística Exploratória
- **EST0046**: Métodos Estatísticos
- **EST0081**: Trabalho de Conclusão de Curso
- **EST0091/092**: Computação Estatística I e II
- **MAT0075**: Matemática Básica
- **TAS0000**: Tópicos Avançados em Estatística
- **\_arquivos**: Ementas e materiais de planejamento

## 🚀 Como Usar

### 🌥️ **Opção 1: GitHub Codespace (Recomendado)**

1. **Abra no Codespace**: Clique em "Code" → "Codespaces" → "Create codespace on main"
2. **Ambiente pré-configurado**: R, Python, Quarto e LaTeX já instalados
3. **VS Code otimizado**: Extensões e configurações personalizadas

### 💻 **Opção 2: Local**

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/cesargabrielphd/books.git
   cd books
   ```

2. **Instale as dependências**:

   ```bash
   # Quarto
   https://quarto.org/docs/get-started/

   # R packages
   install.packages(c("tidyverse", "ggplot2", "rmarkdown", "knitr"))

   # Python packages
   pip install pandas numpy matplotlib jupyter quarto
   ```

3. **Abra no VS Code**:
   ```bash
   code .
   ```

### 📝 **Trabalhando com os Documentos**

#### **Renderizar um documento Quarto:**

```bash
quarto render documento.qmd
```

#### **Visualizar em tempo real:**

```bash
quarto preview
```

#### **Executar análises R:**

```r
# Abrir arquivo .qmd ou .Rmd no VS Code
# Usar Ctrl+Shift+Enter para executar chunks
```

#### **Executar notebooks Python:**

```bash
jupyter lab
# ou usar diretamente no VS Code
```

## 🎨 Estrutura das Branches

- **🌟 `main`**: Código principal e documentação finalizada
- **🔧 `dev1`**: Desenvolvimento de novas funcionalidades
- **🧪 `stag`**: Ambiente de teste e validação
- **📖 `books`**: Deploy automático para GitHub Pages

## 🤖 Uso Responsável de IA

Este projeto utiliza **GitHub Copilot** e outras ferramentas de IA de forma transparente:

### ✅ **Diretrizes de IA:**

- **Mínimo 75% do código** é marcado como gerado por IA
- Uso de comentários específicos: `# 🤖 Código gerado por IA - GitHub Copilot`
- Commits incluem percentual de código gerado por IA
- Documentação completa em [`.copilot-instructions.md`](.copilot-instructions.md)

### 📝 **Exemplo de Commit:**

```
feat(quarto): adicionar análise estatística para EST0033

🤖 Código 85% gerado por GitHub Copilot
- Análise exploratória de dados
- Gráficos com ggplot2
- Documentação em português
```

## 🛠️ Desenvolvimento

### **Configurações Incluídas:**

- **DevContainer**: Ambiente completo para Codespace
- **VS Code Settings**: Configurações otimizadas para R, Python, Quarto
- **GitHub Copilot**: Templates e snippets personalizados
- **Extensões**: Lista curada de extensões essenciais

### **Comandos Úteis:**

```bash
# Renderizar todos os documentos
quarto render

# Limpar arquivos temporários
find . -name "*_files" -type d -exec rm -rf {} +

# Atualizar dependências R
Rscript -e "update.packages(ask = FALSE)"

# Instalar pacotes Python
pip install -r requirements.txt
```

## 📊 Estatísticas do Projeto

- **📚 Disciplinas**: 8+ disciplinas universitárias
- **📄 Documentos**: 50+ arquivos Quarto/RMarkdown
- **🔬 Análises**: 100+ scripts R e Python
- **🤖 IA**: 75%+ código assistido por GitHub Copilot
- **📖 Páginas**: Disponível em [GitHub Pages](https://cesargabrielphd.github.io/books/)

## 🎓 Sobre o Autor

**César Gabriel Castro de Oliveira**

- 🎓 Estatística - Universidade de Brasília (UnB)
- 💼 Especialização em Ciência de Dados
- 🤖 Entusiasta de IA aplicada à educação

## 🤝 Como Contribuir

1. **Fork** o repositório
2. **Crie** uma branch: `git checkout -b feature/nova-funcionalidade`
3. **Commit** suas mudanças: `git commit -m 'feat: adicionar nova funcionalidade 🤖 Código 80% gerado por IA'`
4. **Push** para a branch: `git push origin feature/nova-funcionalidade`
5. **Abra** um Pull Request

### 📋 **Checklist para Contribuições:**

- [ ] Código comentado em português
- [ ] Indicação de código gerado por IA (mín. 75%)
- [ ] Documentação atualizada
- [ ] Testes funcionais (quando aplicável)
- [ ] Commit message segue o padrão do projeto

## 📄 Licença

Este projeto está sob a licença **MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🔗 Links Úteis

- 📖 **Site do Projeto**: [books.estatistica.pro](https://cesargabrielphd.github.io/books/)
- 📚 **Documentação Quarto**: [quarto.org](https://quarto.org/)
- 🤖 **GitHub Copilot**: [github.com/features/copilot](https://github.com/features/copilot)
- 📊 **R for Data Science**: [r4ds.had.co.nz](https://r4ds.had.co.nz/)
- 🐍 **Python Data Science**: [jakevdp.github.io/PythonDataScienceHandbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

---

<div align="center">

**📚 Construído com ❤️ e 🤖 IA**

_Este repositório é atualizado continuamente com novos conteúdos e melhorias._

</div>

---

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
# voltar para a pasta raiz do projeto
cd ../..
```

ou mais compacto:

```
cd .\build\EST0033\ ; quarto render . ; cd ../.. ;
python run/cleanBooks.py --base-dir book/ --base-ac .\build\ac\books\
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
