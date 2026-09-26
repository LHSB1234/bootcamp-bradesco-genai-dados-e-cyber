# Fundamentos de Cibersegurança

## Tríade CIA

### O que é

A Tríade CIA é um modelo fundamental de segurança da informação,
formado por três pilares: Confidencialidade (garantir que apenas
pessoas autorizadas acessem a informação), Integridade (garantir que
a informação não seja alterada indevidamente) e Disponibilidade
(garantir que a informação esteja acessível quando necessário).

### Conceitos relacionados

- Vulnerabilidade
- Criptografia
- Autenticação e Autorização

### Observações

Praticamente toda decisão de segurança pode ser analisada sob a
ótica de qual pilar da Tríade CIA ela protege.

---

## Vulnerabilidade

### O que é

Uma vulnerabilidade é uma fraqueza em um sistema, aplicação,
configuração ou processo que pode ser explorada para comprometer sua
segurança.

### Conceitos relacionados

- Exploit
- Ataque
- Payload

### Observações

Nem toda vulnerabilidade é explorada — algumas permanecem sem impacto
real até que alguém desenvolva ou utilize um exploit para tirar
proveito dela.

---

## Ataque

### O que é

Um ataque é uma ação deliberada que tenta explorar uma vulnerabilidade
para comprometer a confidencialidade, integridade ou disponibilidade
de um sistema.

### Conceitos relacionados

- Vulnerabilidade
- Exploit
- Payload

### Observações

Ataques podem ter diferentes objetivos: roubo de dados, interrupção
de serviço, acesso não autorizado, entre outros.

---

## Exploit

### O que é

Exploit é um código, técnica ou ferramenta criada especificamente
para tirar proveito de uma vulnerabilidade conhecida em um sistema
ou aplicação.

### Conceitos relacionados

- Vulnerabilidade
- Payload
- Ataque

### Observações

O estudo de exploits em ambientes controlados e autorizados ajuda a
entender como as vulnerabilidades funcionam na prática — e, com
isso, como se defender delas.

---

## Payload

### O que é

Payload é a parte de um exploit ou ataque responsável por executar a
ação desejada após a vulnerabilidade ser explorada, como abrir um
acesso remoto ou extrair dados.

### Conceitos relacionados

- Exploit
- Vulnerabilidade
- Ataque

### Observações

Em contextos educacionais, o payload costuma ser algo simples e
inofensivo (como exibir uma mensagem), usado apenas para demonstrar
que a exploração funcionou.

---

## Hashing

### O que é

Hashing é o processo de transformar uma informação (como uma senha)
em uma sequência de caracteres de tamanho fixo, chamada hash, de
forma que não seja possível reverter esse processo para obter a
informação original.

### Conceitos relacionados

- Criptografia
- Autenticação
- `bcrypt`

### Observações

Diferente da criptografia, o hashing não é reversível — por isso é
amplamente utilizado para armazenar senhas com segurança: o sistema
compara o hash da senha digitada com o hash armazenado, sem nunca
guardar a senha original.

---

## Criptografia

### O que é

Criptografia é a técnica utilizada para transformar uma informação
em um formato ilegível para quem não possui a chave correta,
protegendo os dados contra acesso não autorizado.

### Conceitos relacionados

- HTTPS
- Hashing
- Autenticação JWT

### Observações

Existem dois tipos principais: criptografia simétrica (mesma chave
para criptografar e descriptografar) e assimétrica (par de chaves
pública e privada).

---

## Autenticação

### O que é

Autenticação é o processo de verificar a identidade de uma pessoa
usuária, geralmente por meio de credenciais como usuário e senha,
confirmando que ela é quem diz ser.

### Conceitos relacionados

- Autorização
- Autenticação JWT
- Senha fraca

### Observações

Autenticação responde à pergunta "quem é você?", enquanto autorização
responde à pergunta "o que você pode fazer?" — são conceitos
relacionados, mas distintos.

---

## Autorização

### O que é

Autorização é o processo que determina quais recursos ou ações uma
pessoa usuária, já autenticada, tem permissão para acessar ou
executar.

### Conceitos relacionados

- Autenticação
- Broken Access Control

### Observações

Uma falha comum em aplicações é confundir autenticação com
autorização, permitindo que uma pessoa autenticada acesse recursos
que não deveriam estar disponíveis para o seu nível de permissão.

---

## Senha Fraca

### O que é

Senha fraca é uma credencial de acesso fácil de adivinhar ou
quebrar, seja por ser muito curta, previsível (como "123456") ou
reutilizada em vários serviços.

### Conceitos relacionados

- Autenticação
- Hashing
- Vazamento de dados

### Observações

O uso de senhas fortes, únicas para cada serviço, combinado com
autenticação em duas etapas, reduz significativamente o risco de
acesso não autorizado.

---

## Vazamento de Dados

### O que é

Vazamento de dados (data breach) é a exposição não autorizada de
informações sensíveis, que pode ocorrer por falhas de segurança,
configurações incorretas ou ataques bem-sucedidos.

### Conceitos relacionados

- Vulnerabilidade
- Criptografia
- Security Misconfiguration

### Observações

Após um vazamento, é uma boa prática trocar imediatamente as senhas
afetadas e verificar se as mesmas credenciais foram reutilizadas em
outros serviços.

---

## Pentest / Teste de Penetração

### O que é

Teste de segurança autorizado e controlado, realizado para identificar
e avaliar vulnerabilidades em sistemas, redes ou aplicações antes que
sejam exploradas por agentes maliciosos.

### Conceitos relacionados

- Vulnerabilidade
- Exploit
- Laboratórios de segurança

### Boas práticas

- Possuir sempre autorização formal prévia e explícita por escrito;
- Definir escopo, alvos e horários de teste com clareza;
- Utilizar ambientes controlados para estudos (OWASP Juice Shop, DVWA, PortSwigger Web Security Academy);
- Registrar evidências e resultados de forma responsável;
- Priorizar a comunicação ágil para a correção e mitigação das falhas identificadas.