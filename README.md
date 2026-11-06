# Pulse · Painel Admin Master (protótipo)

Protótipo navegável do painel administrativo da plataforma **Pulse**, de avaliação diária de prontidão de funcionários.

**Acesse:** https://lorranbrs.github.io/pulse-admin-prototipo/

> Ambiente de demonstração: qualquer e-mail e senha dão acesso. Todos os dados são fictícios e nada é salvo em servidor (o que for cadastrado vale até recarregar a página).

## Telas

- **Login**: acesso simulado e "Esqueci minha senha".
- **Dashboard**: indicadores do dia, resultados por período, funil Principais → Avaliação → Adicionais e últimos alertas.
- **Empresas**: listagem com busca e filtros, cadastro e edição.
- **Banco de Perguntas**: grupos de análise, perguntas (texto, imagem na pergunta e alternativas em imagem), Avaliação e Adicionais, com pré-visualização no celular.
- **Configurações**: sorteio por grupo, disparo diário, faixas Apto/Atenção/Risco, tempos de resposta, envio das etapas e bloqueio de login.
- **Relatórios**: filtros por período e empresa, volumes diário/mensal/anual, adesão por empresa, respostas fora do tempo limite e exportação simulada.

Por LGPD, funcionários aparecem só por código (ex.: `FUNC-00123`).

## Arquivos

| Arquivo | Função |
|---|---|
| `pulse-admin.html` | Fonte do protótipo (HTML, CSS e JS num arquivo só) |
| `index.html` | Página publicada no GitHub Pages, gerada pelo `build.py` |
| `build.py` | Gera o `index.html` a partir do fonte |

## Atualizar a versão publicada

```bash
python3 build.py
git add -A && git commit -m "Atualiza protótipo" && git push
```

O GitHub Pages atualiza o link em cerca de 1 minuto.

## Trocar o nome do produto

Procure por `Pulse` em `pulse-admin.html` (título, logotipo e textos) e rode o `build.py`.
