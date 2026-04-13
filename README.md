# 📊 Dashboard de Análise de Insumos - Abril

Este projeto automatiza a análise de custos de insumos alimentícios a partir de planilhas de fechamento mensal. O objetivo é transformar dados brutos em insights estratégicos para a gestão financeira, focando no comportamento dos custos de proteínas.

## 🚀 Funcionalidades

- **Leitura Híbrida**: Compatibilidade com arquivos Excel (`.xlsx`) e CSV com detecção inteligente de separadores (`,` ou `;`).
- **Tratamento de Dados**: Limpeza de nomes de colunas, remoção de linhas vazias/subtotais e conversão de unidades de volume.
- **Visão Executiva**: Agrupa cortes individuais em categorias macro (Bovino, Frango, Suíno, Pescado).
- **Visualização de Dados**:
  - **Gráfico de Pizza**: Proporção de gastos por setor (Limpeza, Estocáveis, Proteínas, etc).
  - **Gráfico de Eixo Duplo**: Barras para o valor total investido e linha para o custo médio por quilo.

## 🛠️ Tecnologias Utilizadas

- **Python 3.11**
- **Pandas**: Processamento e manipulação de DataFrames.
- **Matplotlib**: Engine gráfica para geração de insights visuais.
- **Openpyxl**: Suporte para leitura de arquivos nativos do Excel.

## 📂 Estrutura do Projeto

```bash
.
├── analise.py               # Script principal em Python
├── ANALÍTICO INSUMOS.xlsx   # Fonte de dados (Planilha de Abril)
└── README.md                # Documentação do projeto

🔧 Como Executar
Instale as dependências via terminal:

pip install pandas matplotlib openpyxl
Certifique-se de que a sua planilha está na mesma pasta do script analise.py.

Execute o comando:
python analise.py