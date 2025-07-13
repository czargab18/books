import argparse
import re
import os
from bs4 import BeautifulSoup


class LimparHTML:
    def __init__(self, remove_quarto_header=True, remove_selectors=None, base_ac_path=None):
        self.remove_quarto_header = remove_quarto_header
        self.remove_selectors = remove_selectors or []
        if base_ac_path:
            self.base_ac_path = base_ac_path
        else:
            self.base_ac_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "build")

    @staticmethod
    def preservar_links_seo(head_soup, novo_head_soup):
        # Preserva <link rel="next"> e <link rel="prev"> do head original
        for rel in ["next", "prev"]:
            for link in head_soup.find_all("link", rel=rel):
                # Evita duplicidade: só adiciona se não existe no novo head
                if not novo_head_soup.find("link", rel=rel):
                    novo_head_soup.append(link)
        return novo_head_soup

    @staticmethod
    def substituir_head(html, novo_head_html):
        """
        Substitui apenas o conteúdo interno da tag <head> do HTML pelo conteúdo de novo_head_html.
        """
        soup = BeautifulSoup(html, "html.parser")
        novo_head_soup = BeautifulSoup(novo_head_html, "html.parser")
        head_tag = soup.find("head")
        if head_tag:
            # Preserva links SEO antes de substituir
            LimparHTML.preservar_links_seo(head_tag, novo_head_soup)
            for child in list(head_tag.contents):  # type: ignore
                child.extract()
            for elem in novo_head_soup.find_all(recursive=False):
                head_tag.append(elem)  # type: ignore
        return str(soup)

    def limpar(self, html):
        soup = BeautifulSoup(html, "html.parser")
        if self.remove_quarto_header:
            # ids = ["quarto-header", "title-block-header"]
            ids = ["quarto-header", "title-block-header"]
            for header_id in ids:
                header = soup.find("header", id=header_id)
                if header:
                    header.decompose()
        # Remove divs com classes específicas
        classes_remover = [
            "pt-lg-2 mt-2 text-left sidebar-header",
            "mt-2 flex-shrink-0 align-items-center"
        ]
        for class_name in classes_remover:
            for div in soup.find_all("div", class_=class_name):
                div.decompose()
        # Remove o pai da div com class="sidebar-search"
        for div_search in soup.find_all("div", class_="sidebar-search"):
            parent = div_search.find_parent("div")
            if parent:
                parent.decompose()
            else:
                div_search.decompose()
        for tag, attrs in self.remove_selectors:
            for elem in soup.find_all(tag, attrs=attrs):
                elem.decompose()
        return str(soup)

    def limpar_arquivo_html(self, caminho):
        with open(caminho, encoding="utf-8") as f:
            html = f.read()
        # Salva links SEO antes de qualquer alteração
        soup_original = BeautifulSoup(html, "html.parser")
        head_tag = soup_original.find("head")
        links_seo = []
        from bs4 import Tag
        if isinstance(head_tag, Tag):
            for rel in ["next", "prev"]:
                links_seo.extend(head_tag.find_all("link", rel=rel))
        # Substitui o head se o arquivo build/head.html existir
        build_head_path = os.path.join(self.base_ac_path, "head.html")
        if os.path.exists(build_head_path):
            with open(build_head_path, encoding="utf-8") as f:
                novo_head = f.read()
            html = LimparHTML.substituir_head(html, novo_head)
        html_limpo = self.limpar(html)
        # Adiciona os links SEO novamente ao head
        soup_limpo = BeautifulSoup(html_limpo, "html.parser")
        head_limpo = soup_limpo.find("head")
        if isinstance(head_limpo, Tag):
            for link in links_seo:
                if not head_limpo.find("link", rel=link.get("rel")):
                    head_limpo.append(link)
        # Insere o conteúdo do globalheader.html após a abertura do <body>
        globalheader_path = os.path.join(
            self.base_ac_path, "globalheader.html")
        if os.path.exists(globalheader_path):
            with open(globalheader_path, encoding="utf-8") as f:
                globalheader_html = f.read()
            body_tag = soup_limpo.find("body")
            if isinstance(body_tag, Tag):
                # Verifica se já existe o conteúdo do globalheader pelo id ou classe principal
                globalheader_soup = BeautifulSoup(
                    globalheader_html, "html.parser")
                # Exemplo: verifica se existe um elemento com id="globalheader"
                existe_globalheader = False
                gh_tag = globalheader_soup.find(True, id=True)
                if gh_tag and body_tag.find(True, id=gh_tag.get("id")): # type: ignore
                    existe_globalheader = True
                # Se não existir, insere
                if not existe_globalheader:
                    body_tag.insert(0, globalheader_soup)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(str(soup_limpo))
        print(f"Arquivo limpo: {caminho}")

    def rel_seo(self, html):
        """
        Retorna todos os links <link rel="next"> e <link rel="prev"> presentes no <head> do HTML.
        """
        soup = BeautifulSoup(html, "html.parser")
        head_tag = soup.find("head")
        links_seo = []
        from bs4 import Tag
        if isinstance(head_tag, Tag):
            for rel in ["next", "prev"]:
                links_seo.extend(head_tag.find_all("link", rel=rel))
        return links_seo

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
    parser.add_argument("--base-ac", type=str,
                        help="Diretório dos componentes (ex: globalheader.html e head.html).")
    args = parser.parse_args()

    limpador = LimparHTML(base_ac_path=args.base_ac)

    if args.base_dir:
        limpador.limpar_recursivo(args.base_dir)
    elif args.file:
        limpador.limpar_arquivo_html(args.file)
    else:
        print(
            "Informe --base-dir para limpar recursivamente ou --file para um arquivo único.")
