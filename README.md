# 📊 Análise de Portefólio de Investimentos

Aplicação em Python (com [Streamlit](https://streamlit.io)) para analisar o teu
portefólio de investimentos: carregas um ficheiro CSV com os teus ativos e a
aplicação calcula o valor total investido e mostra gráficos interativos
(Pie Charts ou Treemaps) da distribuição por **Tipo de Ativo**, **Setor** e
**País**.

Este guia assume que **não tens nada instalado no computador** e explica
todos os passos, um a um.

---

## 1. Instalar o Python

O Python é a linguagem de programação necessária para correr esta aplicação.

### Windows
1. Vai a https://www.python.org/downloads/ e clica no botão amarelo "Download
   Python 3.x.x".
2. Abre o ficheiro descarregado (`python-3.x.x-amd64.exe`).
3. **Muito importante:** na primeira janela do instalador, marca a caixa
   **"Add python.exe to PATH"** (fica no fundo da janela) antes de clicares em
   "Install Now".
4. Espera que a instalação termine e clica em "Close".
5. Para confirmar que funcionou, abre a aplicação **Prompt de Comando** (procura
   por "cmd" no menu Iniciar) e escreve:
   ```
   python --version
   ```
   Deve aparecer algo como `Python 3.12.x`.

### macOS
1. Vai a https://www.python.org/downloads/ e descarrega o instalador para macOS.
2. Abre o ficheiro `.pkg` e segue os passos do instalador (Continuar → Continuar
   → Aceitar → Instalar).
3. Abre a aplicação **Terminal** (procura por "Terminal" no Spotlight, com
   Cmd+Espaço) e escreve:
   ```
   python3 --version
   ```
   Deve aparecer algo como `Python 3.12.x`.

---

## 2. Obter os ficheiros da aplicação

Se já tens esta pasta no teu computador (por exemplo, porque a
descarregaste ou clonaste do GitHub), passa diretamente ao passo 3.

Se não tens, cria uma pasta no teu computador (por exemplo, no Ambiente de
Trabalho, chamada `portefolio-app`) e coloca lá dentro os seguintes ficheiros:
- `app.py`
- `requirements.txt`
- `sample_portfolio.csv`

---

## 3. Abrir o terminal na pasta do projeto

- **Windows:** abre a pasta no Explorador de Ficheiros, clica na barra de
  endereço no topo, escreve `cmd` e prime Enter. Abre-se um Prompt de
  Comando já dentro dessa pasta.
- **macOS:** abre o **Terminal** e escreve `cd ` (com um espaço a seguir),
  depois arrasta a pasta do projeto para dentro da janela do Terminal e
  prime Enter.

---

## 4. Criar um "ambiente virtual" (recomendado)

Um ambiente virtual isola as bibliotecas desta aplicação do resto do
computador, evitando conflitos. É um passo opcional mas recomendado.

**Windows:**
```
python -m venv venv
venv\Scripts\activate
```

**macOS:**
```
python3 -m venv venv
source venv/bin/activate
```

Se funcionou, deves ver `(venv)` no início da linha do terminal.

> Sempre que voltares a abrir o terminal para usar a aplicação noutro dia,
> tens de repetir apenas o comando de ativação (`venv\Scripts\activate` ou
> `source venv/bin/activate`), não é preciso criar o ambiente virtual outra
> vez.

---

## 5. Instalar as bibliotecas necessárias

Com o ambiente virtual ativado (ou sem ele, se optaste por saltar o passo
4), escreve no terminal:

**Windows:**
```
pip install -r requirements.txt
```

**macOS:**
```
pip3 install -r requirements.txt
```

Isto vai instalar automaticamente o Streamlit, o Pandas (para tratar os
dados) e o Plotly (para os gráficos interativos). Pode demorar um a dois
minutos.

---

## 6. Correr a aplicação

Ainda no mesmo terminal, escreve:

```
streamlit run app.py
```

O terminal vai mostrar umas linhas de texto e, ao fim de alguns segundos, o
teu browser (Chrome, Edge, etc.) abre-se automaticamente com a aplicação a
funcionar em `http://localhost:8501`.

Se o browser não abrir sozinho, copia o endereço `http://localhost:8501`
que aparece no terminal e cola-o na barra do teu browser.

Para parar a aplicação, volta ao terminal e prime `Ctrl + C`.

---

## 7. Usar a aplicação

1. Clica na área "Carrega o teu ficheiro CSV" e escolhe um ficheiro CSV
   com o teu portefólio. Podes começar por testar com o ficheiro de
   exemplo incluído, `sample_portfolio.csv`.
2. A aplicação mostra automaticamente:
   - O **valor total investido**, o número de posições e o número de ativos
     distintos;
   - A **tabela** com todos os teus ativos e o valor investido em cada um;
   - **Gráficos interativos** (podes escolher entre Pie Chart ou Treemap) com
     a distribuição do teu portefólio por Tipo de Ativo, Setor e País.

### Formato do ficheiro CSV

O ficheiro CSV do teu portefólio real tem de ter estas colunas, com estes
nomes exatos:

| Coluna | Descrição | Exemplo |
|---|---|---|
| `Ticker` | Símbolo do ativo | `AAPL` |
| `Quantidade` | Número de unidades detidas | `10` |
| `Preco_Medio_Compra` | Preço médio pago por unidade | `150.50` |
| `Tipo_Ativo` | Um de: Ações, ETF, Crypto, P2P | `Ações` |
| `Setor` | Setor económico do ativo | `Tecnologia` |
| `Pais` | País do ativo/empresa | `EUA` |

Podes criar/editar este ficheiro facilmente no Excel: preenche as colunas
com estes nomes na primeira linha e, ao guardar, escolhe o formato
**"CSV (delimitado por vírgulas)"**.

---

## Resolução de problemas comuns

- **"python não é reconhecido como um comando"** (Windows): o Python não
  ficou no PATH. Reinstala o Python e não te esqueças de marcar a caixa
  "Add python.exe to PATH" no instalador.
- **"streamlit não é reconhecido como um comando"**: confirma que ativaste
  o ambiente virtual (passo 4) antes de instalar as bibliotecas (passo 5) e
  antes de correr a aplicação (passo 6).
- **O browser não abre automaticamente**: copia manualmente o endereço
  `http://localhost:8501` do terminal para o browser.
- **Erro sobre colunas em falta no CSV**: confirma que os nomes das colunas
  no teu ficheiro são exatamente os indicados na tabela acima (maiúsculas/
  minúsculas incluídas, sem espaços a mais).
