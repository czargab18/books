#!/bin/bash

# Script de configuração para o devcontainer
echo "🚀 Configurando ambiente de desenvolvimento..."

# Atualizar pacotes do sistema
sudo apt-get update

# Instalar dependências adicionais
sudo apt-get install -y \
    curl \
    wget \
    git \
    vim \
    nano \
    tree \
    htop \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    texlive-full \
    pandoc \
    libcurl4-openssl-dev \
    libxml2-dev \
    libssl-dev \
    libfontconfig1-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libfreetype6-dev \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev

# Instalar Quarto
echo "📖 Instalando Quarto..."
wget -q https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.550/quarto-1.4.550-linux-amd64.deb
sudo dpkg -i quarto-1.4.550-linux-amd64.deb
rm quarto-1.4.550-linux-amd64.deb

# Instalar pacotes R essenciais
echo "📊 Instalando pacotes R..."
Rscript -e "
install.packages(c(
  'rmarkdown', 'knitr', 'tinytex', 'bookdown', 'blogdown',
  'ggplot2', 'dplyr', 'tidyr', 'readr', 'purrr', 'tibble',
  'stringr', 'forcats', 'lubridate', 'tidyverse',
  'devtools', 'remotes', 'usethis', 'roxygen2',
  'shiny', 'DT', 'plotly', 'htmlwidgets',
  'reticulate', 'IRkernel', 'languageserver'
), repos='https://cran.rstudio.com/')
"

# Configurar IRkernel para Jupyter
echo "🔧 Configurando IRkernel..."
Rscript -e "IRkernel::installspec(user = FALSE)"

# Instalar pacotes Python essenciais
echo "🐍 Instalando pacotes Python..."
pip install --upgrade pip
pip install \
    jupyter \
    jupyterlab \
    notebook \
    numpy \
    pandas \
    matplotlib \
    seaborn \
    plotly \
    scipy \
    scikit-learn \
    statsmodels \
    requests \
    beautifulsoup4 \
    openpyxl \
    xlrd \
    ipykernel \
    ipywidgets \
    nbconvert \
    nbformat

# Instalar extensões do JupyterLab
echo "🧩 Instalando extensões do JupyterLab..."
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter lab build

# Configurar Git (se necessário)
echo "🔧 Configurando Git..."
git config --global init.defaultBranch main
git config --global core.autocrlf input

# Verificar instalações
echo "✅ Verificando instalações..."
echo "R version: $(R --version | head -1)"
echo "Python version: $(python --version)"
echo "Quarto version: $(quarto --version)"
echo "Jupyter version: $(jupyter --version)"

echo "🎉 Configuração concluída!"
