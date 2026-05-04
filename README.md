# Legal Ops Strategic Analytics: Jurimetria e Gestão de Risco

Este projeto simula uma operação de **Legal Operations** em um grande escritório de advocacia ou departamento jurídico corporativo. O objetivo é transformar dados brutos de tribunais em insights estratégicos para tomada de decisão financeira e operacional.

## 🚀 Pilares do Projeto

*   **Financial Intelligence:** Gestão de Provisão (CPC 25) e análise de *Exposure* (Exposição Financeira).
*   **Operational Efficiency:** Monitoramento de *Lead Time* processual e identificação de gargalos por Comarca/UF.
*   **Risk Management:** Matriz de risco baseada em probabilidade de êxito e custo de defesa.
*   **Data-Driven Decisions:** Dashboards interativos para visualização de KPIs críticos.

## 📊 Metodologia

1.  **Dados Reais:** Utilização do dataset *Brazilian Legal Proceedings* (Kaggle), contendo movimentações reais de tribunais brasileiros.
2.  **Enriquecimento (Legal Ops):** Script Python desenvolvido para injetar camadas de negócio:
    *   Classificação de Risco Contábil (Provável, Possível, Remoto).
    *   Simulação de Valor da Causa e Provisão Financeira.
    *   Cálculo de Custos de Defesa e SLAs.
3.  **Análise:** Notebooks Jupyter para EDA e validação de hipóteses.

## 📁 Estrutura do Repositório

*   `data/`: Datasets (Brutos ignorados no Git, Enriquecidos incluídos).
*   `notebooks/`: Análise exploratória e visualizações.
*   `scripts/`: Scripts de automação e engenharia de dados.
*   `docs/`: Documentação metodológica.

---
**Desenvolvido por Rodrigo Cruz para portfólio de Legal Analytics.**
