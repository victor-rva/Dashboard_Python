 # Supermarket Sales Dashboard

Este é um aplicativo Streamlit para análise visual de dados de vendas de supermercado. O código lê um conjunto de dados de vendas de supermercado, permite a seleção de um mês específico e exibe visualizações interativas para análise de faturamento, tipos de produtos, desempenho de filiais, métodos de pagamento e avaliações.

## Como Executar

Certifique-se de ter o Streamlit instalado. Caso não tenha, você pode instalá-lo usando o seguinte comando:

```bash
pip install streamlit
```

Após a instalação, execute o aplicativo Streamlit usando o seguinte comando:

```bash
streamlit run nome_do_arquivo.py
```

O aplicativo será iniciado e você poderá visualizá-lo no navegador padrão.

## Requisitos

Certifique-se de ter as seguintes bibliotecas Python instaladas:

- `streamlit`
- `pandas`
- `plotly`

Você pode instalá-las usando o seguinte comando:

```bash
pip install streamlit pandas plotly
```

## Uso

1. O aplicativo exibirá uma barra lateral com a opção de seleção do mês. Escolha o mês desejado.
2. O gráfico superior à esquerda mostra o faturamento diário por cidade.
3. O gráfico superior à direita exibe o faturamento por tipo de produto ao longo do tempo.
4. O gráfico do meio à esquerda mostra o faturamento total por filial.
5. O gráfico do meio à direita exibe a distribuição do faturamento por tipo de pagamento.
6. O gráfico inferior mostra a avaliação média por cidade.

Sinta-se à vontade para explorar os dados e ajustar a análise conforme necessário!

---

**Observação:** Certifique-se de ter o arquivo "supermarket_sales.csv" no mesmo diretório do script para garantir que os dados sejam carregados corretamente.
