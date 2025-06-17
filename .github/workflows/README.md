# Action: Render Books

A action `build.render.yml` é usada para automatizar o processo de renderização de livros criados com Quarto e realizar o deploy para o GitHub Pages.

## Lógica da Action

- A ação é acionada nos seguintes eventos:
  - `push` para as branches `main` e `dev1`.
  - `pull_request` para as branches `main` e `dev1`.
  - `workflow_dispatch` para execução manual.

## Estrutura dos Jobs

### 1. `evento`
Identifica o tipo de evento que acionou a action (`push`, `pull_request`, `workflow_dispatch`, etc.) e exporta o tipo de evento como output.

### 2. `detectar`
Clona o repositório, identifica os arquivos alterados e monta uma lista única de subdiretórios que contêm mudanças. Exporta essa lista como output e artefatos da pasta.

### 3. `renderizar`
Renderiza os livros Quarto nos subdiretórios detectados e salva os resultados no diretório `_books`.

### 4. `backend`
Executa automações adicionais no backend, utilizando os livros renderizados como entrada.

### 5. `pages`
Realiza o deploy dos livros renderizados para o GitHub Pages na branch `books`.

## Como Funciona

1. **Identificação de Arquivos Alterados**:
   - Verifica os arquivos `.qmd` e `.yml` alterados no diretório `build/`.
   - Extrai os subdiretórios afetados.

2. **Renderização dos Livros**:
   - Utiliza o comando `quarto render` para gerar os livros em formato HTML.

3. **Automação no Backend**:
   - Executa scripts Python no backend para processar os livros renderizados.

4. **Deploy para GitHub Pages**:
   - Publica os livros renderizados na branch `books`.

## Configuração

### Permissões
A action requer as seguintes permissões:
- `contents: write` para modificar o conteúdo do repositório.
- `pages: write` para realizar o deploy no GitHub Pages.
- `pull-requests: read` para ler informações de pull requests.

### Variáveis de Ambiente
- `GITHUB_TOKEN`: Token padrão do GitHub Actions.
- `REPO_SYNC`: Token para sincronização entre repositórios.
- `USEREMAIL` e `USERNAME`: Informações do usuário para commits e deploy.

## Observações

- Certifique-se de que os arquivos `.qmd` e `.yml` estão localizados no diretório `build/`.
- A branch `books` deve estar configurada como destino para o GitHub Pages.

## Exemplo de Uso

Para executar manualmente a action:
1. Vá até a aba "Actions" no repositório.
2. Selecione a action `[build] - Renderizar Books Quarto`.
3. Clique em "Run workflow" e escolha a branch desejada.