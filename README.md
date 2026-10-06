# 🔍 Fast TCP Port Scanner (Python Multithreading)

Ferramenta CLI desenvolvida em Python para auditoria de rede e reconhecimento inicial (*reconnaissance*), focada em performance através de conexões simultâneas via sockets brutos e threads.

---

## 📌 Funcionalidades

- **Varredura Concorrente:** Implementação com `concurrent.futures.ThreadPoolExecutor` para acelerar a checagem de portas sem gargalos de I/O síncrono.
- **Low-level Sockets:** Uso direto da biblioteca nativa `socket` com método `connect_ex()`, evitando overhead de exceções e medindo com precisão o *Three-Way Handshake* TCP.
- **Identificação de Serviços:** Mapeamento automático de serviços conhecidos em portas padrão (HTTP, SSH, SMB, MySQL, etc.).
- **Parâmetros Customizáveis:** Suporte a intervalos de portas (`1-1024`), listas pontuais (`80,443`), número de workers e controle fino de timeout.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Ambiente:** Ubuntu 24.04 LTS
- **Bibliotecas:** `socket`, `argparse`, `concurrent.futures`, `datetime` (Zero dependências externas — usa apenas a biblioteca padrão do Python).

---

## 🚀 Como Executar

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/tcp-port-scanner.git
cd tcp-port-scanner
```

### 2. Criar e ativar o ambiente virtual (Ubuntu 24.04)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Execução

Exemplo 1: Escanear portas comuns no alvo padrão de testes:
```bash
python3 scanner.py -t scanme.nmap.org
```

Exemplo 2: Escanear um range de portas com 100 threads:
```bash
python3 scanner.py -t 192.168.1.1 -p 1-1024 -w 100 --timeout 0.5
```

---

## 📊 Exemplo de Saída

```text
============================================================
[*] Alvo: scanme.nmap.org (45.33.32.156)
[*] Portas a testar: 15
[*] Threads ativas: 50
[*] Início: 2026-10-06 10:45:00
============================================================
[+] Porta 22    | Status: ABERTA   | Serviço: SSH
[+] Porta 80    | Status: ABERTA   | Serviço: HTTP
------------------------------------------------------------
[*] Varredura finalizada em: 2026-10-06 10:45:01
```

---

## ⚠️ Aviso Legal (Disclaimer)

*Este projeto foi desenvolvido exclusivamente para propósitos educacionais e testes em ambientes autorizados. Realizar varreduras de portas em hosts sem autorização prévia pode violar leis locais e termos de serviço.*