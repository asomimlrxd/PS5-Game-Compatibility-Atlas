# PS5 Game Compatibility Atlas — Português (Portugal)

O **PS5 Game Compatibility Atlas** organiza relatos públicos de jogos PS5 em ambientes homebrew, cruzando firmware, formato, armazenamento, sintomas, duração do teste e fontes originais.

## Começar

Executa na pasta do projeto:

```bash
python -m http.server 8000
```

Abre depois `http://localhost:8000`. O site não precisa de uma API ou base de dados remota.

## O que contém

- 83 registos de teste e 46 nomes de jogos/títulos.
- 18 fontes públicas e 7 guias de formato.
- Pesquisa e filtros por firmware, formato, armazenamento e estado.
- Português de Portugal e inglês, com tema escuro e interface adaptável.
- Links diretos às fontes; não existem links para downloads de jogos.
- Formulário de contribuição local: os dados ficam no teu navegador e podem ser exportados para JSON. Não são enviados para um servidor.
- Exportação dos registos curados para CSV ou JSON.

## Interpretação

Um registo descreve uma configuração e uma observação — não define o estado universal de um jogo. «Teste curto» não equivale a conclusão, e resultados contraditórios permanecem separados. A qualidade da evidência descreve quão bem o relato está documentado, não uma probabilidade estatística de sucesso.

A documentação atual do ShadowMountPlus recomenda `.ffpkg`/UFS para uso geral, apresenta `.exfat` como opção de compatibilidade para alguns títulos e classifica PFS (`.ffpfs`/`.ffpfsc`) como experimental. Os resultados específicos por jogo podem divergir destas indicações.

Consulta `METHODOLOGY.md` para conhecer as fontes e limitações e `CONTRIBUTING.md` antes de introduzir novos resultados.
