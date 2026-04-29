import tkinter as tk
import uuid

def mostrar_ransom_gui(on_submit):
    root = tk.Tk()
    root.title("SYSTEM LOCKED")
    root.configure(bg="black")
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.focus_force()

    victim_id = str(uuid.uuid4())[:8]

    frame = tk.Frame(root, bg="black")
    frame.pack(expand=True, pady=20)

    titulo_app = tk.Label(
        frame,
        text="☣[SimuLock v1.0]☣︎",
        fg="white",
        bg="black",
        font=("Courier", 22, "bold"),
    )

    titulo_msg = tk.Label(
        frame,
        text="⚠︎ SEUS ARQUIVOS FORAM CRIPTOGRAFADOS ⚠︎",
        fg="red",
        bg="black",
        font=("Courier", 22, "bold")
    )

    titulo_app.pack(pady=(10, 0))
    titulo_msg.pack(pady=(0, 20))

    info = tk.Label(
        frame,
        text=f"ID DA VÍTIMA: {victim_id}\n\n"
             "Todos os seus arquivos foram bloqueados.\n"
             "Envie 0.5 BTC (SIMULADO)\n\n"
             "Tempo restante para perda permanente:",
        fg="white",
        bg="black",
        font=("Courier", 14), 
    )
    info.pack(pady=10)

    # TIMER
    tempo_label = tk.Label(
        frame,
        text="24:00:00",
        fg="red",
        bg="black",
        font=("Courier", 32, "bold")
    )
    tempo_label.pack(pady=10)

    tempo_restante = 24 * 60 * 60  # 24 horas em segundos

    def atualizar_timer():
        nonlocal tempo_restante

        horas = tempo_restante // 3600
        minutos = (tempo_restante % 3600) // 60
        segundos = tempo_restante % 60

        tempo_label.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")

        if tempo_restante > 0:
            tempo_restante -= 1
            root.after(1000, atualizar_timer)
        else:
            tempo_label.config(text="TEMPO ESGOTADO", fg="darkred")

    atualizar_timer()

    entry = tk.Entry(
        frame,
        font=("Courier", 16),
        width=30,
        justify="center",
        show="*"
    )
    entry.pack(pady=10)
    root.after(100, lambda: entry.focus_set())

    result_label = tk.Label(
        frame,
        text="",
        fg="green",
        bg="black",
        font=("Courier", 12)
    )
    result_label.pack(pady=10)
    entry.focus()

    def toggle_password():
        if entry.cget("show") == "":
            entry.config(show="*")
        else:
            entry.config(show="")

    btn_toggle = tk.Button(
        frame,
        text="MOSTRAR/OCULTAR CHAVE",
        command=toggle_password,
        bg="black",
        fg="white"
    )
    btn_toggle.pack(pady=5)

    def submit():
        if botao["state"] == "disabled":
            return

        botao.config(state="disabled")
        key = entry.get().strip()
        ok = on_submit(key)

        if ok:
            result_label.config(text="✔︎ Arquivos restaurados", fg="green")
            root.after(2000, root.destroy)
        else:
            result_label.config(
                text="✖︎ Chave inválida — tente novamente",
                fg="red"
            )
            entry.delete(0, tk.END)
            botao.config(state="normal")

    def sair():
        result_label.config(
            text="✖︎ Não é possível sair sem a chave",
            fg="red"
        )

    entry.bind("<Return>", lambda e: submit())
    root.bind_all("<Escape>", lambda e: sair())

    botao = tk.Button(
        frame,
        text="DESBLOQUEAR",
        command=submit,
        bg="red",
        fg="white",
        font=("Courier", 14, "bold"),
        width=20
    )
    botao.pack(pady=20)

    root.mainloop()