# DevSecOps

## DevSecOps

### O que é

DevSecOps é uma abordagem que integra práticas de segurança em todas
as etapas do desenvolvimento de software, desde o planejamento até a
entrega, em vez de tratar a segurança apenas como uma etapa final.

### Conceitos relacionados

- CI/CD
- SAST e DAST
- Secrets

### Boas práticas

Trate a segurança como responsabilidade de toda a equipe, e não
apenas de um time específico, incorporando verificações automáticas
desde o início do desenvolvimento.

---

## CI/CD

### O que é

CI/CD (Integração Contínua e Entrega/Implantação Contínua) é um
conjunto de práticas que automatiza a construção, o teste e a
implantação de uma aplicação sempre que uma alteração é enviada ao
repositório.

### Conceitos relacionados

- GitHub Actions
- DevSecOps
- Git

### Boas práticas

Inclua verificações de segurança (como SAST) como parte do pipeline
de CI/CD, garantindo que problemas sejam identificados antes de
chegar à produção.

---

## SAST

### O que é

SAST (Static Application Security Testing) é uma técnica que analisa
o código-fonte de uma aplicação, sem executá-la, em busca de padrões
que possam indicar vulnerabilidades de segurança.

### Conceitos relacionados

- CI/CD
- DevSecOps
- Vulnerabilidade

### Boas práticas

Execute ferramentas de SAST automaticamente no pipeline de CI/CD,
para que problemas no código sejam identificados o quanto antes,
ainda durante o desenvolvimento.

---

## DAST

### O que é

DAST (Dynamic Application Security Testing) é uma técnica que testa
uma aplicação já em execução, simulando ataques reais para identificar
vulnerabilidades que só aparecem em tempo de execução.

### Conceitos relacionados

- OWASP ZAP
- CI/CD
- DevSecOps

### Boas práticas

Combine SAST e DAST: o SAST identifica problemas no código-fonte,
enquanto o DAST identifica problemas que só se manifestam com a
aplicação rodando, oferecendo uma cobertura mais completa.

---

## Secrets

### O que é

Secrets são informações sensíveis (como senhas, chaves de API e
tokens) que uma aplicação precisa para funcionar, mas que nunca devem
ser expostas publicamente, especialmente em repositórios de código.

### Conceitos relacionados

- Variáveis de ambiente
- `dotenv`
- GitHub Actions

### Boas práticas

Nunca versione secrets diretamente no código — utilize variáveis de
ambiente e, em pipelines de CI/CD, recursos específicos de
armazenamento seguro de secrets oferecidos pela plataforma.

---

## Variáveis de Ambiente

### O que é

Variáveis de ambiente são valores configuráveis fora do código-fonte
de uma aplicação, utilizados para armazenar informações que variam
entre ambientes (desenvolvimento, teste, produção) ou que são
sensíveis, como secrets.

### Conceitos relacionados

- Secrets
- `dotenv`
- Docker

### Boas práticas

Utilize um arquivo `.env` para desenvolvimento local e sempre o
inclua no `.gitignore`, evitando que credenciais sejam enviadas
acidentalmente ao repositório.

---

## GitHub Actions

### O que é

GitHub Actions é uma ferramenta de automação integrada ao GitHub,
utilizada para criar pipelines de CI/CD que executam tarefas
automaticamente, como testes, builds e verificações de segurança, a
cada alteração no repositório.

### Conceitos relacionados

- CI/CD
- Git
- SAST

### Boas práticas

Configure workflows para rodar testes e verificações de segurança
automaticamente em cada pull request, evitando que código com
problemas seja integrado ao projeto principal.
