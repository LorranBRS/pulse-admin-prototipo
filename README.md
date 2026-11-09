# Pulse · Painel Admin Master (protótipo)

Protótipo navegável do painel administrativo da plataforma **Pulse**, de avaliação diária de prontidão de funcionários.

**Acesse:** https://lorranbrs.github.io/pulse-admin-prototipo/

> Ambiente de demonstração: qualquer e-mail e senha dão acesso. Todos os dados são fictícios e nada é enviado a servidor. O que for cadastrado ou alterado fica salvo só no navegador de quem está usando; em **Configurações → Restaurar dados de demonstração** tudo volta ao exemplo.

## Telas

- **Login**: acesso simulado e "Esqueci minha senha".
- **Tema claro e escuro**: botão no topo (e na tela de login) para alternar; a escolha fica salva no navegador.
- **Modo apresentação**: funcionário, supervisor e painel lado a lado. Os celulares abrem numa tela de bloqueio com notificação; quando o funcionário responde, o supervisor recebe o aviso, o painel atualiza e o alerta novo aparece em destaque.
- **Animações**: números que contam até o valor, linha do alerta novo em destaque, sino que balança quando chega notificação e aviso de novo alerta no canto da tela (desligadas para quem prefere menos movimento).
- **Perfis de acesso**: seletor "Ver como" no menu lateral (ou no topo, em telas médias). Admin Master vê tudo; Gestor da empresa e Segurança do trabalho veem só a própria empresa e menos telas.
- **Central de notificações**: o sino abre a lista de alertas de hoje, planos de ação vencidos ou vencendo e respostas suspeitas, com marcação de lidas.
- **Dashboard**: indicadores do dia, resultados por período, funil Principais → Avaliação → Adicionais e últimos alertas, com **plano de ação** em cada alerta e aba de **respostas suspeitas** (todas iguais, padrão alternado ou rápidas demais), que podem ser reenviadas.
- **Prazo dos planos de ação** (Dashboard): vencidos, que vencem em até 4 h, pendentes no prazo e percentual registrado dentro do prazo configurado.
- **Empresas**: listagem com busca e filtros, cadastro e edição.
- **Funcionários**: listagem somente por código (LGPD), com tipo, equipe, termo LGPD, resultado do dia e histórico de 30 dias com gráfico de pontuação e indicador de tendência de piora.
- **App do funcionário**: simulador do celular. O funcionário responde as perguntas sorteadas (Principais → Avaliação → Adicionais) e o resultado entra no painel na hora: alerta, notificação ao supervisor, prazo do plano de ação, desvios de tempo e respostas suspeitas. Tem botões de resposta rápida (Apto, Atenção, Risco e "sem ler") para a apresentação.
- **Visão do supervisor**: o app do supervisor no celular, com a equipe por nome (só ele vê nomes, pela LGPD), quem respondeu, quem tem alerta, registro da conversa (vira plano de ação) e lembrete para quem não respondeu.
- **Banco de Perguntas**: 4 grupos de análise com 20+ perguntas cada (texto, imagem na pergunta e alternativas em imagem), 4 perguntas fixas de Avaliação e 4+ Adicionais, edição protegida por senha master e pré-visualização no celular.
- **Configurações**: sorteio por grupo (total de 8 a 12), disparo diário, faixas Apto/Atenção/Risco, tempo mínimo e máximo por resposta, envio das etapas, bloqueio de login, cópia dos alertas de Risco, WhatsApp (opcional), prazo do plano de ação e detecção de respostas suspeitas.

A estrutura segue o documento "Resumo funcionalidades – Aplicativo Pesquisa – LAD" (seção Painel Web – Acesso do Admin).
- **Relatórios**: filtros por período e empresa, volumes diário/mensal/anual, adesão por empresa, respostas fora do tempo limite e exportação simulada.
- **Auditoria**: registro de quem fez o quê e quando (logins, empresas, perguntas, configurações, planos de ação, exportações), com busca e filtros.

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
