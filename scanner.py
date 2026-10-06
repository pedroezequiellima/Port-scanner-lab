#!/usr/bin/env python3
"""
Fast TCP Port Scanner (Multithreaded)
Author: Portfolio Project
Target: Educational & Security Auditing
"""

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Common ports with standard service mapping for quick identification
SERVICE_MAP = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-Proxy",
    8443: "HTTPS-Alt"
}

def scan_port(target_ip: str, port: int, timeout: float = 0.8) -> None:
    """
    Attempts to establish a TCP connection with a target IP on a specific port.
    Uses socket.connect_ex to handle return codes cleanly without raising exceptions.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((target_ip, port))
            
            if result == 0:
                service = SERVICE_MAP.get(port, "Unknown")
                print(f"[+] Porta {port:<5} | Status: ABERTA   | Serviço: {service}")
    except socket.error:
        pass

def parse_ports(port_arg: str) -> list[int]:
    """Parses port ranges (e.g., '1-1024') or comma-separated lists (e.g., '80,443,8080')."""
    if "-" in port_arg:
        start_p, end_p = map(int, port_arg.split("-"))
        return list(range(start_p, end_p + 1))
    return [int(p.strip()) for p in port_arg.split(",")]

def main():
    parser = argparse.ArgumentParser(description="Auditoria de Portas TCP - Scanner Multithreaded")
    parser.add_argument("-t", "--target", required=True, help="Host alvo (ex.: scanme.nmap.org ou 192.168.1.1)")
    parser.add_argument("-p", "--ports", default="21,22,23,25,53,80,110,139,143,443,445,3306,3389,5432,8080", 
                        help="Portas separadas por vírgula ou intervalo (ex.: '80,443' ou '1-1024')")
    parser.add_argument("-w", "--workers", type=int, default=50, help="Número de threads simultâneas (default: 50)")
    parser.add_argument("--timeout", type=float, default=0.8, help="Timeout de conexão em segundos (default: 0.8)")

    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"[!] Erro: Não foi possível resolver o hostname '{args.target}'.")
        return

    ports = parse_ports(args.ports)

    print("=" * 60)
    print(f"[*] Alvo: {args.target} ({target_ip})")
    print(f"[*] Portas a testar: {len(ports)}")
    print(f"[*] Threads ativas: {args.workers}")
    print(f"[*] Início: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Execução concorrente usando ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        for port in ports:
            executor.submit(scan_port, target_ip, port, args.timeout)

    print("-" * 60)
    print(f"[*] Varredura finalizada em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()