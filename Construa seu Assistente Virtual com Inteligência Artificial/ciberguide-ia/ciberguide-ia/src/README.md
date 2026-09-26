# Execução da Aplicação (src/)

Este diretório contém o código da aplicação interativa do **CyberGuide AI** construída com **Streamlit** e integrada à API do **Google Gemini**.

---

## 1. Obter uma chave gratuita do Gemini

1. Acesse [Google AI Studio](https://aistudio.google.com/apikey).
2. Faça login com sua conta Google.
3. Clique em **"Create API key"** (não é necessário cartão de crédito).

---

## 2. Configurar o ambiente

Execute os comandos a partir da **raiz do projeto** (`ciberguide-ia`):

```bash
# 1. Copie o arquivo de exemplo
cp .env.example .env
```

Abra o arquivo `.env` e insira sua chave:
```env
GEMINI_API_KEY=coloque_sua_chave_aqui
GEMINI_MODEL=gemini-3.5-flash-lite
```

---

## 3. Instalar dependências

Ainda na raiz do projeto:

```bash
pip install -r requirements.txt
```

---

## 4. Iniciar o assistente

Execute a aplicação Streamlit:

```bash
streamlit run src/app.py
```

O navegador abrirá automaticamente em `http://localhost:8501`.

---

## Observações sobre a cota do modelo

O modelo padrão (`gemini-3.5-flash-lite`) dispõe de uma cota gratuita suficiente para estudos, testes e demonstrações. Se a aplicação retornar um aviso de limite de cota excedido (Erro 429), basta aguardar alguns instantes ou alterar a variável `GEMINI_MODEL` no `.env` para outro modelo disponível na sua conta.
