"""Gera o index.html publicado no GitHub Pages a partir de pulse-admin.html.

pulse-admin.html é o arquivo-fonte (sem <!doctype>/<head>, formato usado no Artifact do Claude).
Este script adiciona a estrutura de documento completa. Rode sempre depois de editar o fonte:

    python3 build.py
"""
from pathlib import Path

raiz = Path(__file__).parent
fonte = (raiz / "pulse-admin.html").read_text(encoding="utf-8")

# Separa o que vai no <head> (meta, title, links, style) do conteúdo da página
corte = fonte.index("</style>") + len("</style>")
cabeca, corpo = fonte[:corte], fonte[corte:]
cabeca = cabeca.replace('<meta charset="utf-8">\n', "")

pagina = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<style>:root{{color-scheme:light}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{cabeca}
</head>
<body>
{corpo.strip()}
</body>
</html>
"""
(raiz / "index.html").write_text(pagina, encoding="utf-8")
print("index.html gerado")
