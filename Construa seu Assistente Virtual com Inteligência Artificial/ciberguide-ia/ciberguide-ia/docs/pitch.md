# Pitch do Projeto: CyberGuide AI

> Apresentação estruturada do projeto para avaliação final do Bootcamp **Bradesco - GenAI, Dados & Cybersecurity da DIO**.  
> **Tempo estimado de apresentação:** 1 a 2 minutos.

---

## 1. Problema

Quem está começando a estudar cibersegurança e desenvolvimento seguro enfrenta uma barreira comum: os conteúdos estão dispersos em dezenas de documentações, manuais densos e fóruns da internet. 

Além disso, ao tirar dúvidas com ferramentas de IA genéricas, é frequente se deparar com três problemas:
* **Alucinações técnicas:** comandos ou ferramentas inventados;
* **Falta de adaptação:** respostas com excesso de jargões para quem é iniciante;
* **Riscos de segurança:** orientações inadequadas que podem sugerir testes em ambientes não autorizados.

---

## 2. Público

O CyberGuide AI foi desenvolvido para:
* **Pessoas iniciantes e em transição de carreira** que precisam de explicações simples e analogias;
* **Estudantes de tecnologia e cibersegurança** que buscam entender o funcionamento interno de protocolos e falhas;
* **Desenvolvedores e profissionais de TI** que desejam consultar rapidamente conceitos e boas práticas defensivas.

---

## 3. Solução

O **CyberGuide AI** é um assistente virtual educacional focado em **Programação, Redes e Cibersegurança**. 

Seu papel é atuar como um tutor de estudos acessível, respondendo dúvidas técnicas com base em uma curadoria própria de informações e ajudando a pessoa usuária a decidir o próximo passo de aprendizado.

---

## 4. Como Funciona

A arquitetura do projeto prioriza a simplicidade:
1. A pessoa usuária digita sua dúvida na interface de chat;
2. A aplicação carrega os arquivos da base de conhecimento e os adiciona ao prompt de sistema da IA;
3. O modelo processa a pergunta sob regras estritas de conduta;
4. A resposta é entregue de forma direta, clara e formatada no chat.

---

## 5. Base de Conhecimento

A base de conhecimento foi organizada na pasta `data/` em **7 módulos temáticos** em formato Markdown:
1. `programacao.md` — JavaScript, Node.js, APIs REST, Git;
2. `redes.md` — IP, portas, DNS, TCP/UDP, HTTP/HTTPS;
3. `fundamentos-cyber.md` — Tríade CIA, vulnerabilidades, hashing, criptografia;
4. `seguranca-web.md` — OWASP Top 10, SQLi, XSS, CSRF, JWT;
5. `ferramentas.md` — Nmap, Wireshark, Burp Suite, Kali Linux;
6. `devsecops.md` — CI/CD, SAST, DAST, Secrets;
7. `laboratorios.md` — OWASP Juice Shop, DVWA, PortSwigger Academy.

---

## 6. Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Interface:** Streamlit (chat web leve, interativo e direto)
* **Inteligência Artificial:** Google Gemini API (`gemini-3.5-flash-lite`, tier gratuito)
* **SDK:** `google-genai` oficial
* **Configuração:** `python-dotenv` para isolamento de credenciais

---

## 7. Diferenciais

* **Aderência à base:** O agente prioriza o conteúdo curado em vez de tentar adivinhar;
* **Controle de alucinação:** Diz claramente "não sei" ou "não está na base" quando a informação não estiver disponível;
* **Adaptação didática:** Ajusta o vocabulário conforme o nível percebido na pergunta;
* **Simplicidade de código:** Todo o protótipo é transparente, fácil de ler, manter e executar localmente.

---

## 8. Segurança e Ética

O CyberGuide AI tem finalidade **estritamente defensiva e educacional (Blue Team)**:
* Não fornece comandos ou instruções para invadir sistemas de terceiros;
* Sempre que uma ferramenta ou técnica de teste é abordada (como Nmap ou SQL Injection), o assistente reforça que a prática deve ocorrer **exclusivamente em laboratórios próprios e autorizados**.

---

## 9. Avaliação

O projeto conta com uma matriz de avaliação prática de **20 casos de teste** em `docs/avaliacao-metricas.md`, avaliando critérios de correção técnica, aderência à base, controle de alucinação, segurança e recusa educada de perguntas fora de escopo.

---

## 10. Próximos Passos

Como evolução natural do protótipo:
* Expandir a base de conhecimento com tópicos de segurança em nuvem (Cloud Security);
* Adicionar sugestões de exercícios rápidos no chat após as explicações;
* Conectar referências diretas para cursos e materiais complementares da plataforma DIO.

---

## 🎙️ Roteiro Sugerido para Apresentação Oral (1 a 2 minutos)

> *"Olá! Meu nome é [Seu Nome] e este é o **CyberGuide AI**, meu projeto final do Bootcamp Bradesco - GenAI, Dados & Cybersecurity na DIO.*
> 
> *Aprender cibersegurança hoje pode ser desafiador pela quantidade de jargões técnicos dispersos. E ao usar IAs genéricas para estudar, é comum esbarrar em alucinações técnicas ou explicações difíceis demais.*
> 
> *Para resolver isso, criei o CyberGuide AI: um assistente virtual em Python e Streamlit integrado à API do Google Gemini. Ele utiliza uma base de conhecimento própria com 7 módulos práticos — cobrindo desde lógica e redes até OWASP e DevSecOps.*
> 
> *O grande valor do CyberGuide está nas suas regras de comportamento: ele prioriza a base curada, adapta a didática para iniciantes ou profissionais, assume quando não possui uma informação e é estritamente defensivo — orientando sempre a prática em laboratórios controlados como o Juice Shop.*
> 
> *O projeto cumpre todos os passos do desafio DIO: documentação, base, prompts, aplicação funcional, matriz de 20 testes e este pitch. É um protótipo simples, funcional e pronto para evoluir. Muito obrigado!"*
