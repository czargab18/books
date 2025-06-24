# DevContainer - Ambiente de Desenvolvimento

Este devcontainer está configurado para desenvolvimento de livros acadêmicos usando R, Python e Quarto.

## 🚀 Recursos Incluídos

### Linguagens e Ferramentas
- **R** - Para análise estatística e visualização
- **Python** - Para ciência de dados e programação geral
- **Quarto** - Para criação de documentos científicos
- **LaTeX** - Para formatação de documentos acadêmicos
- **Node.js** - Para ferramentas de desenvolvimento web

### Extensões VS Code
- R Language Support
- Python & Pylance
- Jupyter Notebooks
- Quarto Extension
- LaTeX Workshop
- Prettier (formatação de código)

### Pacotes R Pré-instalados
- tidyverse (ggplot2, dplyr, tidyr, etc.)
- rmarkdown, knitr, bookdown
- shiny, plotly
- reticulate (integração R-Python)

### Pacotes Python Pré-instalados
- numpy, pandas, matplotlib, seaborn
- jupyter, jupyterlab
- scikit-learn, scipy, statsmodels
- requests, beautifulsoup4

## 🔧 Configuração

### Portas Configuradas
- **8787** - RStudio Server (se instalado)
- **8080** - Quarto Preview
- **8888** - Jupyter Lab
- **3000-9000** - Portas de desenvolvimento geral

### Comandos Úteis

#### Quarto
```bash
# Renderizar um documento
quarto render documento.qmd

# Visualizar um livro
quarto preview

# Publicar
quarto publish
```

#### Jupyter
```bash
# Iniciar Jupyter Lab
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root

# Iniciar Jupyter Notebook
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

#### R
```bash
# Executar script R
Rscript meu_script.R

# Abrir R console
R
```

## 📁 Estrutura do Projeto

O workspace está organizado por disciplinas:
- `CIC0007/` - Introdução à Computação (Python)
- `EST0033/`, `EST0046/`, `EST0081/`, `EST0091/`, `EST0092/` - Estatística
- `MAT0075/` - Matemática
- `TAS0000/` - Outros tópicos

## 🛠️ Personalização

Para adicionar novos pacotes:

### R
```r
install.packages("nome_do_pacote")
```

### Python
```bash
pip install nome_do_pacote
```

## 📚 Recursos Adicionais

- [Quarto Documentation](https://quarto.org/)
- [R for Data Science](https://r4ds.had.co.nz/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

## 🐛 Troubleshooting

### Problema: Quarto não encontrado
```bash
# Verificar instalação
which quarto
quarto --version

# Reinstalar se necessário
sudo dpkg -i quarto-*.deb
```

### Problema: Kernel R não aparece no Jupyter
```r
# No console R
IRkernel::installspec(user = FALSE)
```

### Problema: LaTeX não compila
```bash
# Instalar pacotes adicionais do LaTeX
sudo apt-get install texlive-full
```
