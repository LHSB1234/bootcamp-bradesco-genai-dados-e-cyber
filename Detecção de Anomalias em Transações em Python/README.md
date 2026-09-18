# Detecção de Anomalias em Transações em Python

Projeto desenvolvido para o módulo de **Análise de dados com Python: Da Preparação à aplicação com Segurança**, com foco na aplicação de análise de dados e Machine Learning para identificar transações potencialmente fraudulentas.

---

## Sobre o Projeto

A detecção de fraudes é um problema relevante para **Cibersegurança, Segurança da Informação e análise de dados financeiros**.

O desafio consiste em analisar transações, identificar padrões associados às classes normal e fraudulenta e avaliar modelos capazes de auxiliar na identificação de operações potencialmente suspeitas.

O projeto contempla todo o fluxo:

```text
Dados → Preparação → Análise → Modelagem → Avaliação → Otimização → Explicabilidade
```

O modelo deve ser entendido como uma **ferramenta de apoio à análise de risco**, e não como uma confirmação definitiva de fraude.

---

## Objetivos

* Analisar e preparar dados de transações.
* Identificar o desbalanceamento entre as classes.
* Aplicar Feature Engineering.
* Treinar diferentes modelos de classificação.
* Comparar seus desempenhos.
* Avaliar Precision, Recall, F1, ROC-AUC e PR-AUC.
* Analisar diferentes thresholds.
* Otimizar o modelo com Cross-validation e GridSearch.
* Interpretar as previsões utilizando SHAP.
* Relacionar Machine Learning com práticas de segurança.

---

## Dataset e Fonte dos Dados

O projeto utiliza o dataset público **Credit Card Fraud Detection**, disponibilizado por meio de uma fonte pública do TensorFlow.

**Arquivo:** `creditcard.csv`

**Fonte:**

```text
https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv
```

A coluna `Class` representa a variável-alvo:

| Valor | Classificação         |
| ----- | --------------------- |
| `0`   | Transação normal      |
| `1`   | Transação fraudulenta |

### Fonte remota / API

A URL utilizada não é uma API REST tradicional. Trata-se de uma **fonte remota de dados**, que disponibiliza diretamente o arquivo CSV.

A utilização dessa fonte evita manter o dataset dentro do repositório e facilita a reprodução do projeto.

---

## Tecnologias

* **Python** — linguagem principal.
* **Pandas** — manipulação e análise dos dados.
* **NumPy** — operações numéricas.
* **Matplotlib** — visualização.
* **Scikit-learn** — Machine Learning e métricas.
* **Imbalanced-learn** — tratamento do desbalanceamento.
* **XGBoost** — modelo baseado em Gradient Boosting.
* **SHAP** — explicabilidade do modelo.

---

## Metodologia

### 1. Análise e preparação

Foram verificados:

* estrutura do dataset;
* tipos de dados;
* valores ausentes;
* duplicidades;
* estatísticas descritivas;
* distribuição das classes;
* comportamento dos valores das transações.

Também foi aplicada Feature Engineering, incluindo a criação de `Amount_log`.

### 2. Divisão dos dados

Os dados foram separados em:

* **70% para treinamento**
* **30% para teste**

A divisão utiliza estratificação para preservar a proporção das classes.

O processo também evita **Data Leakage**, impedindo que informações do conjunto de teste influenciem o treinamento.

### 3. Modelos

Foram avaliados:

* Regressão Logística;
* Random Forest;
* XGBoost.

O objetivo foi comparar modelos com diferentes abordagens antes da etapa de otimização.

### 4. Desbalanceamento

Como existem muito mais transações normais que fraudulentas, foram consideradas técnicas específicas para classes desbalanceadas.

Entre elas está o **SMOTE**, que gera exemplos sintéticos da classe minoritária.

O balanceamento é aplicado somente aos dados de treinamento para preservar a independência do conjunto de teste.

### 5. Otimização

O XGBoost foi submetido a:

* Cross-validation estratificada;
* GridSearch;
* diferentes hiperparâmetros;
* avaliação utilizando PR-AUC.

---

# Avaliação do Modelo

O projeto utiliza várias métricas porque nenhuma delas, isoladamente, representa completamente o desempenho em um problema desbalanceado.

| Métrica       | O que representa                                     | Importância                                       |
| ------------- | ---------------------------------------------------- | ------------------------------------------------- |
| **Precision** | Quantas previsões positivas realmente eram positivas | Mede a quantidade de falsos alarmes               |
| **Recall**    | Quantos casos positivos existentes foram encontrados | Mede a capacidade de detectar fraudes             |
| **F1-score**  | Equilíbrio entre Precision e Recall                  | Resume as duas métricas em um único indicador     |
| **ROC-AUC**   | Capacidade geral de separar as classes               | Avalia a discriminação do modelo                  |
| **PR-AUC**    | Relação entre Precision e Recall                     | Especialmente relevante em classes desbalanceadas |

---

# Threshold

O **threshold** é o ponto de corte utilizado para transformar a probabilidade gerada pelo modelo em uma classificação.

Exemplo:

```text
Probabilidade ≥ Threshold
        ↓
Classe positiva / suspeita

Probabilidade < Threshold
        ↓
Classe negativa / normal
```

O projeto avaliou diferentes thresholds para analisar como eles alteram Precision, Recall e F1-score.

### Threshold final

```text
0.95
```

Com esse valor, o modelo considera positiva uma transação cuja probabilidade estimada de fraude seja de pelo menos **95%**.

Um threshold mais alto torna a classificação positiva mais restritiva e pode alterar o equilíbrio entre falsos positivos e falsos negativos. Por isso, sua escolha depende do contexto operacional.

---

# Resultado Final

O resultado obtido no conjunto de teste foi:

```text
ROC-AUC     : 0.9694
PR-AUC      : 0.8316
Precision   : 0.9492
Recall      : 0.7568
F1-score    : 0.8421
Threshold   : 0.95
```

### Interpretação

**ROC-AUC — 0.9694**

Indica elevada capacidade de separação entre as classes considerando diferentes thresholds.

**PR-AUC — 0.8316**

Resume o comportamento de Precision e Recall e possui especial relevância devido ao desbalanceamento das classes.

**Precision — 0.9492**

Aproximadamente **94,92%** das previsões positivas realizadas pelo modelo no threshold avaliado pertencem à classe positiva real.

**Recall — 0.7568**

Aproximadamente **75,68%** dos casos positivos existentes foram identificados pelo modelo no threshold avaliado.

**F1-score — 0.8421**

Representa o equilíbrio entre Precision e Recall, apresentando aproximadamente **84,21%** no resultado obtido.

**Threshold — 0.95**

Define o nível de probabilidade necessário para que uma transação seja classificada como positiva pelo modelo.

> Os resultados representam o desempenho no conjunto de teste utilizado no projeto e não devem ser interpretados como garantia de desempenho em um ambiente financeiro real.

---

# Matriz de Confusão

A matriz de confusão detalha os acertos e erros:

| Resultado | Significado                     |
| --------- | ------------------------------- |
| **TN**    | Normal classificada como normal |
| **FP**    | Normal classificada como fraude |
| **FN**    | Fraude classificada como normal |
| **TP**    | Fraude classificada como fraude |

Em detecção de fraude, **FN** merece atenção porque representa uma fraude que não foi identificada. Já **FP** representa um alerta incorreto sobre uma transação normal.

---

# Explicabilidade

O projeto utiliza duas abordagens complementares:

### Importância das variáveis

Mostra quais atributos tiveram maior participação nas decisões do modelo.

### SHAP

Permite analisar como as variáveis contribuíram para as previsões, ajudando a reduzir o caráter de "caixa-preta" de modelos mais complexos.

A importância de uma variável não significa que ela seja a causa da fraude; representa sua contribuição para as decisões do modelo.

---

# Segurança

O projeto considera alguns princípios importantes:

* proteção de dados financeiros;
* anonimização quando aplicável;
* controle de acesso;
* prevenção de Data Leakage;
* utilização correta do conjunto de teste;
* balanceamento somente no treinamento;
* monitoramento do modelo após implantação;
* revisão periódica do desempenho;
* utilização do modelo como apoio à análise, e não como decisão isolada.

Em um ambiente real, também seria necessário considerar requisitos regulatórios, auditoria, governança, controles de acesso e políticas de proteção de dados.

---

# Estrutura

```text
.
├── desafio_aula8.py
└── README.md
```

---

# Como Executar

### Instalar as dependências

```bash
pip install pandas numpy matplotlib scikit-learn imbalanced-learn xgboost shap
```

### Executar

O projeto pode ser executado em:

* Google Colab;
* Jupyter Notebook;
* VS Code;
* ambiente Python compatível.

É necessário possuir acesso à internet para carregar o dataset da fonte remota.

---

# Aprendizados

O projeto permitiu aplicar conceitos de:

* análise de dados com Python;
* preparação e qualidade dos dados;
* Feature Engineering;
* classificação supervisionada;
* classes desbalanceadas;
* Machine Learning;
* avaliação de modelos;
* otimização de hiperparâmetros;
* análise de Threshold;
* explicabilidade;
* segurança de dados.

O principal aprendizado foi que **avaliar um modelo não significa observar apenas uma métrica**. Em um problema de detecção de fraude, é necessário analisar diferentes indicadores e entender os impactos dos falsos positivos e falsos negativos.

---

# Conclusão

O projeto demonstrou um fluxo completo para análise e detecção de transações potencialmente fraudulentas utilizando Python e Machine Learning.

A combinação de diferentes modelos, métricas, análise de Threshold, otimização e explicabilidade permitiu avaliar o problema sob diferentes perspectivas.

Os resultados obtidos foram:

```text
ROC-AUC     : 0.9694
PR-AUC      : 0.8316
Precision   : 0.9492
Recall      : 0.7568
F1-score    : 0.8421
Threshold   : 0.95
```

A análise evidencia a importância de considerar o **desbalanceamento das classes, a escolha do threshold, a qualidade dos dados e os impactos dos erros de classificação** ao desenvolver soluções de detecção de fraude.

---
