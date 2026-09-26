# Ferramentas

## Kali Linux

### O que é

Kali Linux é uma distribuição Linux voltada para testes de segurança,
que vem com diversas ferramentas de análise, varredura e testes de
penetração já pré-instaladas.

### Conceitos relacionados

- Nmap
- Wireshark
- Burp Suite Community

### Uso educacional

Pode ser utilizado em uma máquina virtual própria (com VirtualBox ou
VMware) para estudar e praticar ferramentas de segurança em um
ambiente isolado e controlado.

---

## Nmap

### O que é

Nmap é uma ferramenta utilizada para descoberta de hosts,
portas e serviços em uma rede.

### Conceitos relacionados

- Port scanning
- Descoberta de serviços
- Enumeração
- TCP
- UDP

### Uso educacional

Pode ser utilizado em máquinas próprias, laboratórios
e ambientes autorizados para compreender como serviços
de rede podem ser identificados.

---

## Wireshark

### O que é

Wireshark é uma ferramenta utilizada para capturar e analisar
tráfego de rede, permitindo observar protocolos, pacotes e
informações presentes nas comunicações.

### Conceitos relacionados

- TCP e UDP
- HTTP/HTTPS
- Modelo cliente/servidor

### Uso educacional

Pode ser utilizado em uma rede própria ou máquina virtual para
observar, por exemplo, como uma requisição HTTP trafega sem
criptografia — reforçando a importância do HTTPS.

---

## Burp Suite Community

### O que é

Burp Suite Community é uma ferramenta utilizada para testes de
segurança em aplicações web, permitindo interceptar, analisar e
modificar requisições HTTP entre o navegador e o servidor.

### Conceitos relacionados

- SQL Injection
- Cross-Site Scripting (XSS)
- Requests e Responses

### Uso educacional

Pode ser utilizada junto a laboratórios como o OWASP Juice Shop e o
PortSwigger Web Security Academy para praticar a identificação de
vulnerabilidades em aplicações de teste.

---

## OWASP ZAP

### O que é

OWASP ZAP (Zed Attack Proxy) é uma ferramenta gratuita e de código
aberto utilizada para encontrar vulnerabilidades em aplicações web,
por meio de varreduras automáticas e testes manuais.

### Conceitos relacionados

- OWASP
- Segurança em APIs
- Security Misconfiguration

### Uso educacional

Pode ser utilizado para realizar varreduras em aplicações próprias
ou em ambientes de laboratório, como o OWASP Juice Shop, para
identificar possíveis pontos de melhoria.

---

## Postman

### O que é

Postman é uma ferramenta utilizada para testar APIs, permitindo
enviar requisições HTTP e visualizar respostas, cabeçalhos e códigos
de status de forma prática.

### Conceitos relacionados

- APIs REST
- HTTP
- Segurança em APIs

### Uso educacional

Útil para testar, em uma API própria, como o sistema reage a
requisições sem autenticação ou com dados inválidos — ajudando a
identificar falhas antes de irem para produção.

---

## Docker

### O que é

Docker é uma ferramenta que permite empacotar uma aplicação e suas
dependências em containers, garantindo que ela funcione da mesma
forma em diferentes ambientes.

### Conceitos relacionados

- DevSecOps
- CI/CD
- Variáveis de ambiente

### Uso educacional

Pode ser utilizado para subir, em ambiente local, laboratórios como o
OWASP Juice Shop e o DVWA de forma rápida e isolada, sem afetar o
restante do sistema.

---

## VirtualBox

### O que é

VirtualBox é um software de virtualização que permite criar e
executar máquinas virtuais, possibilitando rodar outro sistema
operacional (como o Kali Linux) dentro do computador principal, de
forma isolada.

### Conceitos relacionados

- Kali Linux
- VMware
- Laboratórios de segurança

### Uso educacional

Permite montar um ambiente de estudos seguro e isolado, no qual é
possível praticar testes de segurança sem colocar o sistema principal
em risco.

---

## VMware

### O que é

VMware é outra ferramenta de virtualização, semelhante ao VirtualBox,
utilizada para criar e gerenciar máquinas virtuais em diferentes
sistemas operacionais.

### Conceitos relacionados

- VirtualBox
- Kali Linux
- Laboratórios de segurança

### Uso educacional

Assim como o VirtualBox, pode ser usada para isolar ambientes de
teste e prática de segurança, mantendo o sistema principal protegido.

---

## WSL

### O que é

WSL (Windows Subsystem for Linux) é um recurso do Windows que permite
executar um ambiente Linux diretamente no sistema operacional
Windows, sem a necessidade de uma máquina virtual completa.

### Conceitos relacionados

- Kali Linux
- Docker
- Git

### Uso educacional

Facilita o uso de ferramentas de linha de comando e de segurança
originalmente feitas para Linux em um computador com Windows,
simplificando o ambiente de estudos.
