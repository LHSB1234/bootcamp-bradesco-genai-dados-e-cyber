# Programação e Desenvolvimento

## JavaScript

### O que é

JavaScript é uma linguagem de programação utilizada principalmente
para desenvolvimento web, tanto no navegador (front-end) quanto no
servidor, por meio do Node.js.

### Conceitos relacionados

- Variáveis (`let`, `const`)
- Tipos de dados
- Funções
- Arrays e Objetos
- Node.js

### Boas práticas

Prefira `const` e `let` em vez de `var`, mantenha funções pequenas e
com responsabilidade única, e valide sempre os dados recebidos de
fontes externas (formulários, APIs, arquivos).

---

## Funções

### O que é

Uma função é um bloco de código reutilizável, criado para executar
uma tarefa específica. Pode receber parâmetros e retornar um valor.

### Conceitos relacionados

- Parâmetros e argumentos
- Retorno de valores
- Funções anônimas e arrow functions
- Escopo (scope)

### Boas práticas

Dê nomes claros às funções, evite que uma função faça mais de uma
coisa ao mesmo tempo, e prefira funções puras (que não dependem nem
alteram estado externo) sempre que possível.

---

## Arrays

### O que é

Array é uma estrutura de dados usada para armazenar uma coleção
ordenada de valores, acessados por meio de um índice numérico.

### Conceitos relacionados

- Métodos de array (`map`, `filter`, `reduce`, `forEach`)
- Iteração
- Estruturas de dados

### Boas práticas

Prefira métodos como `map` e `filter` em vez de loops manuais quando
o objetivo é transformar ou filtrar dados — o código fica mais
legível e menos propenso a erros.

---

## Objetos

### O que é

Objeto é uma estrutura de dados que armazena informações em pares de
chave e valor, permitindo representar entidades do mundo real (como
um usuário ou um produto) de forma organizada.

### Conceitos relacionados

- Propriedades e métodos
- Desestruturação (destructuring)
- JSON

### Boas práticas

Use nomes de propriedades descritivos e evite objetos com muitos
níveis de aninhamento, pois isso dificulta a leitura e a manutenção
do código.

---

## Async/Await

### O que é

`async/await` é uma sintaxe do JavaScript que facilita o trabalho
com operações assíncronas (como chamadas a uma API), tornando o
código mais parecido com uma sequência síncrona e mais fácil de ler.

### Conceitos relacionados

- Promises
- Fetch API
- Tratamento de erros com `try/catch`

### Boas práticas

Sempre envolva chamadas `await` em blocos `try/catch` para tratar
possíveis falhas, como uma API fora do ar ou uma resposta inesperada.

---

## Fetch API

### O que é

A Fetch API é um recurso nativo do JavaScript utilizado para fazer
requisições HTTP, como buscar dados de uma API ou enviar informações
para um servidor.

### Conceitos relacionados

- APIs REST
- HTTP (GET, POST, PUT, DELETE)
- JSON
- Async/Await

### Boas práticas

Sempre trate os possíveis erros de rede e valide o status da
resposta (`response.ok`) antes de processar os dados recebidos.

---

## APIs REST

### O que é

REST é um estilo de arquitetura para construção de APIs, baseado no
uso de recursos identificados por URLs e métodos HTTP padronizados
(GET, POST, PUT, DELETE) para manipular esses recursos.

### Conceitos relacionados

- HTTP
- JSON
- Autenticação e Autorização
- Postman

### Boas práticas

Utilize nomes de recursos claros nas URLs, códigos de status HTTP
apropriados nas respostas, e documente os endpoints disponíveis.

---

## Node.js

### O que é

Node.js é um ambiente de execução que permite rodar JavaScript fora
do navegador, sendo muito utilizado para construir servidores e
APIs.

### Conceitos relacionados

- APIs REST
- Middlewares
- npm (gerenciador de pacotes)
- Banco de dados

### Boas práticas

Separe o código em módulos com responsabilidades claras (rotas,
controllers, serviços) e nunca exponha informações sensíveis
(senhas, chaves de API) diretamente no código.

---

## Middlewares

### O que é

Middleware é uma função que fica no meio do caminho entre a
requisição de uma pessoa usuária e a resposta final do servidor,
podendo validar, transformar ou bloquear a requisição antes que ela
chegue ao destino final.

### Conceitos relacionados

- Node.js
- Autenticação
- Validações
- Middlewares de segurança (Helmet, CORS, rate limiting)

### Boas práticas

Use middlewares para centralizar validações e regras de segurança
que se repetem em várias rotas, evitando duplicação de código.

---

## Validações

### O que é

Validação é o processo de verificar se os dados recebidos (de um
formulário, de uma API, de um arquivo) estão no formato e nos
critérios esperados antes de serem processados ou armazenados.

### Conceitos relacionados

- Middlewares
- Segurança de aplicações
- Prevenção de SQL Injection e XSS

### Boas práticas

Nunca confie apenas na validação feita no front-end — sempre valide
também no back-end, pois é o servidor que garante a integridade dos
dados.

---

## Autenticação JWT

### O que é

JWT (JSON Web Token) é um formato de token usado para representar,
de forma segura, informações sobre uma pessoa usuária autenticada,
permitindo que o servidor verifique sua identidade em requisições
futuras sem precisar consultar o banco de dados a cada vez.

### Conceitos relacionados

- Autenticação
- Autorização
- Criptografia
- Segurança em APIs

### Boas práticas

Defina um tempo de expiração para o token, nunca armazene
informações sensíveis dentro do JWT (ele não é criptografado, apenas
assinado) e mantenha a chave secreta fora do código-fonte.

---

## Banco de Dados

### O que é

Banco de dados é um sistema utilizado para armazenar, organizar e
consultar dados de forma estruturada e persistente.

### Conceitos relacionados

- MongoDB
- Bancos relacionais e não relacionais
- Consultas (queries)

### Boas práticas

Escolha o tipo de banco (relacional ou não relacional) de acordo com
a natureza dos dados da aplicação, e nunca armazene senhas em texto
puro — sempre utilize hash.

---

## MongoDB

### O que é

MongoDB é um banco de dados não relacional (NoSQL) que armazena
informações em documentos no formato semelhante a JSON, o que
facilita o trabalho com dados flexíveis e sem uma estrutura rígida
de tabelas.

### Conceitos relacionados

- Banco de Dados
- JSON
- Node.js

### Boas práticas

Modele as coleções de acordo com os padrões de acesso da aplicação e
sempre valide os dados antes de inseri-los, já que o MongoDB não
impõe um schema rígido por padrão.

---

## Postman

### O que é

Postman é uma ferramenta utilizada para testar APIs, permitindo
enviar requisições HTTP (GET, POST, PUT, DELETE) e visualizar as
respostas sem precisar criar uma interface própria.

### Conceitos relacionados

- APIs REST
- HTTP
- Autenticação

### Boas práticas

Organize as requisições em coleções por funcionalidade e utilize
variáveis de ambiente no Postman para não expor tokens e chaves
diretamente nas requisições.

---

## Git

### O que é

Git é um sistema de controle de versão que permite acompanhar o
histórico de alterações em um projeto, facilitando o trabalho em
equipe e a organização do código ao longo do tempo.

### Conceitos relacionados

- Repositório
- Commit
- Branch
- GitHub Actions

### Boas práticas

Escreva mensagens de commit claras e objetivas, use branches para
desenvolver novas funcionalidades separadamente, e nunca versione
arquivos com senhas ou chaves de API.

---

## Visual Studio Code

### O que é

Visual Studio Code (VS Code) é um editor de código-fonte gratuito,
amplamente utilizado para desenvolvimento web e de software em
geral, com suporte a extensões que ampliam suas funcionalidades.

### Conceitos relacionados

- Extensões (linters, formatadores, Git integration)
- Depuração (debug)
- Terminal integrado

### Boas práticas

Utilize extensões de linting e formatação automática para manter um
padrão de código consistente, e aproveite o terminal integrado para
executar comandos sem sair do editor.
