# Redes

## Endereço IP

### O que é

Um endereço IP é um identificador numérico atribuído a cada
dispositivo conectado a uma rede, utilizado para localizar e se
comunicar com esse dispositivo.

### Conceitos relacionados

- Modelo cliente/servidor
- DNS
- Portas

### Observações

Existem IPs públicos (usados na internet) e privados (usados dentro
de redes locais). Conhecer o IP de um dispositivo é o primeiro passo
para entender como ele se comunica com outros na rede.

---

## Portas

### O que é

Porta é um número que identifica, dentro de um mesmo endereço IP,
qual serviço ou aplicação deve receber uma comunicação específica
(por exemplo, a porta 80 costuma ser usada para HTTP).

### Conceitos relacionados

- Endereço IP
- TCP e UDP
- Nmap (port scanning)

### Observações

Cada serviço de rede "escuta" em uma porta específica. Entender
portas é essencial para compreender como ferramentas como o Nmap
identificam serviços ativos em um host.

---

## DNS

### O que é

DNS (Domain Name System) é o sistema responsável por traduzir nomes
de domínio (como `exemplo.com`) em endereços IP, permitindo que as
pessoas usem nomes em vez de números para acessar sites e serviços.

### Conceitos relacionados

- Endereço IP
- Modelo cliente/servidor
- HTTP/HTTPS

### Observações

O DNS funciona como uma espécie de "agenda de contatos" da internet.
Problemas de DNS são uma causa comum de sites parecerem "fora do ar"
mesmo quando o servidor está funcionando normalmente.

---

## TCP

### O que é

TCP (Transmission Control Protocol) é um protocolo de comunicação
que garante a entrega confiável e ordenada dos dados entre dois
dispositivos, sendo utilizado por serviços que exigem confiabilidade,
como o HTTP.

### Conceitos relacionados

- UDP
- Portas
- Modelo cliente/servidor

### Observações

O TCP é mais lento que o UDP por causa das verificações de entrega,
mas garante que os dados cheguem completos e na ordem correta — por
isso é usado em navegação web, e-mail e transferência de arquivos.

---

## UDP

### O que é

UDP (User Datagram Protocol) é um protocolo de comunicação mais
rápido que o TCP, porém sem garantia de entrega ou ordem dos dados,
sendo usado em aplicações que priorizam velocidade, como streaming e
jogos online.

### Conceitos relacionados

- TCP
- Portas

### Observações

A escolha entre TCP e UDP depende da necessidade da aplicação:
confiabilidade (TCP) ou velocidade (UDP).

---

## HTTP

### O que é

HTTP (Hypertext Transfer Protocol) é o protocolo utilizado para a
comunicação entre clientes (como navegadores) e servidores na web,
definindo como as requisições e respostas devem ser estruturadas.

### Conceitos relacionados

- HTTPS
- Requests e Responses
- APIs REST
- Modelo cliente/servidor

### Observações

O HTTP, por padrão, transmite dados sem criptografia, o que o torna
vulnerável à interceptação — por isso o uso do HTTPS é recomendado
sempre que houver dados sensíveis envolvidos.

---

## HTTPS

### O que é

HTTPS é a versão segura do HTTP, que utiliza criptografia (TLS/SSL)
para proteger os dados transmitidos entre cliente e servidor contra
interceptação e adulteração.

### Conceitos relacionados

- HTTP
- Criptografia
- Autenticação

### Observações

O "S" de HTTPS significa "Secure". Sites que lidam com login, dados
pessoais ou pagamentos devem sempre utilizar HTTPS.

---

## Modelo Cliente/Servidor

### O que é

O modelo cliente/servidor é uma forma de organizar a comunicação em
rede na qual o cliente (por exemplo, um navegador) solicita
informações ou serviços, e o servidor responde a essas solicitações.

### Conceitos relacionados

- HTTP/HTTPS
- Requests e Responses
- APIs REST

### Observações

Esse modelo é a base do funcionamento da maioria das aplicações web:
o front-end atua como cliente e o back-end como servidor.

---

## Requests e Responses

### O que é

Request (requisição) é a solicitação enviada por um cliente a um
servidor; response (resposta) é o retorno enviado pelo servidor com
o resultado dessa solicitação, incluindo um código de status HTTP.

### Conceitos relacionados

- HTTP
- APIs REST
- Postman

### Observações

Entender os principais códigos de status (como 200 para sucesso, 404
para não encontrado e 500 para erro no servidor) ajuda a interpretar
rapidamente o que aconteceu em uma comunicação HTTP.
