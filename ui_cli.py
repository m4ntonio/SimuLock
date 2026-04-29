import uuid
import time
import sys

# cores ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
RESET = "\033[0m"

def typewriter(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def mostrar_ransom_cli(verificar_chave):
    victim_id = str(uuid.uuid4())[:8]

    print("\n" + "="*60)

    typewriter(f"{RED}☣[SimuLock v1.0]☣︎{RESET}", 0.03)
    typewriter(f"{RED}SEUS ARQUIVOS FORAM CRIPTOGRAFADOS{RESET}", 0.02)

    print("="*60)

    print(f"{WHITE}ID DA VÍTIMA:{RESET} {YELLOW}{victim_id}{RESET}")
    print(f"{WHITE}STATUS:{RESET} {RED}ACESSO BLOQUEADO{RESET}")
    print(f"{WHITE}RESGATE:{RESET} {YELLOW}0.5 BTC (SIMULADO){RESET}")

    print("-"*60)

    typewriter(f"{YELLOW}Você tem tempo limitado para recuperar seus arquivos.{RESET}", 0.01)
    typewriter(f"{RED}Após o prazo, a perda será permanente.{RESET}", 0.01)

    print("-"*60)

    try:
        user_key = input(f"\n{WHITE}Digite a chave para recuperar: {RESET}")

        if verificar_chave(user_key.strip()):
            print(f"\n{GREEN}[✓] Arquivos recuperados com sucesso!{RESET}\n")
        else:
            print(f"\n{RED}[!] Chave incorreta!{RESET}\n")

    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Execução cancelada pelo usuário.{RESET}")
        exit(0)