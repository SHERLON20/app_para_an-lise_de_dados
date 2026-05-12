📊 Dashboard de Análise de Vendas com Streamlit

Aplicação desenvolvida em Python utilizando <a href="https://streamlit.io/">Streamlit</a> para análise visual de vendas através de gráficos interativos, filtros dinâmicos e integração com API REST.

O sistema consome dados de vendas via API, processa as informações com Pandas e apresenta dashboards analíticos utilizando gráficos construídos com Matplotlib.

Este projeto demonstra conhecimentos em:

Data Analysis
Integração com APIs REST
Visualização de dados
Dashboards interativos
Streamlit
Manipulação de dados com Pandas
🚀 Tecnologias Utilizadas
🐍 Python
📊 Streamlit
🐼 Pandas
📈 Matplotlib
🌐 Requests
🔗 API REST
🎯 Objetivo do Projeto
🐍 Django rest_framework

Este projeto foi desenvolvido com foco em:

Criação de dashboards analíticos
Consumo de APIs REST
Visualização de dados
Manipulação de datasets
Filtros dinâmicos
Exportação de dados
Desenvolvimento de aplicações data-driven

Dashboards analíticos são amplamente utilizados em:

Business Intelligence (BI)
Controle financeiro
Gestão comercial
Monitoramento de vendas
Análise estratégica
📂 Estrutura do Projeto
📦 dashboard-vendas
 ┣ 📜 app.py
 ┗ 📜 README.md
⚙️ Funcionalidades

✅ Consumo de API REST
✅ Filtro por data inicial
✅ Filtro por data final
✅ Busca por produto
✅ Tabela dinâmica de vendas
✅ Exportação para CSV
✅ Gráfico de vendas por data
✅ Gráfico de vendas por produto
✅ Dashboard interativo
✅ Visualização analítica de dados

🧠 Conceitos Aplicados

O projeto utiliza conceitos importantes do ecossistema Python para análise de dados:

Manipulação de DataFrames
Requisições HTTP
Integração com APIs
Visualização de dados
Dashboards interativos
Agrupamento de dados
Filtros dinâmicos
Exportação de relatórios
🌐 Integração com API

A aplicação consome dados da seguinte rota:

http://127.0.0.1:8000/api/sales

Parâmetros suportados:

Parâmetro	Descrição
start_data	Data inicial
end_data	Data final
product	Nome do produto
💻 Exemplo de Resposta da API
[
  {
    "produto": "Notebook",
    "quantidade": 5,
    "data": "2024-01-10"
  },
  {
    "produto": "Mouse",
    "quantidade": 10,
    "data": "2024-01-11"
  }
]
📊 Funcionalidades do Dashboard
📋 Tabela de Dados

O sistema exibe:

Produtos vendidos
Quantidade
Datas
Dataset completo

Além disso, permite exportar os dados diretamente em CSV.

📈 Gráfico de Vendas por Data

O dashboard apresenta:

Evolução temporal das vendas
Quantidade vendida por período
Visualização analítica cronológica
📦 Gráfico de Vendas por Produto

Exibe:

Produtos mais vendidos
Quantidade por item
Comparativo entre produtos
▶️ Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/SEU-USUARIO/dashboard-vendas.git
2️⃣ Acesse a pasta do projeto
cd dashboard-vendas
3️⃣ Crie um ambiente virtual
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
4️⃣ Instale as dependências
pip install pandas requests streamlit matplotlib
5️⃣ Execute o dashboard
streamlit run app.py
🌍 Acesse a Aplicação
http://localhost:8501
📸 Interface Inspirada
6
🏗️ Arquitetura do Projeto

Fluxo principal da aplicação:

API REST
   ↓
Requests
   ↓
Pandas DataFrame
   ↓
Processamento dos dados
   ↓
Dashboard Streamlit
   ↓
Gráficos e relatórios
📈 Visualizações Disponíveis

O sistema gera automaticamente:

📊 Gráfico temporal de vendas
📦 Gráfico de vendas por produto
📋 Dataset completo
📥 Exportação CSV

🔥 Possíveis Melhorias Futuras
 Dashboard em tempo real
 Integração com PostgreSQL
 Login de usuários
 Deploy na nuvem
 Docker
 KPI Cards
 Filtros avançados
 Gráficos interativos com Plotly
 Machine Learning para previsão de vendas
 Exportação PDF
🔒 Tratamento de Erros

A aplicação já possui tratamento para:

✅ Resposta inesperada da API
✅ Conversão de dados
✅ Estrutura inválida de JSON

📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados:

Desenvolvimento de dashboards
Integração com APIs REST
Análise de dados com Pandas
Criação de gráficos
Estruturação de aplicações analíticas
Manipulação de datasets
Desenvolvimento data-driven

Projetos desse tipo são extremamente utilizados em:

Business Intelligence
Analytics
Gestão empresarial
Ciência de dados
Engenharia de dados
👨‍💻 Desenvolvedor

Desenvolvido por Sherlon Machado.

GitHub: https://github.com/SHERLON20/

LinkedIn: https://www.linkedin.com/in/sherlon-machado/
