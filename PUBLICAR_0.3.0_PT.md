# Publicar o PS5 Game Compatibility Atlas 0.3.0

## O que mudou
- A pesquisa é centrada no nome do jogo.
- Os filtros de firmware, formato, armazenamento e estado estão recolhidos por defeito.
- Cada cartão tem um resumo claro e uma secção expansível para os relatos individuais.
- O texto e os alvos de interação foram aumentados para melhorar a leitura em ecrãs pequenos.
- Os dados gerados e a aplicação passam a indicar a versão 0.3.0.

## Validar localmente
Na raiz do projeto, com Python e Node.js instalados:

```bash
python build_data.py
python -m unittest discover -s tests -v
node --check app.js
node --check downloads.js
```

## Publicar
1. Extrai o ZIP da versão 0.3.0.
2. Copia os ficheiros para o repositório `PS5-Game-Compatibility-Atlas`, mantendo a estrutura das pastas.
3. Confirma que `data/atlas-data.js`, `data/atlas-data.json` e `data/atlas-reports.csv` continuam presentes.
4. Faz commit e push para o ramo `main`.
5. Confirma que o workflow de validação passou e que o GitHub Pages publicou a nova versão.
6. Atualiza o navegador com Ctrl+F5.

Não apagues a pasta `data/` nem carregues estes ficheiros para o repositório PS5-Jailbreak-Doctor.
