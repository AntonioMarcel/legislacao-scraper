# Legislação Scraper

Scraper assíncrono para extração de dados de legislação do portal [legislacao.presidencia.gov.br](https://legislacao.presidencia.gov.br/#).

Extrai título, ementa, status, link da norma e link da ficha de cada legislação publicada, salvando os dados em formato JSONL.

## Estrutura do projeto

```
legislacao-scraper/
├── main.py
├── requirements.txt
└── scraper/
    ├── __init__.py
    ├── config.py
    ├── models.py
    ├── parser.py
    ├── scraper.py
    └── writer.py
```

## Pré-requisitos

- Python 3.12
- Git

## Instalação

**1. Clone o repositório:**

```bash
git clone <url-do-repositorio>
cd legislacao-scraper
```

**2. Crie e ative o ambiente virtual:**

```bash
python -m venv .venv
source .venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Instale o browser do Playwright:**

```bash
playwright install chromium
```

## Execução

```bash
python main.py
```

O scraper vai:
1. Abrir o portal de legislação
2. Acionar a pesquisa
3. Calcular o total de páginas dinamicamente
4. Navegar por todas as páginas extraindo os dados
5. Salvar os resultados em `output/output.jsonl`

## Output

O arquivo gerado segue o formato JSONL — um registro JSON por linha:

```json
{"titulo": "Lei nº 15.374 de 02 de abril de 2026", "ementa": "Cria cargos efetivos...", "status": "Não consta revogação expressa", "link_ficha": "https://...", "link_norma": "https://..."}
```

## Pendências e melhorias futuras

- Adicionar logging estruturado substituindo os `print`
- Adicionar tratamento de erros e retomada em caso de falha
- Implementar carga incremental — raspar apenas legislações novas
- Refatorar para `httpx` + `BeautifulSoup` para maior performance
