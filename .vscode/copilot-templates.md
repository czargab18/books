# Configurações Específicas do GitHub Copilot

## Prompts e Contextos Personalizados

### Para Código R:
```
Contexto: Projeto acadêmico em R para análise estatística e visualização de dados.
Estilo: Usar tidyverse, ggplot2, comentários em português.
Sempre incluir: # 🤖 Código gerado por IA - GitHub Copilot
```

### Para Código Python:
```
Contexto: Análise de dados científicos com Python.
Bibliotecas: pandas, numpy, matplotlib, seaborn, scipy.
Sempre incluir: # 🤖 Código gerado por IA - GitHub Copilot
Documentação: docstrings em português.
```

### Para Documentos Quarto:
```
Contexto: Livros acadêmicos e materiais educacionais.
Formato: Usar YAML header completo, chunks de código bem documentados.
Sempre incluir: <!-- 🤖 Documento gerado por IA - GitHub Copilot -->
```

### Para LaTeX:
```
Contexto: Documentos acadêmicos formais (TCC, artigos).
Padrão: ABNT quando necessário, comentários em português.
Sempre incluir: % 🤖 Código LaTeX gerado por IA - GitHub Copilot
```

## Configurações de Chat

### Linguagem: Português Brasileiro
### Tom: Acadêmico, mas acessível
### Estrutura de Respostas:
1. Explicação breve do que será feito
2. Código com comentários em português
3. Indicação clara de que foi gerado por IA
4. Sugestões de melhorias quando relevante

### Exemplos de Prompts Efetivos:

#### Para Análise de Dados:
"Crie uma análise exploratória em R para dados de [contexto]. Inclua gráficos com ggplot2, estatísticas descritivas e interpretação em português. Marque como código gerado por IA."

#### Para Documentação Quarto:
"Gere um documento Quarto para [disciplina] sobre [tópico]. Inclua introdução, desenvolvimento com chunks de código R/Python, conclusão e referências. Formato acadêmico em português."

#### Para Scripts Python:
"Desenvolva um script Python para [objetivo]. Use pandas para manipulação de dados, matplotlib para visualização. Inclua docstrings em português e marque como código IA."

## Templates Rápidos

### Commit Message Template:
```
feat(escopo): descrição em português

🤖 Código [X]% gerado por GitHub Copilot
- Detalhe 1
- Detalhe 2
```

### Header Quarto Template:
```yaml
---
title: "Título do Documento"
author: "César Gabriel Castro de Oliveira"
date: "`r Sys.Date()`"
format: 
  html:
    toc: true
    toc-depth: 3
    code-fold: true
    theme: flatly
  pdf:
    toc: true
    number-sections: true
lang: pt-BR
---
```

### Function Documentation Template Python:
```python
def nome_funcao(parametro: tipo) -> tipo:
    """
    Descrição da função.
    
    🤖 Função gerada por IA - GitHub Copilot
    
    Args:
        parametro: Descrição do parâmetro
        
    Returns:
        Descrição do retorno
        
    Examples:
        >>> nome_funcao(valor)
        resultado_esperado
    """
```

### Function Documentation Template R:
```r
#' Título da Função
#'
#' Descrição detalhada da função.
#' 
#' 🤖 Função gerada por IA - GitHub Copilot
#'
#' @param parametro Descrição do parâmetro
#' @return Descrição do retorno
#' @examples
#' nome_funcao(valor)
#' @export
nome_funcao <- function(parametro) {
  # Código aqui
}
```
