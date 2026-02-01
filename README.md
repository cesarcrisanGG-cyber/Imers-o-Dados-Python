# 📊 Dashboard de Salários

Dashboard interativo desenvolvido em **Python** com **Streamlit**, **Pandas** e **Plotly**, com foco em **análise exploratória e visualização de dados salariais** na área de tecnologia.

O projeto permite analisar salários por **ano, senioridade, tipo de contrato, modalidade de trabalho e país**, oferecendo uma visão clara e interativa do mercado.

---

## 🚀 Demonstração

> O dashboard é executado localmente via Streamlit e pode ser facilmente publicado no **Streamlit Cloud**.

---

## 🧠 Objetivo do Projeto

Este projeto foi criado com o objetivo de:

* Praticar **análise de dados com Pandas**
* Criar **dashboards interativos** com Streamlit
* Utilizar **visualizações adequadas para cada tipo de pergunta**
* Desenvolver um projeto apresentável para **portfólio profissional**

---

## 📂 Fonte dos Dados

Os dados utilizados vêm de um conjunto público contendo informações sobre salários na área de tecnologia, incluindo:

* Ano
* Cargo
* Senioridade
* Tipo de contrato
* Modalidade de trabalho (remoto, híbrido, presencial)
* País de residência
* Salário em USD

Os dados são carregados diretamente via URL usando `pandas.read_csv()`.

---

## 🎛️ Funcionalidades

### 🔍 Filtros Interativos

Disponíveis na barra lateral:

* Ano
* Senioridade
* Tipo de contrato
* Modalidade de trabalho

Todos os gráficos e indicadores reagem dinamicamente aos filtros selecionados.

---

### 📌 Indicadores (KPIs)

No topo do dashboard:

* 💰 Salário médio (USD)
* 📊 Salário mediano (USD)
* 🚀 Salário máximo (USD)
* 🧮 Total de registros analisados

---

### 📊 Visualizações

O dashboard utiliza diferentes tipos de gráficos, escolhidos de acordo com o tipo de análise:

* 🌍 **Mapa (Choropleth)** – Salário médio por país
* 🥧 **Gráfico de pizza** – Distribuição por senioridade
* 🥧 **Gráfico de pizza** – Modalidade de trabalho
* 🥧 **Gráfico de pizza** – Média salarial por tipo de contrato
* 🏆 **Gráfico de barras** – Top 10 cargos com maior salário médio

O layout é organizado em **duas colunas**, mantendo boa legibilidade e hierarquia visual.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Streamlit** – Interface e interatividade
* **Pandas** – Manipulação e análise de dados
* **Plotly Express** – Visualizações interativas

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/cesarcrisanGG-cyber/Imers-o-Dados-Python.git
cd Imers-o-Dados-Python
```

### 2️⃣ Crie e ative um ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute o Streamlit

```bash
streamlit run app.py
```

---

## 📈 Possíveis Evoluções

* Publicação no **Streamlit Cloud**
* Gráfico de evolução salarial ao longo do tempo
* Comparação entre países ou senioridades específicas
* Adição de storytelling com insights automáticos

---

## 👤 Autor

Projeto desenvolvido por **Crisan Cesar**.

GitHub: [https://github.com/cesarcrisanGG-cyber](https://github.com/cesarcrisanGG-cyber)

📌 Em aprendizado contínuo em **Análise de Dados e Desenvolvimento em Python**.

---

## ⭐ Considerações Finais

Este projeto demonstra:

* Capacidade de estruturar dados
* Escolha adequada de visualizações
* Uso consciente de interatividade
* Organização de código e layout

Ideal como **projeto de portfólio** para áreas como:

* Análise de Dados
* Business Intelligence
* Data Science (nível iniciante/intermediário)

---

Se você gostou do projeto, fique à vontade para ⭐ o repositório!

