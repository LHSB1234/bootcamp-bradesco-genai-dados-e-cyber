# Segurança de Aplicações Web

## SQL Injection

### O que é

SQL Injection (SQLi) é uma vulnerabilidade que permite a uma pessoa
mal-intencionada inserir comandos SQL não previstos em campos de
entrada de uma aplicação, podendo ler, alterar ou apagar dados do
banco sem autorização.

### Conceitos relacionados

- Validações
- Banco de Dados
- Broken Access Control

### Uso educacional

Pode ser estudado em ambientes como o OWASP Juice Shop ou o DVWA,
utilizando consultas parametrizadas (prepared statements) como forma
de prevenção, sempre em ambientes próprios e autorizados.

---

## Cross-Site Scripting (XSS)

### O que é

XSS é uma vulnerabilidade que permite a injeção de scripts maliciosos
em páginas web visualizadas por outras pessoas usuárias, podendo ser
usada para roubar dados de sessão ou manipular o conteúdo exibido.

### Conceitos relacionados

- Validações
- Segurança em APIs
- Vazamento de dados

### Uso educacional

Pode ser estudado em laboratórios como o OWASP Juice Shop e o
PortSwigger Web Security Academy, praticando técnicas de sanitização
de entrada como forma de prevenção.

---

## Broken Authentication

### O que é

Broken Authentication é uma categoria de vulnerabilidade relacionada
a falhas nos mecanismos de autenticação de uma aplicação, como
senhas fracas permitidas, sessões que não expiram ou tokens mal
implementados.

### Conceitos relacionados

- Autenticação
- Autenticação JWT
- Senha fraca

### Uso educacional

Laboratórios como o DVWA costumam incluir cenários com autenticação
propositalmente falha, úteis para entender e corrigir esse tipo de
problema.

---

## Security Misconfiguration

### O que é

Security Misconfiguration ocorre quando um sistema, servidor ou
aplicação está configurado de forma insegura — como o uso de
credenciais padrão, permissões excessivas ou funcionalidades de
depuração ativas em produção.

### Conceitos relacionados

- Vazamento de dados
- Broken Access Control
- Docker

### Uso educacional

Revisar configurações padrão de servidores, containers e frameworks
em ambientes de teste ajuda a identificar más práticas antes que
cheguem à produção.

---

## Cross-Site Request Forgery (CSRF)

### O que é

CSRF é uma vulnerabilidade que engana o navegador de uma pessoa
usuária autenticada, fazendo-o enviar uma requisição não desejada a
uma aplicação na qual ela está logada, sem o seu conhecimento.

### Conceitos relacionados

- Autenticação
- Modelo cliente/servidor
- Middlewares de segurança

### Uso educacional

Pode ser estudado no PortSwigger Web Security Academy, que oferece
laboratórios específicos sobre como identificar e mitigar esse tipo
de falha, geralmente com o uso de tokens anti-CSRF.

---

## Broken Access Control

### O que é

Broken Access Control é uma falha na qual uma pessoa usuária consegue
acessar recursos ou executar ações que deveriam estar restritas ao
seu nível de permissão, por falhas na verificação de autorização.

### Conceitos relacionados

- Autorização
- Autenticação
- Segurança em APIs

### Uso educacional

É uma das categorias mais comuns no OWASP Top 10, e pode ser
praticada em laboratórios como o Juice Shop, que simula falhas desse
tipo em um e-commerce fictício.

---

## Segurança em APIs

### O que é

Segurança em APIs envolve o conjunto de práticas utilizadas para
proteger endpoints de uma API contra acessos indevidos, abuso de
requisições e exposição de dados sensíveis.

### Conceitos relacionados

- Autenticação JWT
- Rate limiting
- Validações

### Uso educacional

O Postman pode ser usado para testar, em ambientes próprios, como uma
API reage a requisições malformadas ou não autenticadas, ajudando a
identificar pontos de melhoria.

---

## JWT (em Segurança)

### O que é

No contexto de segurança, o JWT precisa ser implementado com cuidado:
um token mal configurado (sem expiração, com chave fraca ou
armazenado de forma insegura no cliente) pode se tornar uma
vulnerabilidade de autenticação.

### Conceitos relacionados

- Autenticação JWT
- Broken Authentication
- Criptografia

### Uso educacional

Analisar, em ambiente controlado, como um JWT é estruturado (header,
payload, assinatura) ajuda a entender por que ele nunca deve conter
dados sensíveis em texto legível.

---

## Rate Limiting

### O que é

Rate limiting é uma técnica que limita a quantidade de requisições
que uma pessoa usuária ou sistema pode fazer a uma API em um
determinado período, prevenindo abuso e ataques de força bruta.

### Conceitos relacionados

- Segurança em APIs
- `express-rate-limit`
- Broken Authentication

### Uso educacional

Pode ser implementado e testado em uma API própria construída com
Node.js, utilizando bibliotecas como `express-rate-limit`.

---

## Validação de Entradas (em Segurança)

### O que é

No contexto de segurança, validação de entradas é a principal linha
de defesa contra ataques como SQL Injection e XSS, garantindo que
apenas dados esperados e no formato correto sejam processados pela
aplicação.

### Conceitos relacionados

- SQL Injection
- Cross-Site Scripting (XSS)
- Validações

### Uso educacional

Praticar a validação de campos de entrada em uma aplicação própria,
testando o que acontece ao enviar dados inesperados, é uma forma
segura de entender essa defesa.

---

## Hash de Senhas

### O que é

Hash de senhas é a prática de armazenar senhas em formato de hash em
vez de texto puro, geralmente utilizando bibliotecas específicas como
o `bcrypt`, que adicionam proteções extras contra ataques.

### Conceitos relacionados

- Hashing
- `bcrypt`
- Vazamento de dados

### Uso educacional

Implementar hash de senhas com `bcrypt` em uma aplicação Node.js de
teste é uma forma prática de entender por que senhas nunca devem ser
armazenadas em texto puro.

---

## Middlewares de Segurança

### O que é

Middlewares de segurança são funções aplicadas em uma aplicação
Node.js para adicionar proteções automáticas, como cabeçalhos HTTP
seguros (Helmet), controle de origem de requisições (CORS) e limite
de requisições (rate limiting).

### Conceitos relacionados

- Helmet
- CORS
- `express-rate-limit`

### Uso educacional

Adicionar esses middlewares em uma API própria e observar como o
comportamento das requisições muda é uma boa forma de entender seu
funcionamento na prática.
