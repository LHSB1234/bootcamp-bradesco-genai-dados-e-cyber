# 🛡️ CyberGuide AI

> Projeto desenvolvido como trabalho final do Bootcamp **Bradesco - GenAI, Dados & Cybersecurity** da [Digital Innovation One (DIO)](https://dio.me), no desafio **"Construa seu Assistente Virtual com Inteligência Artificial"**.

---

## 📌 Sobre o Projeto

O **CyberGuide AI** é um assistente virtual educacional voltado para **Programação, Redes e Cibersegurança**. 

Seu objetivo é ajudar as pessoas usuárias a esclarecer dúvidas técnicas e compreender conceitos essenciais de segurança da informação, respondendo estritamente com base em uma base de conhecimento curada, evitando alucinações técnicas e promovendo uma conduta defensiva e ética.

Esta é a versão **simples, direta e funcional** do projeto: uma aplicação em Python com interface interativa em Streamlit, integrada à API do Google Gemini (`gemini-3.5-flash-lite`, tier gratuito) e utilizando arquivos Markdown como contexto direto.

### 👥 Público-Alvo
* **Pessoas Iniciantes:** Que precisam de explicações acessíveis, analogias do cotidiano e conceitos fundamentais sem jargões desnecessários;
* **Estudantes de Tecnologia:** Que desejam compreender o funcionamento interno de protocolos, arquiteturas e falhas de segurança;
* **Profissionais e Desenvolvedores:** Que buscam consultas rápidas sobre boas práticas defensivas, padrões OWASP e DevSecOps.

---

## 🧭 Os 6 Passos do Desafio DIO

O projeto foi estruturado para cumprir com rigor todas as etapas do desafio proposto:

| Passo | Descrição | Localização |
| :---: | :--- | :--- |
| **1** | **Documentação** | [`docs/documentacao-agente.md`](docs/documentacao-agente.md) — Objetivos, persona e limites do agente |
| **2** | **Base de conhecimento** | [`data/`](data/) — 7 módulos curados em Markdown |
| **3** | **Prompts do agente** | [`docs/prompts.md`](docs/prompts.md) — Engenharia de prompts e regras de conduta |
| **4** | **Aplicação funcional** | [`src/app.py`](src/app.py) — Interface interativa Streamlit com Google Gemini |
| **5** | **Avaliação e métricas** | [`docs/avaliacao-metricas.md`](docs/avaliacao-metricas.md) — Matriz de 20 casos de teste práticos |
| **6** | **Pitch** | [`docs/pitch.md`](docs/pitch.md) — Apresentação executiva e roteiro oral de 1 a 2 min |

---

## 🎯 Problema e Solução

* **O Problema:** Os conteúdos de cibersegurança e programação estão dispersos em documentações extensas e com excesso de termos técnicos. Além disso, assistentes de IA genéricos frequentemente alucinam comandos inexistentes, geram respostas desconectadas da realidade do estudante ou fornecem instruções que podem ser utilizadas indevidamente fora de ambientes de teste.
* **A Solução:** Um tutor virtual especializado que responde a partir de uma base curada, ajusta a profundidade pedagógica ao perfil do estudante, assume quando não possui uma informação e redireciona qualquer prática técnica exclusivamente para laboratórios controlados.

---

## 🏗️ Arquitetura da Solução

O CyberGuide AI optou por uma arquitetura em memória, simples e robusta, evitando sistemas de banco vetorial ou pipelines RAG desnecessários para a escala atual do projeto:

```text
[Usuário no Chat] 
       │ (pergunta + histórico recente)
       ▼
[Streamlit - src/app.py]
       │
       ├─► [Lê módulos data/*.md via Pathlib] ──► [Monta SYSTEM_PROMPT com base curada]
       │
       ▼ (system_instruction + histórico recente + pergunta)
[Google Gemini API (gemini-3.5-flash-lite)]
       │
       ▼ (resposta direta, contextualizada e formatada)
[Exibição na Interface do Chat]
```

Para detalhes aprofundados sobre as decisões arquiteturais e fluxo de dados, consulte [`docs/arquitetura.md`](docs/arquitetura.md).

---

## 📚 Base de Conhecimento (`data/`)

A base de conhecimento foi estruturada em 7 módulos objetivos na pasta `data/`:

* [`programacao.md`](data/programacao.md) — JavaScript, Node.js, APIs REST, Git, MongoDB, Postman;
* [`redes.md`](data/redes.md) — Endereços IP, Portas, DNS, TCP/UDP, HTTP/HTTPS, Modelo Cliente/Servidor;
* [`fundamentos-cyber.md`](data/fundamentos-cyber.md) — Tríade CIA, vulnerabilidades, hashing, criptografia, senhas, pentest;
* [`seguranca-web.md`](data/seguranca-web.md) — OWASP Top 10 (SQLi, XSS, CSRF), JWT, Rate Limiting, sanitização;
* [`ferramentas.md`](data/ferramentas.md) — Nmap, Wireshark, Burp Suite, Kali Linux, Docker, WSL;
* [`devsecops.md`](data/devsecops.md) — CI/CD, SAST, DAST, Secrets, GitHub Actions;
* [`laboratorios.md`](data/laboratorios.md) — Ambientes seguros de treino: OWASP Juice Shop, DVWA, PortSwigger Academy.

---

## 🤖 Comportamento e Diretrizes do Agente

O CyberGuide AI opera sob instruções de sistema (`system_instruction`) rigorosas:

1. **Aderência Prioritária:** Responde prioritariamente com base nas definições dos módulos da pasta `data/`;
2. **Controle de Alucinação:** Se a informação solicitada não constar na base ou envolver fatos em tempo real, o assistente declara expressamente que não possui a informação, evitando suposições;
3. **Postura Estritamente Defensiva:** Não fornece instruções para atacar ou invadir sistemas reais de terceiros. Sempre que comandos ou ferramentas (como Nmap ou Burp Suite) são abordados, direciona o estudo para laboratórios controlados;
4. **Filtro de Escopo:** Perguntas que fogem de programação, redes e cibersegurança são recusadas de maneira educada;
5. **Adaptação de Linguagem:** Ajusta o tom e o vocabulário para iniciantes (analogias), estudantes (mecanismos internos) ou profissionais (nuances e trade-offs).

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Interface Web:** [Streamlit](https://streamlit.io/)
* **Inteligência Artificial:** [Google Gemini API](https://ai.google.dev/) (`gemini-3.5-flash-lite`, tier gratuito)
* **SDK Oficial:** `google-genai`
* **Gerenciamento de Ambiente:** `python-dotenv`

---

## 🚀 Como Executar Localmente

### 1. Clonar o repositório e acessar a pasta
```bash
git clone <url-do-seu-repositorio>
cd ciberguide-ia
```

### 2. Configurar a chave de API
Crie o arquivo `.env` a partir do modelo `.env.example`:
```bash
cp .env.example .env
```
Edite o arquivo `.env` e insira sua chave gratuita obtida no [Google AI Studio](https://aistudio.google.com/apikey):
```env
GEMINI_API_KEY=coloque_sua_chave_aqui
GEMINI_MODEL=gemini-3.5-flash-lite
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Executar o assistente
```bash
streamlit run src/app.py
```
A interface será aberta automaticamente no navegador em `http://localhost:8501`.

---

## 🧪 Avaliação e Validação

A qualidade e a segurança do assistente são avaliadas por meio de uma metodologia estruturada com **20 casos de teste práticos** descrita em [`docs/avaliacao-metricas.md`](docs/avaliacao-metricas.md).

A matriz de testes cobre:
* **Cobertura da base:** validação dos 7 módulos temáticos;
* **Comportamento e transparência:** respostas claras, tratamento de dúvidas parciais, fora da base e fora de escopo;
* **Segurança e ética:** recusa a ataques a alvos reais e orientação de laboratórios autorizados;
* **Adaptação didática:** respostas calibradas para perfis iniciante, estudante e avançado.

---

## ⚠️ Limitações do Protótipo

* **Dependência da base local:** As respostas dependem do escopo dos arquivos em `data/*.md`. Tópicos não contemplados resultarão em aviso de ausência de informação;
* **Sem dados em tempo real:** O agente não pesquisa na web nem acompanha CVEs ou notícias publicadas no dia;
* **Caráter educacional:** As respostas não substituem consultorias formais de segurança da informação, auditorias profissionais ou documentações oficiais de ferramentas.
