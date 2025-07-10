import argparse
import re
import os
from bs4 import BeautifulSoup


class LimparHTML:
    def __init__(self, remove_quarto_header=True, remove_selectors=None):
        """
        Classe para remover conteúdos de HTML.
        :param remove_quarto_header: Remove o <header id="quarto-header"> se True
        :param remove_selectors: Lista de seletores (tuplas: (tag, dict_atributos)) para remoção
        """
        self.remove_quarto_header = remove_quarto_header
        self.remove_selectors = remove_selectors or []

    @staticmethod
    def substituir_head(html, novo_head_html):
        """
        Substitui apenas o conteúdo interno da tag <head> do HTML pelo conteúdo de novo_head_html.
        """
        soup = BeautifulSoup(html, "html.parser")
        novo_head_soup = BeautifulSoup(novo_head_html, "html.parser")
        head_tag = soup.find("head")
        if head_tag:
            for child in list(head_tag.contents):  # type: ignore
                child.extract()
            for elem in novo_head_soup.find_all(recursive=False):
                head_tag.append(elem)  # type: ignore
        return str(soup)

    def limpar(self, html):
        soup = BeautifulSoup(html, "html.parser")
        if self.remove_quarto_header:
            ids = ["quarto-header", "title-block-header"]
            for header_id in ids:
                header = soup.find("header", id=header_id)
                if header:
                    header.decompose()
        for tag, attrs in self.remove_selectors:
            for elem in soup.find_all(tag, attrs=attrs):
                elem.decompose()
        return str(soup)

    def limpar_arquivo_html(self, caminho):
        with open(caminho, encoding="utf-8") as f:
            html = f.read()
        # Substitui o head se o arquivo build/head.html existir
        build_head_path = os.path.join(os.path.dirname(
            os.path.dirname(__file__)), "build", "head.html")
        if os.path.exists(build_head_path):
            with open(build_head_path, encoding="utf-8") as f:
                novo_head = f.read()
            html = LimparHTML.substituir_head(html, novo_head)
        html_limpo = self.limpar(html)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(html_limpo)
        print(f"Arquivo limpo: {caminho}")

    def limpar_recursivo(self, base_dir):
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file.lower().endswith(".html"):
                    caminho = os.path.join(root, file)
                    self.limpar_arquivo_html(caminho)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Limpa arquivos HTML removendo headers específicos.")
    parser.add_argument("--base-dir", type=str,
                        help="Diretório base para limpeza recursiva de arquivos HTML.")
    parser.add_argument("--file", type=str,
                        help="Arquivo HTML único para limpar.")
    args = parser.parse_args()

    limpador = LimparHTML()

    if args.base_dir:
        limpador.limpar_recursivo(args.base_dir)
    elif args.file:
        limpador.limpar_arquivo_html(args.file)
    else:
        print(
            "Informe --base-dir para limpar recursivamente ou --file para um arquivo único.")
